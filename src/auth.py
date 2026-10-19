"""
Gestion de l'authentification Google Sign-In (OAuth2 / Google Identity Services)
et des sessions utilisateur pour le portail central AppHub.
"""
import os
import json
import base64
import time
import secrets
from pathlib import Path
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR / "data" / "auth_config.json"
USERS_FILE = BASE_DIR / "data" / "users.json"

DEFAULT_GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "")
ADMIN_EMAIL = "sebastienlamoliate@gmail.com"
ADMIN_NAME = "Sébastien LAMOLIATE"
ADMIN_PICTURE = "https://lh3.googleusercontent.com/a/default-user=s96-c"

# Mémoire de secours pour environnements Serverless (Vercel Lambda)
_memory_auth_config: Dict[str, Any] = {
    "google_client_id": DEFAULT_GOOGLE_CLIENT_ID,
    "sso_enabled": True,
    "suggested_account": {
        "email": ADMIN_EMAIL,
        "name": ADMIN_NAME,
        "picture": ADMIN_PICTURE
    }
}

_memory_sessions: Dict[str, Dict[str, Any]] = {}
_memory_user_prefs: Dict[str, Dict[str, Any]] = {
    ADMIN_EMAIL: {
        "email": ADMIN_EMAIL,
        "name": ADMIN_NAME,
        "picture": ADMIN_PICTURE,
        "pinned_apps": ["cryptoplatform", "vitaltrack"],
        "theme": "dark"
    }
}


class GoogleAuthPayload(BaseModel):
    credential: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    picture: Optional[str] = None
    sub: Optional[str] = None
    pinned_apps: Optional[List[str]] = None
    theme: Optional[str] = None


class AuthConfigUpdate(BaseModel):
    google_client_id: Optional[str] = None
    sso_enabled: Optional[bool] = None


def get_auth_config() -> Dict[str, Any]:
    """Charge la configuration auth depuis data/auth_config.json ou mémoire."""
    client_id = _memory_auth_config.get("google_client_id") or os.environ.get("GOOGLE_CLIENT_ID", "")
    sso_enabled = _memory_auth_config.get("sso_enabled", True)

    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                client_id = data.get("google_client_id", client_id)
                sso_enabled = data.get("sso_enabled", sso_enabled)
        except Exception as e:
            print(f"Avertissement lecture auth_config: {e}")

    return {
        "google_client_id": client_id,
        "sso_enabled": sso_enabled,
        "is_configured": bool(client_id),
        "suggested_account": {
            "email": ADMIN_EMAIL,
            "name": ADMIN_NAME,
            "picture": ADMIN_PICTURE
        }
    }


def save_auth_config(client_id: Optional[str] = None, sso_enabled: Optional[bool] = None) -> Dict[str, Any]:
    """Met à jour et persiste la configuration auth."""
    current = get_auth_config()
    if client_id is not None:
        current["google_client_id"] = client_id.strip()
        current["is_configured"] = bool(client_id.strip())
        _memory_auth_config["google_client_id"] = client_id.strip()
    if sso_enabled is not None:
        current["sso_enabled"] = sso_enabled
        _memory_auth_config["sso_enabled"] = sso_enabled

    try:
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({
                "google_client_id": current["google_client_id"],
                "sso_enabled": current["sso_enabled"]
            }, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Avertissement sauvegarde auth_config sur disque: {e}")

    return current


def decode_jwt_unverified(token: str) -> Dict[str, Any]:
    """
    Décode les claims d'un ID token JWT sans bibliothèque tierce lourde.
    En environnement serverless / browser token, permet de lire sub, email, name, picture.
    """
    try:
        parts = token.split(".")
        if len(parts) >= 2:
            payload_b64 = parts[1]
            # Rajouter padding si nécessaire
            rem = len(payload_b64) % 4
            if rem > 0:
                payload_b64 += "=" * (4 - rem)
            decoded = base64.urlsafe_b64decode(payload_b64.encode("utf-8")).decode("utf-8")
            return json.loads(decoded)
    except Exception as e:
        print(f"Erreur parsing JWT Google: {e}")
    return {}


def get_user_profile(email: str) -> Dict[str, Any]:
    """Récupère le profil et les préférences utilisateur."""
    if email in _memory_user_prefs:
        return _memory_user_prefs[email]

    if USERS_FILE.exists():
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                users = json.load(f)
                if email in users:
                    _memory_user_prefs[email] = users[email]
                    return users[email]
        except Exception:
            pass

    # Profil par défaut
    is_admin = (email.lower() == ADMIN_EMAIL.lower())
    default_profile = {
        "email": email,
        "name": ADMIN_NAME if is_admin else email.split("@")[0].capitalize(),
        "picture": ADMIN_PICTURE if is_admin else "",
        "pinned_apps": ["cryptoplatform", "vitaltrack"] if is_admin else [],
        "theme": "dark"
    }
    _memory_user_prefs[email] = default_profile
    return default_profile


def save_user_profile(profile: Dict[str, Any]) -> None:
    """Enregistre le profil et les préférences en mémoire et sur disque."""
    email = profile.get("email")
    if not email:
        return
    _memory_user_prefs[email] = profile

    try:
        data = {}
        if USERS_FILE.exists():
            try:
                with open(USERS_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except Exception:
                data = {}
        data[email] = profile
        USERS_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(USERS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Avertissement écriture users.json: {e}")


def authenticate_google_user(payload: GoogleAuthPayload) -> Dict[str, Any]:
    """
    Authentifie l'utilisateur Google soit via ID Token (GIS), soit via données Quick-Sign.
    Crée une session et renvoie les informations utilisateur et le token de session.
    """
    email = payload.email
    name = payload.name
    picture = payload.picture
    sub = payload.sub

    if payload.credential:
        claims = decode_jwt_unverified(payload.credential)
        if claims:
            email = claims.get("email", email)
            name = claims.get("name", name)
            picture = claims.get("picture", picture)
            sub = claims.get("sub", sub)

    if not email:
        email = ADMIN_EMAIL

    if not name:
        name = ADMIN_NAME if email.lower() == ADMIN_EMAIL.lower() else email.split("@")[0].capitalize()

    if not picture:
        picture = ADMIN_PICTURE if email.lower() == ADMIN_EMAIL.lower() else "https://lh3.googleusercontent.com/a/default-user=s96-c"

    if not sub:
        sub = f"google_sub_{secrets.token_hex(8)}"

    # Mettre à jour profil et préférences si fournis
    profile = get_user_profile(email)
    profile["name"] = name
    profile["picture"] = picture
    profile["sub"] = sub
    if payload.pinned_apps is not None:
        profile["pinned_apps"] = payload.pinned_apps
    if payload.theme is not None:
        profile["theme"] = payload.theme
    save_user_profile(profile)

    # Créer session
    session_token = f"apphub_sess_{secrets.token_urlsafe(32)}"
    session_data = {
        "session_token": session_token,
        "email": email,
        "name": name,
        "picture": picture,
        "sub": sub,
        "authenticated_via": "google",
        "created_at": time.time(),
        "pinned_apps": profile.get("pinned_apps", []),
        "theme": profile.get("theme", "dark")
    }
    _memory_sessions[session_token] = session_data

    return session_data


def get_current_user_from_token(token: Optional[str]) -> Optional[Dict[str, Any]]:
    """Retourne la session active si le token est valide."""
    if not token:
        return None
    cleaned_token = token.replace("Bearer ", "").strip()
    session = _memory_sessions.get(cleaned_token)
    if not session:
        return None
    # Recharger les préférences à jour
    profile = get_user_profile(session["email"])
    session["pinned_apps"] = profile.get("pinned_apps", [])
    session["theme"] = profile.get("theme", "dark")
    return session


def revoke_session(token: Optional[str]) -> bool:
    """Déconnexion / révocation de la session."""
    if not token:
        return False
    cleaned_token = token.replace("Bearer ", "").strip()
    if cleaned_token in _memory_sessions:
        del _memory_sessions[cleaned_token]
        return True
    return False
