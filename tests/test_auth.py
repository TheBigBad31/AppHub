"""
Tests unitaires pour l'authentification Google Sign-In et les sessions utilisateur.
"""
import pytest
from fastapi.testclient import TestClient
from src.app import app
import src.auth as auth_module

client = TestClient(app)


def test_auth_config_default():
    response = client.get("/api/auth/config")
    assert response.status_code == 200
    data = response.json()
    assert "google_client_id" in data
    assert "sso_enabled" in data
    assert data["sso_enabled"] is True
    assert "suggested_account" in data
    assert data["suggested_account"]["email"] == "sebastienlamoliate@gmail.com"


def test_update_auth_config():
    payload = {"google_client_id": "test-client-id-12345.apps.googleusercontent.com", "sso_enabled": True}
    response = client.put("/api/auth/config", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["google_client_id"] == "test-client-id-12345.apps.googleusercontent.com"
    assert data["is_configured"] is True

    # Vérification que GET reflète la mise à jour
    check = client.get("/api/auth/config")
    assert check.json()["google_client_id"] == "test-client-id-12345.apps.googleusercontent.com"


def test_login_with_google_quick_sign():
    # Connexion directe avec le compte Google pré-proposé
    payload = {
        "email": "sebastienlamoliate@gmail.com",
        "name": "Sébastien LAMOLIATE",
        "picture": "https://lh3.googleusercontent.com/a/default-user=s96-c",
        "pinned_apps": ["cryptoplatform", "vitaltrack"]
    }
    response = client.post("/api/auth/google", json=payload)
    assert response.status_code == 200
    res_data = response.json()
    assert res_data["status"] == "success"
    assert "session_token" in res_data
    assert res_data["user"]["email"] == "sebastienlamoliate@gmail.com"
    assert "cryptoplatform" in res_data["user"]["pinned_apps"]

    session_token = res_data["session_token"]

    # Test /api/auth/me avec token valide
    me_resp = client.get("/api/auth/me", headers={"Authorization": f"Bearer {session_token}"})
    assert me_resp.status_code == 200
    me_data = me_resp.json()
    assert me_data["authenticated"] is True
    assert me_data["user"]["email"] == "sebastienlamoliate@gmail.com"
    assert me_data["user"]["name"] == "Sébastien LAMOLIATE"

    # Test mise à jour des préférences (favoris / pinned apps)
    pref_payload = {"pinned_apps": ["cryptoplatform", "vitaltrack", "cognistim"], "theme": "dark"}
    pref_resp = client.put("/api/auth/preferences", json=pref_payload, headers={"Authorization": f"Bearer {session_token}"})
    assert pref_resp.status_code == 200
    pref_data = pref_resp.json()
    assert "cognistim" in pref_data["pinned_apps"]

    # Vérification que /api/auth/me reflète les nouvelles apps épinglées
    me_resp_updated = client.get("/api/auth/me", headers={"Authorization": f"Bearer {session_token}"})
    assert "cognistim" in me_resp_updated.json()["user"]["pinned_apps"]

    # Déconnexion
    logout_resp = client.post("/api/auth/logout", headers={"Authorization": f"Bearer {session_token}"})
    assert logout_resp.status_code == 200
    assert logout_resp.json()["logged_out"] is True

    # Vérification que la session est invalidée
    me_after_logout = client.get("/api/auth/me", headers={"Authorization": f"Bearer {session_token}"})
    assert me_after_logout.status_code == 200
    assert me_after_logout.json()["authenticated"] is False


def test_auth_me_unauthenticated():
    response = client.get("/api/auth/me")
    assert response.status_code == 200
    data = response.json()
    assert data["authenticated"] is False
    assert data["user"] is None
