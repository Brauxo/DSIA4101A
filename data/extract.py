import requests

# The following python file will be used to extract the data from a JSON file.

class extract:
    # Initialize the class
    def __init__(self, url):
        self.url = url

    # Function that fetches the data from the URL
    def get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            raise Exception(f"Failed to fetch data: {response.status_code}")
