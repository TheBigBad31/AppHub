"""
Application FastAPI principale pour le portail AppHub.
Fournit le catalogue d'applications, les endpoints de vérification de disponibilité en direct,
la consultation des derniers changements GitHub et les flux d'actualités.
"""
import os
import json
import time
import urllib.request
import urllib.error
from pathlib import Path
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "apps.json"
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="AppHub API",
    description="Portail centralisé et catalogue des applications Vercel de Sébastien (TheBigBad31)",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


from src.catalog_data import DEFAULT_APPS_CATALOG


def load_apps_catalog() -> List[Dict[str, Any]]:
    """
    Charge le catalogue d'applications depuis data/apps.json s'il existe et est valide.
    Bascule automatiquement sur DEFAULT_APPS_CATALOG (en mémoire) dans les environnements
    serverless isolés comme Vercel Lambda.
    """
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data and isinstance(data, list) and len(data) > 0:
                    return data
        except Exception as e:
            print(f"Avertissement: Impossible de lire apps.json ({e}), utilisation du catalogue en mémoire.")

    return [dict(app) for app in DEFAULT_APPS_CATALOG]


def ping_url(url: str, timeout: float = 6.0) -> Dict[str, Any]:
    """Teste la disponibilité d'une URL et mesure le temps de réponse."""
    start_time = time.time()
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "AppHub-HealthCheck/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            latency_ms = int((time.time() - start_time) * 1000)
            status_code = response.status
            return {
                "online": 200 <= status_code < 400,
                "status_code": status_code,
                "latency_ms": latency_ms,
                "error": None
            }
    except urllib.error.HTTPError as e:
        latency_ms = int((time.time() - start_time) * 1000)
        return {
            "online": False,
            "status_code": e.code,
            "latency_ms": latency_ms,
            "error": f"HTTP {e.code}"
        }
    except Exception as e:
        latency_ms = int((time.time() - start_time) * 1000)
        return {
            "online": False,
            "status_code": 0,
            "latency_ms": latency_ms,
            "error": str(e)
        }


@app.get("/api/health")
def health():
    """Vérification de santé de l'API AppHub."""
    return {"status": "ok", "service": "AppHub", "timestamp": time.time()}


@app.get("/api/apps")
def get_apps(check_status: bool = Query(False, description="Vérifier la disponibilité HTTP en direct")):
    """Retourne la liste de toutes les applications avec détails et statut optionnel."""
    apps = load_apps_catalog()
    if check_status:
        for item in apps:
            url = item.get("vercel_url")
            if url:
                item["live_status"] = ping_url(url)
    return apps


@app.get("/api/apps/{app_id}")
def get_app_detail(app_id: str, check_status: bool = Query(True)):
    """Retourne les détails complets d'une application spécifique."""
    apps = load_apps_catalog()
    app_data = next((a for a in apps if a.get("id") == app_id.lower()), None)
    if not app_data:
        raise HTTPException(status_code=404, detail=f"Application {app_id} introuvable")

    if check_status and app_data.get("vercel_url"):
        app_data["live_status"] = ping_url(app_data["vercel_url"])

    return app_data


@app.get("/api/apps/{app_id}/status")
def check_app_status(app_id: str):
    """Vérifie la disponibilité en direct de l'URL Vercel d'une application."""
    apps = load_apps_catalog()
    app_data = next((a for a in apps if a.get("id") == app_id.lower()), None)
    if not app_data:
        raise HTTPException(status_code=404, detail=f"Application {app_id} introuvable")

    url = app_data.get("vercel_url")
    if not url:
        return {"online": False, "error": "Pas d'URL Vercel configurée"}

    result = ping_url(url)
    result["url"] = url
    result["app_id"] = app_id
    result["app_name"] = app_data.get("name")
    return result


@app.get("/api/apps/{app_id}/changes")
def get_app_changes(app_id: str, refresh: bool = Query(False)):
    """
    Retourne l'historique des derniers changements et commits de l'application.
    Si refresh=true, tente d'interroger directement l'API GitHub si disponible.
    """
    apps = load_apps_catalog()
    app_data = next((a for a in apps if a.get("id") == app_id.lower()), None)
    if not app_data:
        raise HTTPException(status_code=404, detail=f"Application {app_id} introuvable")

    commits = app_data.get("commits", [])
    latest_summary = app_data.get("latest_summary", "")

    if refresh:
        from src.sync_catalog import get_repo_commits, get_git_credential_token
        repo_url = app_data.get("github_url", "")
        if "github.com/" in repo_url:
            parts = repo_url.replace("https://github.com/", "").split("/")
            if len(parts) >= 2:
                token = get_git_credential_token()
                fresh_commits = get_repo_commits(parts[0], parts[1], token=token, count=10)
                if fresh_commits:
                    commits = fresh_commits

    return {
        "app_id": app_id,
        "name": app_data.get("name"),
        "github_url": app_data.get("github_url"),
        "latest_summary": latest_summary,
        "last_updated": app_data.get("last_updated"),
        "commits": commits
    }


@app.get("/api/feed")
def get_recent_activity():
    """
    Retourne une timeline consolidée de tous les récents commits et mises à jour
    sur l'ensemble des applications du portail.
    """
    apps = load_apps_catalog()
    timeline = []
    for app_item in apps:
        app_name = app_item.get("name")
        app_id = app_item.get("id")
        app_color = app_item.get("color", "indigo")
        for c in app_item.get("commits", []):
            timeline.append({
                "app_id": app_id,
                "app_name": app_name,
                "app_color": app_color,
                "sha": c.get("sha"),
                "message": c.get("message"),
                "author": c.get("author"),
                "date": c.get("date"),
                "url": c.get("url")
            })

    timeline.sort(key=lambda x: x.get("date", ""), reverse=True)
    return {
        "total_updates": len(timeline),
        "updates": timeline
    }


@app.get("/", response_class=HTMLResponse)
def serve_index():
    candidates = [
        STATIC_DIR / "index.html",
        BASE_DIR / "index.html",
        BASE_DIR / "public" / "index.html",
    ]
    for candidate in candidates:
        if candidate.exists():
            try:
                with open(candidate, "r", encoding="utf-8") as f:
                    return HTMLResponse(content=f.read())
            except Exception:
                pass
    return HTMLResponse("<h1>Portail AppHub</h1><p>Index.html manquant.</p>")


# Montage des fichiers statiques si le répertoire existe
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
