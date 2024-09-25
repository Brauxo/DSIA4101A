import requests

#The following python file will be used to extract the data from a json file.   

class Extract:
    #here we initialize the class 
    def __init__(self, url):
        self.url = url

    #here is the function that take the data from the url 
    def get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data
        #In case have no response :
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")

