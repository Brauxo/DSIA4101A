from visualizer.dashboardholder import dashboardholder
from data.data import data_process
import pandas as pd


if __name__ == '__main__':
    # Instancie le Dashboard avec les données nécessaires
    url = 'https://www.data.gouv.fr/fr/datasets/r/c582bbe8-2d56-4273-a9f2-096b7377317b'

    df= data_process(url)
    dashboard = dashboardholder(df)

    # Lancer le dashboard
    dashboard.run()
