from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import folium
import base64
from io import BytesIO
from visualizer.components.header import create_header
from visualizer.components.footer import create_footer
from visualizer.components.navbar import create_navbar

class Affichage:
    def __init__(self, cleaned_data):
        self.cleaned_data = cleaned_data

    def create_map(self):
        map_center = [46.603354, 1.888334]  # Coordonnées approximatives du centre de la France
        map_object = folium.Map(location=map_center, zoom_start=6, tiles='cartodb positron')


        # nombre de lignes sélectionnées (3347 le max)
        line_count = 1650


        for index, row in self.cleaned_data.head(line_count).iterrows():
            coordinates = row['coordinates']  # Liste de coordonnées pour cette ligne

            if coordinates and len(coordinates) > 0:
                filtered_coordinates = [(lat, lon) for lon, lat in coordinates]

                if len(filtered_coordinates) >= 2:
                    folium.PolyLine(locations=filtered_coordinates, color="blue", weight=5, opacity=1).add_to(map_object)

                    #folium.Marker(
                        #location=filtered_coordinates[0],
                        #popup=f"Code ligne: {row['code_ligne']}, Statut: {row['statut']}"
                    #).add_to(map_object)

        return map_object

def simple_page(app, data_frame):
    """ Créer la mise en page de la page 1 avec le dropdown et le graphe interactif """
    affichage = Affichage(data_frame)  # Crée une instance de la classe Affichage
    folium_map = affichage.create_map()  # Crée la carte

    # Sauvegarder la carte dans un fichier HTML
    map_file = 'map.html'
    folium_map.save(map_file)

    # Lire le fichier HTML et l'encoder pour l'affichage
    with open(map_file, 'r', encoding='utf-8') as f:
        map_html = f.read()

    layout = html.Div([
        create_header(),
        create_navbar(),
        html.H1("Gapminder Dashboard - Carte"),
        html.Iframe(srcDoc=map_html, width='100%', height='600px',className='map-iframe'),  # Afficher la carte dans un iframe
        create_footer(app)
    ])

    return layout
