# DSIA4101A

**Projet de cours - Filière Data Science :**  
Ce projet, réalisé en binôme, porte sur l'analyse des voies ferroviaires en France.

# Jeu de données 

Pour la réalisation de ce projet, nous avons utilisé différentes données issues de la SNCF, soigneusement triées par Mathias Maestri, que nous tenons à remercier chaleureusement. Ces données ont ensuite été exportées dans un fichier au format .geojson.

[Jeu de données utilisé : Données réseau ferroviaire national concaténées](https://www.data.gouv.fr/fr/datasets/donnees-reseau-ferroviaire-national-concatenees/)

[données SNCF](https://data.sncf.com/pages/accueil/)

# Sommaire

## Guide de l'application
1. [Prérequis d'installation](#1---Prérequis-dinstallation)
2. [Lancer l'application](#2---Lancer-lapplication)
3. [Présentation du Dashboard](#3---Présentation-du-dashboard)

## Analyse des données
1. [Contexte](#1---Contexte)
2. [Analyse des voies ferroviaires françaises](#2---Analyse-des-voies-ferroviaires-françaises)

## Guide du developpeur
1. [Contexte](#1---Contexte)
2. [Arborescence des fichiers](#2---Arborescence-des-fichiers)
---

# Guide de l'application

## 1 - Prérequis d'installation

Cette section décrit les étapes nécessaires à l'installation des outils et dépendances pour exécuter l'application.

### Installation de Python 3

Tout d'abord, il est nécessaire d'installer une version récente de Python 3 (la version 3.12.0 est recommandée pour ce projet). Vous pouvez télécharger Python à partir du lien suivant :  
[Installation de Python](https://www.python.org/downloads/)

### Installation des packages requis

Les dépendances du projet sont listées dans le fichier `requirements.txt`. Pour installer ces packages, ouvrez un terminal et exécutez la commande suivante :  
```
pip install -r requirements.txt
```

### Installation de Git

Pour cloner le dépôt Git de ce projet, assurez-vous que Git est installé sur votre machine. Si ce n'est pas le cas, vous pouvez l'installer à partir de ce lien :  
[Installation de Git](https://git-scm.com/)

### Cloner le dépôt Git

Une fois Git installé, ouvrez `Git Bash` ou tout autre terminal et exécutez la commande suivante pour cloner le projet dans le répertoire de votre choix :  
```
   *git clone https://github.com/Brauxo/DSIA4101A*
```

## 2 - Lancer l'application

Après avoir suivi les étapes d'installation, vous pouvez démarrer l'application en exécutant le fichier `main.py`. Pour ce faire, ouvrez un terminal et exécutez la commande suivante :
```
*python main.py*
```

Si tout se passe comme prévu, arpès quelques instants vous allez obtenir : 

```
Dash is running on http://127.0.0.1:8050/

 * Serving Flask app 'visualizer.dashboardholder'
 * Debug mode: on
```

Cela signifie que l'application est en cours d'exécution en local (localhost) à l'adresse suivante :  
[http://127.0.0.1:8050/](http://127.0.0.1:8050/)

Copiez-collez cette adresse dans un navigateur web pour accéder à l'application.

## 3 - Présentation du Dashboard

*(Section à compléter)*

Cette section présentera le fonctionnement du Dashboard une fois lancé, ainsi que ses différentes fonctionnalités.

### Navigation dans le Dashboard


### Page d'accueil 



### Page de la carte 



### Page des graphiques 



### Page d'information sur nous et ce projet





---

# Analyse des données

## 1 - Contexte

*(Section à compléter)*

Cette section fournira un aperçu général du projet, de ses objectifs ainsi que du contexte de l'analyse sur les voies ferroviaires en France.

## 2 - Analyse des voies ferroviaires françaises

*(Section à compléter)*

Cette section détaillera l'analyse des données ferroviaires françaises, y compris les statistiques clés et les insights obtenus à partir des données.

---
# Guide du développeur

## 1 - Contexte

Ce guide développeur présente les objectifs, l'architecture, et la structure de notre projet. Il est conçu pour faciliter l’ajout de nouvelles fonctionnalités et assurer la maintenabilité du code.

Pour garantir la compréhension du code par le plus grand nombre, nous avons choisi de coder en anglais et de respecter les conventions **PEP-8** pour assurer une lisibilité et une cohérence optimales.

Ce guide ne s'attarde pas sur une compréhension exhaustive des codes. Nous expliquons nos choix de conception, les raisons de ces choix, ainsi que la structure logique qui encadre le projet.

## 2 - Architecture du code

Nous avons structuré le projet en plusieurs fichiers Python et répertoires afin de compartimenter chaque tâche pour plus de clarté et de modularité.

- **main.py** : Point d’entrée du projet, coordonne les différentes étapes de traitement.

### Les dossiers

- **data** : contient les scripts de gestion des données.
  - `extract.py` : Récupération et extraction des données initiales.
  - `cleaning.py` : Nettoyage et préparation des données pour analyse.
  - `data.py` : Utilitaires supplémentaires pour la gestion de données.

- **visualizer** : modules responsables de la création du tableau de bord et de la visualisation.
  - `dashboardholder.py` : Gère l’interface du tableau de bord principal.
  - `simple_page*.py` : Différentes pages de visualisation (accueil, pages spécifiques).
  - `components` : Sous-dossier pour les composants UI (ex. : en-tête, navigation, pied de page).
  - `assets` : Regroupe les fichiers visuels et CSS (images, icônes, style CSS pour le design du tableau de bord).

Voici un aperçu visuel de l'arborescence du projet :
*(mettre a jour une fois projet finis)*
<div align="center">
    <img src="https://github.com/user-attachments/assets/3da9ee46-32cf-49c7-a5f6-a69309bf7b91" alt="Aperçu de l'arborescence du projet" width="65%"/>
</div>

Représentation alternative de l'architecture du projet :
*(mettre a jour si besoin j ai le code)*
<div align="center">
    <img src="https://github.com/user-attachments/assets/f358ed75-c1b4-4119-944f-ad8372eb3356" alt="Représentation alternative de l'architecture" width="100%"/>
</div>

## 3 - Ajouter une Page
1. **Créer un Fichier pour la Page** : Créez un nouveau fichier dans le dossier `visualizer` pour définir votre page, par exemple `simple_page_new.py`.
2. **Définir la Structure de la Page** : Dans le fichier crée, créez une fonction pour définir la structure de la page. ![image](https://github.com/user-attachments/assets/a3d4d854-c3ec-448a-9c95-31a2c3bcb9fe)

3. **Ajouter la Page au Tableau de Bord** : Ouvrez dashboardholder.py et a ajouter simple_page_new.*(mettre capture de la ou il faut ajouter)*


## 4 - Suggestions d'améliorations futures

- Compléter les sections incomplètes (présentation du dashboard, contexte, analyse).
- Ajouter une description détaillée de l'interface du dashboard.
- Inclure des captures d'écran du dashboard dans la section correspondante.
- Décrire l'arborescence des fichiers de manière plus détaillée.
