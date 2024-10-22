import pandas as pd
from data.extract import extract  # Adjusted for the new structure
from statistics import mean


# La classe Cleaning a comme objectif de contruire un dataframe "propre" des données qui nous interéssent à partir du fichier brut json

class cleaning:
    def __init__(self, url):
        self.url = url
        self.data = None
        self.cleaned_data = None

    # Ici on charge la data en utilisant la classe Extract 
    def load_data(self):
        extractor = extract(self.url)
        self.data = extractor.get_data()

    def clean_data(self):
        data_list = []

        #extrait toutes les lignes des collonnes qui sont utiles pour la suite
        for feature in self.data:
            code_ligne = feature.get('codeLigne', None)
            nom_ligne = feature.get('nomLigne', None)
            pk_debut = feature.get('pkDebut', None)
            pk_fin = feature.get('pkFin', None)
            statut = feature.get('statut', None)
            troncon = feature.get('troncon', None)
            cantonnements = feature.get('cantonnements', None)
            electrifications = feature.get('electrifications', None)
            type_ligne = feature.get('typeLigne', None)
            vitesses = feature.get('vitesses', None)
            geometry = feature.get('geometry', None)
            coordinates = geometry.get('coordinates', None) if geometry else None


            #ajoute dans le dictionnaire data_list ce qui a été extrait
            data_list.append({
                'code_ligne': code_ligne,
                'nom_ligne': nom_ligne,
                'pk_debut': pk_debut,
                'pk_fin': pk_fin,
                'statut': statut,
                'troncon': troncon,
                'coordinates': coordinates,
                'cantonnements': cantonnements,
                'electrifications': electrifications,
                'type_ligne': type_ligne,
                'vitesses': vitesses
            })

        #création du dataframe
        self.cleaned_data = pd.DataFrame(data_list)

        #renvoie le dataframe
        return self.cleaned_data

    #Organise les données en utilisant un sort
    def filtered_data(self):
        organized_data = self.cleaned_data.sort_values(by='code_ligne')

        #renvoie le datagrame organisé
        return organized_data
