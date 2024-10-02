from Cleaning import Cleaning
import json

# initialisize the app
if __name__ == "__main__":
    # here we have the url of our json file :
    url = 'https://www.data.gouv.fr/fr/datasets/r/c582bbe8-2d56-4273-a9f2-096b7377317b'

    #extraction and CLeaning of the data : 
    data = Cleaning(url)

    data.load_data() #Load the data
    data.clean_data() #clean the data using the Extract class

    cleaned_data = data.filtered_data()

    print(cleaned_data)  
    


