"""
Synchronisation et inspection des dépôts GitHub de TheBigBad31 pour le catalogue AppHub.
Peut être exécuté en ligne de commande : python -m src.sync_catalog
"""
import os
import json
import base64
import subprocess
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional

APPS_DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "apps.json"


def get_git_credential_token() -> Optional[str]:
    """Tente de récupérer le token GitHub via git credential fill ou la variable d'environnement."""
    token = os.getenv("GITHUB_TOKEN")
    if token:
        return token

    try:
        proc = subprocess.Popen(
            ["git", "credential", "fill"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, _ = proc.communicate(input="protocol=https\nhost=github.com\n", timeout=5)
        for line in stdout.splitlines():
            if line.startswith("password="):
                return line.split("=", 1)[1].strip()
    except Exception:
        pass
    return None


def fetch_github_api(endpoint: str, token: Optional[str] = None) -> Any:
    """Interroge l'API REST de GitHub avec gestion des headers."""
    url = f"https://api.github.com{endpoint}"
    headers = {"User-Agent": "AppHub-Catalog-Sync", "Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_repo_commits(repo_owner: str, repo_name: str, token: Optional[str] = None, count: int = 5) -> List[Dict[str, Any]]:
    """Récupère les derniers commits d'un dépôt GitHub."""
    endpoint = f"/repos/{repo_owner}/{repo_name}/commits?per_page={count}"
    try:
        data = fetch_github_api(endpoint, token)
        commits = []
        for c in data:
            commit_info = c.get("commit", {})
            sha = c.get("sha", "")[:7]
            full_sha = c.get("sha", "")
            msg = commit_info.get("message", "").split("\n")[0]
            author = commit_info.get("author", {}).get("name", "Unknown")
            date = commit_info.get("author", {}).get("date", "")
            commits.append({
                "sha": sha,
                "full_sha": full_sha,
                "message": msg,
                "author": author,
                "date": date,
                "url": f"https://github.com/{repo_owner}/{repo_name}/commit/{full_sha}"
            })
        return commits
    except Exception as e:
        print(f"Erreur lors de la récupération des commits pour {repo_name}: {e}")
        return []


def sync_catalog(output_path: Path = APPS_DATA_FILE) -> List[Dict[str, Any]]:
    """Synchronise les métadonnées et commits récents des applications répertoriées."""
    token = get_git_credential_token()
    if not output_path.exists():
        current_apps = []
    else:
        try:
            with open(output_path, "r", encoding="utf-8") as f:
                current_apps = json.load(f)
        except Exception:
            current_apps = []

    updated_apps = []
    for app in current_apps:
        repo_url = app.get("github_url", "")
        if "github.com/" in repo_url:
            parts = repo_url.replace("https://github.com/", "").split("/")
            if len(parts) >= 2:
                owner, repo_name = parts[0], parts[1]
                commits = get_repo_commits(owner, repo_name, token, count=6)
                if commits:
                    app["commits"] = commits
                    app["last_updated"] = commits[0]["date"]
        updated_apps.append(app)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(updated_apps, f, indent=2, ensure_ascii=False)

    # Met également à jour src/catalog_data.py pour garantir la parité du fallback en mémoire
    catalog_py_path = Path(__file__).resolve().parent / "catalog_data.py"
    try:
        content_py = '"""\nCatalogue statique par défaut des applications pour AppHub.\nSert de source de données infaillible et de fallback en mémoire\ndans les environnements serverless Vercel lorsque le fichier apps.json n\'est pas bundlé.\n"""\nfrom typing import List, Dict, Any\n\nDEFAULT_APPS_CATALOG: List[Dict[str, Any]] = ' + json.dumps(updated_apps, indent=2, ensure_ascii=False) + '\n'
        with open(catalog_py_path, "w", encoding="utf-8") as f:
            f.write(content_py)
    except Exception as e:
        print(f"Avertissement: Impossible d'écrire {catalog_py_path}: {e}")

    print(f"Catalogue synchronisé avec succès ({len(updated_apps)} applications) dans {output_path} et {catalog_py_path}")
    return updated_apps


if __name__ == "__main__":
    sync_catalog()
