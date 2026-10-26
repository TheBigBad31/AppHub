"""
Catalogue statique par défaut des applications pour AppHub.
Sert de source de données infaillible et de fallback en mémoire
dans les environnements serverless Vercel lorsque le fichier apps.json n'est pas bundlé.
"""
from typing import List, Dict, Any

DEFAULT_APPS_CATALOG: List[Dict[str, Any]] = [
  {
    "id": "cryptoplatform",
    "name": "CryptoPlatform",
    "tagline": "Plateforme d'investissement crypto & dashboards paramétrables",
    "description": "Plateforme complète de gestion de portefeuille crypto, détection d'opportunités de marché (RSI, Dips 24h), alertes WhatsApp en temps réel et tableaux de bord financiers interactifs.",
    "category": "Finance & Crypto",
    "icon": "trending-up",
    "color": "emerald",
    "vercel_url": "https://crypto-platform-blue.vercel.app",
    "github_url": "https://github.com/TheBigBad31/CryptoPlatform",
    "is_private": True,
    "language": "Python",
    "stack": [
      "FastAPI",
      "Python 3.11",
      "Google Sign-In SSO",
      "Kraken API",
      "Nexo API",
      "WhatsApp API",
      "Chart.js",
      "Tailwind CSS"
    ],
    "features": [
      "Authentification unifiée Google Sign-In & SSO depuis AppHub",
      "Connecteurs modulaires CEX & CeFi (Kraken read-only, Nexo Pro, mode démo sans clés)",
      "Moteur d'indicateurs techniques (RSI de Wilder, Moyennes mobiles SMA/EMA, variations 24h/7j)",
      "Alertes instantanées WhatsApp (CallMeBot, Meta Cloud API, Twilio) avec règles anti-spam",
      "Tableaux de bord interactifs paramétrables (conversion multi-devises EUR/USD/BTC, sliders RSI à la volée)",
      "Suivi des rendements passifs (Staking Kraken & Fixed Terms Nexo, calcul APY en direct)"
    ],
    "latest_summary": "Intégration du calibrage des alertes, profils de dashboard 1-clic, pipelines CI/CD et déploiement Vercel Serverless.",
    "last_updated": "2026-10-19T10:04:43Z",
    "commits": [
      {
        "sha": "0fe84cf",
        "full_sha": "0fe84cf7d9958e57b8e1344f34206cbcdfdeab66",
        "message": "feat(auth): ecran Google Choisir un compte, resilience au clic et fallback localStorage",
        "author": "TheBigBad31",
        "date": "2026-10-19T10:04:43Z",
        "url": "https://github.com/TheBigBad31/CryptoPlatform/commit/0fe84cf7d9958e57b8e1344f34206cbcdfdeab66"
      },
      {
        "sha": "0b4427e",
        "full_sha": "0b4427e2c110806a61647e414fb108b474a59216",
        "message": "feat(auth): ajout de l'authentification Google Sign-In (OAuth2 / GIS) et persistance des preferences",
        "author": "TheBigBad31",
        "date": "2026-10-19T07:31:55Z",
        "url": "https://github.com/TheBigBad31/CryptoPlatform/commit/0b4427e2c110806a61647e414fb108b474a59216"
      },
      {
        "sha": "75f9dbc",
        "full_sha": "75f9dbc910e183ab074127f4f0120dd62de7d3b1",
        "message": "feat(stage-4): Calibrage des paramètres d'alertes, profils de dashboard 1-clic et audit d'opportunités (BALI-7)",
        "author": "TheBigBad31",
        "date": "2026-10-18T13:16:09Z",
        "url": "https://github.com/TheBigBad31/CryptoPlatform/commit/75f9dbc910e183ab074127f4f0120dd62de7d3b1"
      },
      {
        "sha": "7290556",
        "full_sha": "7290556e57573532ed295887006f40b9c62992a0",
        "message": "feat(ci-cd): Add GitHub Actions CI/CD workflows and complete Vercel documentation (BALI-8)",
        "author": "TheBigBad31",
        "date": "2026-10-18T08:49:18Z",
        "url": "https://github.com/TheBigBad31/CryptoPlatform/commit/7290556e57573532ed295887006f40b9c62992a0"
      },
      {
        "sha": "c6a8c5e",
        "full_sha": "c6a8c5edf4dd3b3a787b1bd610748e409243c7ec",
        "message": "feat(stage-3): Dashboards interactifs paramétrables, connecteurs multi-comptes, alertes WhatsApp et déploiement Vercel",
        "author": "TheBigBad31",
        "date": "2026-10-18T08:45:09Z",
        "url": "https://github.com/TheBigBad31/CryptoPlatform/commit/c6a8c5edf4dd3b3a787b1bd610748e409243c7ec"
      }
    ]
  },
  {
    "id": "cognistim",
    "name": "CogniStim",
    "tagline": "Générateur en ligne d'exercices de stimulation cognitive",
    "description": "Application web avancée dédiée à l'entraînement cérébral et aux professionnels de santé. Génération d'exercices variés (chiffres, symboles, labyrinthes, sudokus visuels, mémoire) avec fiches d'exercices prêtes à imprimer ou à pratiquer.",
    "category": "Santé & Cognition",
    "icon": "brain",
    "color": "indigo",
    "vercel_url": "https://cognistim.vercel.app",
    "github_url": "https://github.com/TheBigBad31/CogniStim",
    "is_private": True,
    "language": "TypeScript",
    "stack": [
      "Next.js 15",
      "React 19",
      "TypeScript",
      "Google Sign-In SSO",
      "Tailwind CSS",
      "Drizzle ORM",
      "PostgreSQL"
    ],
    "features": [
      "Authentification unifiée Google Sign-In & SSO depuis AppHub",
      "Générateur d'exercices cognitifs paramétrables (Chiffrement, Lettres manquantes, Sudoku à symboles)",
      "Labyrinthes de lettres et grilles de mots avec réglage fin de linéarité et difficulté",
      "Calculs codés, suites logiques et mémorisation de tables de correspondance",
      "Impression et export de feuilles d'exercices prêtes pour la pratique en atelier clinique ou personnel",
      "Architecture full-stack Next.js avec base de données PostgreSQL via Drizzle ORM"
    ],
    "latest_summary": "Intégration de l'authentification Google (Account Chooser GIS), compatibilité SSO AppHub (?google_user) et optimisations ESLint.",
    "last_updated": "2026-10-25T12:07:00+01:00",
    "commits": [
      {
        "sha": "df278dc",
        "full_sha": "df278dcc83dc423121c016c10abf9fdadeacafe0",
        "message": "feat(auth): ajout du SSO AppHub (?google_user), Google Account Chooser (GIS) et nettoyage ESLint",
        "author": "TheBigBad31",
        "date": "2026-10-25T12:07:00+01:00",
        "url": "https://github.com/TheBigBad31/CogniStim/commit/df278dcc83dc423121c016c10abf9fdadeacafe0"
      },
      {
        "sha": "f8bd2e4",
        "full_sha": "f8bd2e462334a85a52a7805f8c71af1458330df4",
        "message": "Ajout d'un parametre Linearité pour le Labyrinthe de lettres",
        "author": "TheBigBad31",
        "date": "2026-10-09T18:32:05+02:00",
        "url": "https://github.com/TheBigBad31/CogniStim/commit/f8bd2e462334a85a52a7805f8c71af1458330df4"
      },
      {
        "sha": "bc7a80e",
        "full_sha": "bc7a80e4f76945fd7163fd603f0b44ece98f6293",
        "message": "Initial commit: CogniStim Next.js project",
        "author": "TheBigBad31",
        "date": "2026-10-05T11:46:26+02:00",
        "url": "https://github.com/TheBigBad31/CogniStim/commit/bc7a80e4f76945fd7163fd603f0b44ece98f6293"
      }
    ]
  },
  {
    "id": "galaxydefenders",
    "name": "GalaxyDefenders",
    "tagline": "Shoot'em up spatial rétro-futuriste avec IA taunts & graphismes HD",
    "description": "Shoot'em up d'arcade frénétique développé avec HTML5 Canvas et React. Pilotez 6 vaisseaux uniques, affrontez une armada ennemie cyber-militaire en vue 2D Top-Down avec des visuels HD générés par IA et des effets de particules rétro néon.",
    "category": "Jeux & Arcade",
    "icon": "rocket",
    "color": "cyan",
    "vercel_url": "https://galaxy-defenders-ecru.vercel.app",
    "github_url": "https://github.com/TheBigBad31/GalaxyDefenders",
    "is_private": False,
    "language": "TypeScript",
    "stack": [
      "React",
      "HTML5 Canvas",
      "Vite",
      "Google Sign-In SSO",
      "TypeScript",
      "Tailwind CSS",
      "Gemini AI"
    ],
    "features": [
      "Authentification unifiée Google Sign-In & SSO depuis AppHub",
      "Moteur de jeu 60 FPS Canvas avec gestion physique des inclinaisons et tirs multi-canons",
      "Armada ennemie complète avec 12 visuels HD PNG transparents (moteur Cyber-Militaire Style 2)",
      "6 vaisseaux jouables distincts (Bolton, Jeff, Micka, etc.) aux caractéristiques uniques",
      "Système de particules rétro néon, explosions lumineuses et textes flottants",
      "Provocations et réactions dynamiques des boss extraterrestres générées par IA"
    ],
    "latest_summary": "Intégration du service d'authentification Google (Account Chooser) et synchronisation SSO AppHub (?google_user).",
    "last_updated": "2026-10-25T11:59:53+01:00",
    "commits": [
      {
        "sha": "c22684b",
        "full_sha": "c22684b11a5ed9bed5b8e69412270587a1ed0eb5",
        "message": "feat(auth): integration du service d'authentification Google (Account Chooser) et SSO AppHub (?google_user=)",
        "author": "TheBigBad31",
        "date": "2026-10-25T11:59:53+01:00",
        "url": "https://github.com/TheBigBad31/GalaxyDefenders/commit/c22684b11a5ed9bed5b8e69412270587a1ed0eb5"
      },
      {
        "sha": "633653a",
        "full_sha": "633653a532f4e34f3bd3fdb84a8f0c8a7fcfbc62",
        "message": "Integration des 12 nouveaux visuels HD PNG Gemini pour toute l'armada ennemie Style 2",
        "author": "TheBigBad31",
        "date": "2026-08-02T22:19:00+02:00",
        "url": "https://github.com/TheBigBad31/GalaxyDefenders/commit/633653a532f4e34f3bd3fdb84a8f0c8a7fcfbc62"
      },
      {
        "sha": "cc85651",
        "full_sha": "cc856512776706d2c6d2d393c65fc7c22791e2a1",
        "message": "Integration du visuel HD officiel pour le vaisseau ennemi SCOUT avec filtre de transparence automatique",
        "author": "TheBigBad31",
        "date": "2026-08-02T20:33:49+02:00",
        "url": "https://github.com/TheBigBad31/GalaxyDefenders/commit/cc856512776706d2c6d2d393c65fc7c22791e2a1"
      },
      {
        "sha": "a78dac5",
        "full_sha": "a78dac599a08c4103d9311497d4b0ff00743bd67",
        "message": "Preparation de l'architecture d'integration des images HD PNG d'ennemis et de la liste complete des prompts Style 2",
        "author": "TheBigBad31",
        "date": "2026-08-02T20:00:14+02:00",
        "url": "https://github.com/TheBigBad31/GalaxyDefenders/commit/a78dac599a08c4103d9311497d4b0ff00743bd67"
      },
      {
        "sha": "2a848cf",
        "full_sha": "2a848cf81cb7387d842e9d4221ac903cab3a239e",
        "message": "Integration du moteur HD Cyber-Militaire pour la flotte ennemie conforme a la charte officielle Style 2",
        "author": "TheBigBad31",
        "date": "2026-08-02T19:58:04+02:00",
        "url": "https://github.com/TheBigBad31/GalaxyDefenders/commit/2a848cf81cb7387d842e9d4221ac903cab3a239e"
      },
      {
        "sha": "dd2a69c",
        "full_sha": "dd2a69c85cc4b7cff740d65471ecd7f48fbe852c",
        "message": "Nettoyage du code obsolete de generation matricielle de vaisseaux au profit du moteur HD PNG",
        "author": "TheBigBad31",
        "date": "2026-08-02T19:43:36+02:00",
        "url": "https://github.com/TheBigBad31/GalaxyDefenders/commit/dd2a69c85cc4b7cff740d65471ecd7f48fbe852c"
      }
    ]
  },
  {
    "id": "elvishscout",
    "name": "ElvishScout",
    "tagline": "L'Éclaireur Elfe : La Forêt des Gobelins — Déineur tactique & RPG",
    "description": "Jeu de réflexion et de tactique inspiré du démineur dans un univers de dark fantasy. Incarnez un éclaireur elfe explorant une forêt enchantée regorgeant de pièges, de gobelins embusqués, de racines de mandragore et de fleurs magiques.",
    "category": "Jeux & Tactique",
    "icon": "shield",
    "color": "amber",
    "vercel_url": "https://elvish-scout.vercel.app",
    "github_url": "https://github.com/TheBigBad31/ElvishScout",
    "is_private": True,
    "language": "TypeScript",
    "stack": [
      "React",
      "Vite",
      "TypeScript",
      "Google Sign-In SSO",
      "Tailwind CSS",
      "Google GenAI API"
    ],
    "features": [
      "Authentification unifiée Google Sign-In & SSO depuis AppHub",
      "Mécaniques tactiques de démineur revisitées avec système de points de vie et d'armure",
      "Artefacts et plantes légendaires (Fleurs de Gaïa, Racines de Mandragore à déterrer)",
      "Composants de tuiles interactives avec badges de statut et niveaux de menace gobelin",
      "Mode plein écran responsive adapté pour ordinateurs et mobiles (support tactile & drag)",
      "Dialogues et événements narratifs immersifs générés via Google GenAI"
    ],
    "latest_summary": "Intégration de l'authentification Google (Account Chooser) et synchronisation SSO AppHub (?google_user).",
    "last_updated": "2026-10-25T11:46:18+01:00",
    "commits": [
      {
        "sha": "73f13cc",
        "full_sha": "73f13cc509737afdefca509c11e66d2c308b6e6c",
        "message": "feat(auth): ajout du SSO AppHub (?google_user) et Google Account Chooser",
        "author": "TheBigBad31",
        "date": "2026-10-25T11:46:18+01:00",
        "url": "https://github.com/TheBigBad31/ElvishScout/commit/73f13cc509737afdefca509c11e66d2c308b6e6c"
      },
      {
        "sha": "748ca2e",
        "full_sha": "748ca2e777ebacbed7fc9a4455b47134654ed2ee",
        "message": "feat: implement CellContent component to render game tile visual states and metadata badges",
        "author": "TheBigBad31",
        "date": "2026-08-01T07:53:31+02:00",
        "url": "https://github.com/TheBigBad31/ElvishScout/commit/748ca2e777ebacbed7fc9a4455b47134654ed2ee"
      },
      {
        "sha": "d58c88e",
        "full_sha": "d58c88e2b3426cdbacfc51b5fa1c8982a3f868a5",
        "message": "Nerf fleur de gaia",
        "author": "TheBigBad31",
        "date": "2026-08-01T07:49:02+02:00",
        "url": "https://github.com/TheBigBad31/ElvishScout/commit/d58c88e2b3426cdbacfc51b5fa1c8982a3f868a5"
      },
      {
        "sha": "88a5dfd",
        "full_sha": "88a5dfde6cc54a88450e50ed66e020632293b966",
        "message": "nb gobelin Header",
        "author": "TheBigBad31",
        "date": "2026-07-31T13:19:51+02:00",
        "url": "https://github.com/TheBigBad31/ElvishScout/commit/88a5dfde6cc54a88450e50ed66e020632293b966"
      },
      {
        "sha": "9b5512e",
        "full_sha": "9b5512e52b14a595ad53295861784c0cd906e5de",
        "message": "Indicateur de gobelin par niveau",
        "author": "TheBigBad31",
        "date": "2026-07-31T12:22:52+02:00",
        "url": "https://github.com/TheBigBad31/ElvishScout/commit/9b5512e52b14a595ad53295861784c0cd906e5de"
      },
      {
        "sha": "12b757c",
        "full_sha": "12b757ca6f7f1593a0c434379434e60fc2cd7954",
        "message": "Mandragore root upgrade",
        "author": "TheBigBad31",
        "date": "2026-07-30T19:39:32+02:00",
        "url": "https://github.com/TheBigBad31/ElvishScout/commit/12b757ca6f7f1593a0c434379434e60fc2cd7954"
      }
    ]
  },
  {
    "id": "vitaltrack",
    "name": "VitalTrack",
    "tagline": "PWA Mobile-First de suivi poids, nutrition photo IA & objets connectés",
    "description": "Application web PWA de suivi quotidien du poids (moyenne glissante 7j), bilans énergétiques BMR/TDEE, estimation calorique et macronutritionnelle par photo d'assiette (Gemini Vision + OpenFoodFacts), profil persistant et synchronisation bague RingConn Gen 3, Google Health Connect, Oura et balances Withings.",
    "category": "Santé & Nutrition",
    "icon": "activity",
    "color": "emerald",
    "vercel_url": "https://vital-track-one.vercel.app",
    "github_url": "https://github.com/TheBigBad31/VitalTrack",
    "is_private": True,
    "language": "Python",
    "stack": [
      "FastAPI",
      "Python 3.11",
      "Google Sign-In SSO",
      "Gemini Vision",
      "OpenFoodFacts API",
      "Chart.js",
      "Tailwind CSS",
      "RingConn Gen 3",
      "Google Health Connect",
      "Withings API",
      "Oura API"
    ],
    "features": [
      "Authentification unifiée Google Sign-In & SSO depuis AppHub",
      "Tableaux de bord biométriques avancés (hypnogramme RingConn, FC 24h, tendances HRV & passerelle Health Connect)",
      "Suivi quotidien du poids (moyenne glissante 7j) & bilans énergétiques BMR/TDEE",
      "Estimateur de calories & macros par photo d'assiette (Gemini Vision + OpenFoodFacts)",
      "Profil complet persistant (sauvegarde/restauration JSON 1-clic + auto-sync navigateur)",
      "Assistant de connexion & webhooks pour bague RingConn Gen 3, Google Health Connect, Oura Ring et balances Withings",
      "Architecture PWA responsive Mobile-First déployée sur Vercel Serverless avec fallback de données garanti"
    ],
    "latest_summary": "Visualisations biométriques avancées, hypnogramme RingConn, passerelle Android Health Connect et résilience Vercel Serverless (BALI-72, 73, 74).",
    "last_updated": "2026-10-25T19:14:21+01:00",
    "commits": [
      {
        "sha": "2383aed",
        "full_sha": "2383aedfe837306b446d01992ebedbb466e56a79",
        "message": "fix(crypto): fallback securise de cle de chiffrement pour initialisation Vercel Serverless (BALI-74)",
        "author": "TheBigBad31",
        "date": "2026-10-25T19:14:21+01:00",
        "url": "https://github.com/TheBigBad31/VitalTrack/commit/2383aedfe837306b446d01992ebedbb466e56a79"
      },
      {
        "sha": "91cff7a",
        "full_sha": "91cff7aa636567314ead15d60b25239c7c9f20a8",
        "message": "fix(deps): ajouter httpx aux dependances de production pour Vercel Serverless (BALI-74)",
        "author": "TheBigBad31",
        "date": "2026-10-25T18:51:22+01:00",
        "url": "https://github.com/TheBigBad31/VitalTrack/commit/91cff7aa636567314ead15d60b25239c7c9f20a8"
      },
      {
        "sha": "5403e8a",
        "full_sha": "5403e8a59e35dbe5db2cc4a8a4f99727e448d182",
        "message": "Merge remote-tracking branch 'origin/agent/ing-nieur-iot-sant-apps-biom-t/27df5a548ee2' into agent/mike/d3e80a4a6316",
        "author": "TheBigBad31",
        "date": "2026-10-25T18:35:26+01:00",
        "url": "https://github.com/TheBigBad31/VitalTrack/commit/5403e8a59e35dbe5db2cc4a8a4f99727e448d182"
      },
      {
        "sha": "6ed3b1d",
        "full_sha": "6ed3b1de6ddedc68404ad613c89ab9be46f3532f",
        "message": "feat(ui): visualisations biometriques avancees, anneaux d'objectifs, hypnogramme RingConn, FC 24h, tendances HRV et correlations (BALI-73)",
        "author": "TheBigBad31",
        "date": "2026-10-25T18:09:26+01:00",
        "url": "https://github.com/TheBigBad31/VitalTrack/commit/6ed3b1de6ddedc68404ad613c89ab9be46f3532f"
      },
      {
        "sha": "d2d88bb",
        "full_sha": "d2d88bb8c9b5fd8a3ef92c091c8f414cdf009392",
        "message": "Merge remote-tracking branch 'origin/agent/chef-de-projet-vitaltrack/e1abbed639f1' into agent/designer-ux-ui-web-desktop/35914e677c01",
        "author": "TheBigBad31",
        "date": "2026-10-25T17:49:02+01:00",
        "url": "https://github.com/TheBigBad31/VitalTrack/commit/d2d88bb8c9b5fd8a3ef92c091c8f414cdf009392"
      },
      {
        "sha": "ede9fec",
        "full_sha": "ede9fec656e74002192a384911839012345591f5",
        "message": "feat(iot): passerelle Android gratuite Health Connect vers webhook securise VitalTrack (RingConn & Xiaomi)",
        "author": "TheBigBad31",
        "date": "2026-10-25T17:11:24+01:00",
        "url": "https://github.com/TheBigBad31/VitalTrack/commit/ede9fec656e74002192a384911839012345591f5"
      }
    ]
  },
  {
    "id": "epicycleslab",
    "name": "EpicyclesLab",
    "tagline": "Atelier interactif d'épicycles & séries de Fourier (60 fps PWA)",
    "description": "Application web interactive PWA Mobile-First inspirée des cercles tournants de Fourier complexes (Transcendental Space / 3Blue1Brown). Manipulation d'épicycles à 60 fps, synthèse directe en mode Atelier et analyse inverse de contours (DFT/FFT) en Web Worker.",
    "category": "Maths & Animation",
    "icon": "disc",
    "color": "cyan",
    "vercel_url": "https://epicycles-lab.vercel.app",
    "github_url": "https://github.com/TheBigBad31/EpicyclesLab",
    "is_private": True,
    "language": "TypeScript",
    "stack": [
      "TypeScript",
      "Vite",
      "HTML5 Canvas",
      "Web Workers",
      "Fourier DFT/FFT",
      "Vitest",
      "PWA"
    ],
    "features": [
      "Mode Atelier de cercles : réglage dynamique des rayons, fréquences, phases et sens de rotation",
      "Mode Dessin Inverse par DFT/FFT : décomposition automatique en Web Worker dédié",
      "Modèle π de référence, formes géométriques et import de contour SVG vectoriel",
      "Rendu fluide 60 fps sur Canvas 2D avec caméra orbitale, zoom/pan et suivi de pointe",
      "Export haute définition PNG/SVG/JSON & partage direct de configurations par lien URL",
      "3 thèmes visuels soignés (Cosmos Neon, Blueprint Mathématique, Papier & Encre) et raccourcis studio"
    ],
    "latest_summary": "Stage 5 : Mise en place du pipeline CI/CD GitHub Actions, déploiement Vercel Serverless et référencement officiel dans AppHub.",
    "last_updated": "2026-10-24T11:35:13Z",
    "commits": [
      {
        "sha": "3602582",
        "full_sha": "3602582fadf1554725d7f50e52da545d9c331e2d",
        "message": "BALI-51: Add README documentation and inverse drawing RMSE threshold tests",
        "author": "TheBigBad31",
        "date": "2026-10-24T11:35:13Z",
        "url": "https://github.com/TheBigBad31/EpicyclesLab/commit/3602582fadf1554725d7f50e52da545d9c331e2d"
      },
      {
        "sha": "014836f",
        "full_sha": "014836ff33b5b263aa2b133f5fe632185abd8424",
        "message": "ci(devops): pipeline GitHub Actions CI et configuration Vercel SPA/PWA",
        "author": "TheBigBad31",
        "date": "2026-10-24T11:21:12Z",
        "url": "https://github.com/TheBigBad31/EpicyclesLab/commit/014836ff33b5b263aa2b133f5fe632185abd8424"
      },
      {
        "sha": "6e93a18",
        "full_sha": "6e93a1814f6c0852d074698ffb72131e4e294e80",
        "message": "feat(ui): stage 4 - thèmes configurables, ergonomie mobile-first, desktop studio & PWA",
        "author": "TheBigBad31",
        "date": "2026-10-24T11:11:55Z",
        "url": "https://github.com/TheBigBad31/EpicyclesLab/commit/6e93a1814f6c0852d074698ffb72131e4e294e80"
      },
      {
        "sha": "36ab865",
        "full_sha": "36ab865882fc7da1ff24e7fdcea7ae0acb43ff93",
        "message": "feat(inverse, worker, share): mode dessin inverse, worker FFT, indicateurs RMSE et export/partage URL",
        "author": "TheBigBad31",
        "date": "2026-10-24T11:02:35Z",
        "url": "https://github.com/TheBigBad31/EpicyclesLab/commit/36ab865882fc7da1ff24e7fdcea7ae0acb43ff93"
      },
      {
        "sha": "02a1d83",
        "full_sha": "02a1d831549abf8e706f0bee6f81b84f35672911",
        "message": "feat(render, workshop): moteur de rendu 60 fps, caméra interactive zoom/suivi, mode atelier et exports PNG/SVG",
        "author": "TheBigBad31",
        "date": "2026-10-24T10:52:51Z",
        "url": "https://github.com/TheBigBad31/EpicyclesLab/commit/02a1d831549abf8e706f0bee6f81b84f35672911"
      },
      {
        "sha": "9faeb08",
        "full_sha": "9faeb08165a79cabaa12757dcffa8493e9467756",
        "message": "feat(math): socle TypeScript/Vite/Vitest et moteur mathématique pur (DFT/FFT, rééchantillonnage, Gibbs, presets)",
        "author": "TheBigBad31",
        "date": "2026-10-24T10:45:00Z",
        "url": "https://github.com/TheBigBad31/EpicyclesLab/commit/9faeb08165a79cabaa12757dcffa8493e9467756"
      }
    ]
  }
]
