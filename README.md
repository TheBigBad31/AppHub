# AppHub — Portail Central des Applications

Portail centralisé et catalogue interactif regroupant toutes les applications GitHub de **Sébastien (TheBigBad31)** déployées sur **Vercel** :
- **CryptoPlatform** : Plateforme modulaire d'investissement crypto & tableaux de bord financiers interactifs (`https://crypto-platform-blue.vercel.app`)
- **CogniStim** : Générateur en ligne d'exercices de stimulation cognitive (`https://cognistim.vercel.app`)
- **GalaxyDefenders** : Shoot'em up spatial rétro-futuriste avec IA taunts & armada HD (`https://galaxy-defenders-ecru.vercel.app`)
- **ElvishScout** : Démineur tactique et d'aventure dans une forêt enchantée (`https://elvish-scout.vercel.app`)

---

## 🌟 Fonctionnalités Clés du Portail

1. **Lancement 1-Clic & Expérience Moderne** :
   - Interface réactive et soignée avec bascule thème sombre/clair.
   - Boutons de lancement direct vers les applications déployées en production sur Vercel.
   - Liens directs vers chaque dépôt GitHub (publics et privés).

2. **Monitoring & Disponibilité en Direct** :
   - Indicateur live de statut HTTP (`200 OK`) et mesure de latence en millisecondes.
   - Bouton d'actualisation instantanée de l'état de l'écosystème.

3. **Derniers Changements à la Demande (« Quoi de neuf ? »)** :
   - Modale interactive pour chaque application résumant les dernières évolutions techniques en français.
   - Timeline des derniers commits GitHub avec date, auteur et liens vers les commits.
   - Bouton de rafraîchissement à chaud interrogeant directement l'API GitHub.

4. **Fil d'Actualité Consolidé** :
   - Vue globale chronologique des derniers commits et mises à jour toutes applications confondues.

5. **Outil CLI de Synchronisation Automatique** :
   - Script `python -m src.sync_catalog` réutilisable par l'Autopilot pour découvrir et mettre à jour le catalogue.

---

## 🚀 Lancement Local

### Prérequis
- Python 3.11+
- `uv` ou `pip`

### Installation & Démarrage
```bash
# Créer et activer l'environnement
uv venv
source .venv/bin/activate  # ou .venv\Scripts\activate sous Windows

# Installer les dépendances
uv pip install -r requirements.txt

# Lancer le serveur local
uvicorn src.app:app --reload --port 8000
```
Le portail est accessible sur `http://localhost:8000`.

---

## 🧪 Tests Unitaires

```bash
pytest tests -v
```

---

## ☁️ Déploiement Vercel

Le projet est configuré pour un déploiement Vercel Serverless immédiat via `vercel.json` et `api/index.py`.
Pour déployer :
```bash
vercel deploy --prod
```
