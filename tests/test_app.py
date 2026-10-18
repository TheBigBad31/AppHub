"""
Tests unitaires pour l'API AppHub et le catalogue d'applications.
"""
import pytest
from fastapi.testclient import TestClient
from src.app import app, load_apps_catalog, ping_url

client = TestClient(app)


def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "AppHub"


def test_load_apps_catalog():
    apps = load_apps_catalog()
    assert len(apps) >= 4
    app_ids = [a["id"] for a in apps]
    assert "cryptoplatform" in app_ids
    assert "cognistim" in app_ids
    assert "galaxydefenders" in app_ids
    assert "elvishscout" in app_ids


def test_get_apps():
    response = client.get("/api/apps")
    assert response.status_code == 200
    apps = response.json()
    assert len(apps) >= 4
    
    # Vérification des propriétés requises
    for app_item in apps:
        assert "name" in app_item
        assert "vercel_url" in app_item
        assert "github_url" in app_item
        assert "category" in app_item
        assert "features" in app_item
        assert len(app_item["features"]) > 0


def test_get_app_detail_found():
    response = client.get("/api/apps/cryptoplatform?check_status=false")
    assert response.status_code == 200
    app_data = response.json()
    assert app_data["id"] == "cryptoplatform"
    assert "CryptoPlatform" in app_data["name"]
    assert "https://crypto-platform-blue.vercel.app" in app_data["vercel_url"]


def test_get_app_detail_not_found():
    response = client.get("/api/apps/unknown_app_404")
    assert response.status_code == 404


def test_get_app_changes():
    response = client.get("/api/apps/galaxydefenders/changes")
    assert response.status_code == 200
    data = response.json()
    assert data["app_id"] == "galaxydefenders"
    assert "commits" in data
    assert len(data["commits"]) > 0
    assert "sha" in data["commits"][0]
    assert "message" in data["commits"][0]


def test_get_feed():
    response = client.get("/api/feed")
    assert response.status_code == 200
    feed = response.json()
    assert "total_updates" in feed
    assert "updates" in feed
    assert feed["total_updates"] > 0
    assert "message" in feed["updates"][0]
    assert "app_name" in feed["updates"][0]


def test_ping_url_invalid():
    res = ping_url("http://invalid-domain-name-that-does-not-exist.xyz", timeout=1.0)
    assert res["online"] is False
    assert res["status_code"] == 0


def test_fallback_when_apps_json_missing(monkeypatch, tmp_path):
    import src.app as app_module
    fake_data_file = tmp_path / "non_existent_apps.json"
    monkeypatch.setattr(app_module, "DATA_FILE", fake_data_file)
    apps = app_module.load_apps_catalog()
    assert len(apps) == 4
    app_ids = [a["id"] for a in apps]
    assert "cryptoplatform" in app_ids
    assert "cognistim" in app_ids
    assert "galaxydefenders" in app_ids
    assert "elvishscout" in app_ids
