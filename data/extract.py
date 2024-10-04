import requests

# cette classe est utilisée pour extraire les données d'un fichier JSON.

class extract:
    # Initialisation de la classe
    def __init__(self, url):
        self.url = url

    # Fonction qui récupère les données depuis l'URL
    def get_data(self):
        response = requests.get(self.url)
        #si les données sont bien reçues, renvoie le json
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            #en cas d'aucune réponse 
            raise Exception(f"Failed to fetch data: {response.status_code}")
