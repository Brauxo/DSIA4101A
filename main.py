from Cleaning import Cleaning
import json

# initialisize the app
if __name__ == "__main__":
    # here we have the url of our json file :
    url = 'https://www.data.gouv.fr/fr/datasets/r/15ebb66f-a235-45a3-8ad7-639d0e5cc21d'

    #extraction and CLeaning of the data : 
    data = Cleaning(url)

    data.load_data() #Load the data
    data.clean_data() #clean the data using the Extract class

    cleaned_data = data.filtered_data()

    print(cleaned_data.head())  


