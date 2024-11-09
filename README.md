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
2. [Architecture du code](#2---Architecture-du-code)
3. [Ajouter une page](#3---Ajouter-une-page)
4. [Suggestions d'améliorations futures](#4---Suggestions-daméliorations-futures)
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

Cette section présente le fonctionnement du Dashboard une fois lancé, ainsi que ses différentes fonctionnalités.

### Navigation dans le Dashboard
Pour naviguer dans le dashboard on utilise une navbar avec 4 boutons pour chaque page de l'application. 
<div align="center">
  <img src="https://github.com/Brauxo/DSIA4101A/blob/main/visualizer/assets/navbar_example.PNG"/>
</div>

### Page d'accueil 
La page d'accueil qui est la première page montré lors du lancement du dashboard, elle présente vaguement le contenu du dashboard.
<div align="center">
  <img src="https://github.com/Brauxo/DSIA4101A/blob/main/visualizer/assets/home_example.PNG"/>
</div>


### Page de la carte 
La page qui montre différentes cartes des chemins de fer français (LGV,Toutes,Lignes classiques), cette page utilise les callbacks pour mettre à jour en direct les cartes.
<div align="center">
  <img src="https://github.com/Brauxo/DSIA4101A/blob/main/visualizer/assets/map_example.PNG"/>
</div>

### Page des graphiques 
Cette page permet d'obtenir des informations sous formes de graphique sur les chemins de fer français.
<div align="center">
  <img src="https://github.com/Brauxo/DSIA4101A/blob/main/visualizer/assets/data_example.PNG"/>
</div>

### Page d'information sur nous et ce projet
Cette page contient les informations sur les outils utilisés et sur nous.
<div align="center">
  <img src="https://github.com/Brauxo/DSIA4101A/blob/main/visualizer/assets/aboutus_example.PNG"/>
</div>


---

# Analyse des données

## 1 - Contexte

L'objectif de ce projet est de fournir un aperçu général et en temps réel des statistiques sur les voies ferroviaires en France, ainsi qu'une représentation cartographique des rails français. Cette analyse permettra de visualiser les caractéristiques du réseau ferroviaire, d’identifier des tendances et les données du réseau. Ce projet s'inscrit dans le cadre de la validation de l'unité DSIA4101.

## 2 - Analyse des voies ferroviaires françaises

#### Analyse Lignes sur la carte :
<div align="center">
  <img src="https://github.com/user-attachments/assets/637632e5-2f2e-4f0c-b79e-0ed82112f44e"/>
</div>

La **première** **carte**  montre l'entièreté des lignes  générées à partir des données de la sncf, ces lignes sont variées et peuvent être actuellement hors-service.

La **deuxième** **carte**  montre les lignes  générées à partir des données qui ne sont pas des lignes à grandes vitesses (<= 250 km/h), ce sont les lignes dites classique.

La **troisème** **carte**  montre les lignes à grande vitesse (LGV) générées à partir des données. Le critère pour qu'une ligne soit considérée comme LGV est une vitesse maximale supérieure à 250 km/h. Cependant, après une vérification rapide, il apparaît que deux lignes LGV manquent sur cette carte.

La **quatrième** **carte** ajoute ces deux lignes manquantes, qui ont été incluses manuellement. L'absence de ces lignes dans la première carte s'explique par des données incomplètes : la vitesse n'est pas renseignée pour ces deux lignes dans les données.

Complément d'analyse : 

En observant les cartes, on remarque que la majorité des lignes LGV partent ou arrivent à Paris, ce qui souligne un certain phénomène **d'enclavement** du **territoire**. Cette concentration des infrastructures autour de Paris pourrait indiquer une centralisation des transports ferroviaires, reliant principalement la capitale aux autres grandes villes, mais créant moins de connexions directes entre les régions.

#### Analyse des graphiques :

Les graphiques sur les voies ferroviaires en France montrent une répartition intéressante des lignes, en fonction de leur vitesse, de leur électrification et de la taille des tronçons.

<div align="center">
  <img src="https://github.com/Brauxo/DSIA4101A/blob/main/visualizer/assets/histo_speed.png"/>
</div>

**Les** **vitesses** 

Pour les lignes à grande vitesse, on observe qu'elles sont bien représentées, avec 17 tronçons qui roulent à 270 et 300 km/h. On trouve aussi 4 tronçons à 320 km/h et un seul qui atteint 350 km/h. Cela montre que, même si la majorité des LGV roulent à des vitesses proches de 300 km/h, il existe quelques lignes qui vont encore plus vite atteignant une vitesse max de 350 km/h.
Pour lignes classiques, la situation est bien différente. La majorité des tronçons sont assez lents, avec 23,7% des lignes classiques circulant à seulement 30 km/h. celle-ci semblent être régionales en observant sur la carte et repésentent de plus petites distances.

<div align="center">
  <img src="https://github.com/Brauxo/DSIA4101A/blob/main/visualizer/assets/piechart_electric.png"/>
</div>

**L’électrification** **des** **lignes** 

En termes d’électrification, on remarque que 67,8% des lignes sont alimentées par un système de 25 000 volts, ce qui est principalement destiné aux LGV. 31,3% des tronçons utilisent un système de 1 500 volts, plus couramment utilisé pour les lignes classiques et régionales. Les autres systèmes d’alimentation, bien que présents, représentent une proportion très faible du réseau mais on peut noté des précisions comme des volts continu par 3 ème rail qui après une recherche sur internet représente les lignes avec un rail supplémentaire.

<div align="center">
  <img src="https://github.com/Brauxo/DSIA4101A/blob/main/visualizer/assets/histo_segment.png"/>
</div>

**La** **taille** **des** **segments** 

Enfin, en ce qui concerne la taille des tronçons, la plupart d'entre eux mesurent moins de 125 km (environ 98% d'entre eux), bien que certains tronçons soient plus longs, notamment le plus grand se situant entre 825 et 875 km. Cela montre que le réseau français est en grande majorité composé de lignes assez courtes, adaptées aux trajets régionaux, même si certaines lignes longues sont concentrées sur les grands axes à grande vitesse. Par ailleurs les troncons les plus grands correpondent aux LGV. 

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
  - `page_home.py` : La page d'accueil du dashboard.
  - `page_map.py` : Une page qui montre 4 carte différentes des chemins de fer français en fonction de certains critères.
  - `page_graph.py` : Une page où l'on peut retrouvé différents graphiques sur les données de la SNCF.
  - `page_aboutus.py` : Une page qui contient des informations sur les outils utilisés et les créateurs.
  - `components` : Sous-dossier pour les composants UI (ex. : en-tête, navigation, pied de page).
  - `assets` : Regroupe les fichiers visuels et CSS (images, icônes, style CSS pour le design du tableau de bord).

Voici un aperçu visuel de l'arborescence du projet : *(mettre à jour une fois le projet terminé)*

<div align="center">
    <img src="https://github.com/user-attachments/assets/3da9ee46-32cf-49c7-a5f6-a69309bf7b91" alt="Aperçu de l'arborescence du projet" width="65%"/>
</div>

Représentation alternative de l'architecture du projet : *(mettre à jour si besoin, code Mermaid disponible)*

<div align="center">
    <img src="https://github.com/user-attachments/assets/f358ed75-c1b4-4119-944f-ad8372eb3356" alt="Représentation alternative de l'architecture" width="100%"/>
</div>

### Principe de compartimentation

Il est essentiel de respecter le principe de **compartimentation** en développement, afin d'éviter un "code spaghetti" difficile à maintenir. Dans notre projet, chaque composant est isolé dans un module spécifique pour séparer les responsabilités et faciliter l'évolution du code.

Nous avons structuré le projet en trois grands modules :

- **data** : responsable de la gestion des données, depuis l'extraction initiale jusqu'au nettoyage.
- **visualizer** : dédié à la présentation des données sous forme de tableau de bord, avec des pages spécifiques et des composants UI (en-tête, navigation, etc.). Ce module utilise des classes et des fonctions dans chaque page pour organiser le code et les interactions de manière cohérente.
- **assets** : contient les ressources statiques comme les images et les fichiers CSS pour styliser le tableau de bord.

Cette organisation permet une grande flexibilité. Par exemple, si nous disposons déjà de données nettoyées, nous pouvons sauter la partie extraction sans impacter la partie visualisation. Chaque page dans `visualizer` est appelée depuis `dashboardholder.py` et utilise des classes ou des fonctions pour structurer les éléments de la page de manière claire et modulable. 

Enfin, le dossier **assets** inclut un fichier CSS pour minimiser la duplication de styles dans le code. Cette approche nous permet de modifier facilement l'apparence du tableau de bord sans avoir à toucher au code Python, en se concentrant simplement sur les styles dans le CSS.


## 3 - Ajouter une page
1. **Créer un Fichier pour la page** : Créez un nouveau fichier dans le dossier `visualizer` pour définir votre page, par exemple `simple_page_new.py`.
2. **Définir la Structure de la page** : Dans le fichier crée, créez une fonction pour définir la structure de la page.
<div align="center">
    <img src="https://github.com/user-attachments/assets/a3d4d854-c3ec-448a-9c95-31a2c3bcb9fe" alt="image"width="35%"/>
</div>

3. **Ajouter la page au Tableau de Bord** : Ouvrez dashboardholder.py et ajouter simple_page_new.
<div align="center">
    <img src="https://github.com/user-attachments/assets/7cce7a37-90ff-4b4a-b29a-58152bdf932d" alt="image"width="50%"/>
</div>

## 4 - Suggestions d'améliorations futures

- Compléter les sections incomplètes (présentation du dashboard, contexte, analyse).
- Ajouter une description détaillée de l'interface du dashboard.
- Inclure des captures d'écran du dashboard dans la section correspondante.
- Décrire l'arborescence des fichiers de manière plus détaillée.
