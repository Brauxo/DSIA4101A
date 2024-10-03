# DSIA4101A-Air-quality-in-France
Projet de Data Science sur la qualité de l'air de différentes communes en France. 
/project_root
├── main.py                          # Fichier principal pour lancer l'application
├── /assets
├── /visualizer
│   ├── dashboardholder.py           # Fichier principal pour gérer le dashboard
│   ├── simple_page.py               # Page contenant la carte
│   ├── simple_page2.py              # Page contenant l'histogramme
│   └── /components                  # Dossier pour les composants réutilisables
│       ├── header.py                # Composant d'en-tête
│       ├── footer.py                # Composant de pied de page
│       └── navbar.py                # Composant de barre de navigation
│   └── /assets
│       ├── bar_chart.png            # Icône pour la page histogramme
│       ├── map.png                  # Icône pour la page carte
│       └── logo.png                 # Logo ESIEE Paris
└── /data                            # Dossier pour le traitement des données
    ├── data.py                      # Fichier pour gérer l'extraction et le nettoyage des données
    ├── cleaning.py                  # Fichier pour nettoyer les données
    └── extract.py                   # Fichier pour extraire les données depuis l'URL

