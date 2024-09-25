from Extract import Extract
import json

# initialisize the app
if __name__ == "__main__":
    # here we have the url of our json file :
    url = 'https://www.data.gouv.fr/fr/datasets/r/15ebb66f-a235-45a3-8ad7-639d0e5cc21d'
    #extraction of the data using the Extract class
    extractor = Extract(url)
    data = extractor.get_data()

    # Example of viewing the extracted data
    print(json.dumps(data, indent=2))