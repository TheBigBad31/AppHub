"""
Point d'entrée Serverless Vercel pour l'API AppHub.
Expose l'instance FastAPI `app`.
"""
import sys
from pathlib import Path

# Assurer que la racine du projet est dans sys.path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from src.app import app
