import pandas as pd
from Extract import Extract


#The following python file will be used to clean the data that we previously extracted.   

class Cleaning:
    def __init__(self, url):
        self.url = url
        self.data = None
        self.cleaned_data = None

    # Load the data using the Extract class
    def load_data(self):
        extractor = Extract(self.url)
        self.data = extractor.get_data()

    def clean_data(self):

        data_list = []

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

        self.cleaned_data = pd.DataFrame(data_list)
        
        return self.cleaned_data

    def filtered_data(self):
        organized_data = self.cleaned_data.sort_values(by='code_ligne')
        
        return organized_data
    