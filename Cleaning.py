import pandas as pd
from Extract import Extract


#The following python file will be used to clean the data that we previously extracted.   

class Cleaning :
    def __init__(self, url):
        self.url = url
        self.data = None
        self.cleaned_data = None

    # Use the Extract class to get the data from the url
    def load_data(self):
        extractor = Extract(self.url)
        self.data = extractor.get_data()
    
    # Clean and organize the data
    def clean_data(self):
        features = self.data['features']
        data_list = []

        for feature in features:
            properties = feature['properties']

            # Append the data to list
            data_list.append({
                'date': properties['date_ech'],
                'no2': properties.get('val_no2', None),
                'pm10': properties.get('val_pm10', None),
                'o3': properties.get('val_o3', None),
                'pm25': properties.get('val_pm25', None),
                'qualif': properties['qualif'],
                'x_coordinates': properties.get('x_lamb93', None),
                'y_coordinates': properties.get('y_lamb93', None)
            })

        # Here we convert the data to a pandas DataFrame 
        self.cleaned_data = pd.DataFrame(data_list)

    # here is a function to visualize the data (grouping/filtering)
    def filtered_data(self):
        numeric_columns = self.cleaned_data.select_dtypes(include='number')
        organized_data = numeric_columns.groupby(self.cleaned_data['date']).mean().reset_index()
        return organized_data
