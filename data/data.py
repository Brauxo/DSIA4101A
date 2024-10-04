from data.cleaning import cleaning

# Fonction qui traite les données à partir de l'url
def data_process(url):

    # # Extraction, nettoyage des données et creation d'un dataframe ordonné.
    data = cleaning(url)
    data.load_data()  
    data.clean_data()  
    cleaned_data = data.filtered_data() 

    #renvoie les données sous forme de dataframe
    return cleaned_data
