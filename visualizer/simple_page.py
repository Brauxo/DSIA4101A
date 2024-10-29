from dash import dcc, html
import folium
import dash
from visualizer.components.header import create_header
from visualizer.components.footer import create_footer
from visualizer.components.navbar import create_navbar

# Classe pour créer la carte
class Affichage:
    def __init__(self, cleaned_data):
        self.cleaned_data = cleaned_data

    def create_map(self, filter_option="both"):
        map_center = [46.603354, 1.888334]
        map_object = folium.Map(location=map_center, zoom_start=5, tiles='cartodb positron')
        line_count = 3347

        for index, row in self.cleaned_data.head(line_count).iterrows():
            coordinates = row['coordinates']

            if coordinates and len(coordinates) > 0:
                filtered_coordinates = []
                for coord in coordinates:
                    if isinstance(coord, (list, tuple)) and len(coord) == 2:
                        lon, lat = coord
                        filtered_coordinates.append((lat, lon))

                if len(filtered_coordinates) >= 2:
                    if 'vitesses' in row and len(row['vitesses']) > 0:
                        vitesses_detail = [v['detail'] for v in row['vitesses'] if 'detail' in v]
                        max_vitesse = max(vitesses_detail) if vitesses_detail else 0
                    else:
                        max_vitesse = 0

                    if 'code_ligne' in row:
                        code_ligne = row['code_ligne']
                    else:
                        code_ligne = 0

                    color = "green" if max_vitesse >= 250 else "royalblue"
                    if filter_option == "LGV" and max_vitesse < 250:
                        continue
                    if filter_option == "classique" and max_vitesse >= 250:
                        continue
                    if filter_option == "LGVC" and max_vitesse < 250 and code_ligne not in [14000, 5000]:
                        continue
                    if filter_option == "LGVC":
                        color = "green"

                    folium.PolyLine(locations=filtered_coordinates, color=color, weight=1, opacity=1).add_to(map_object)

        return map_object._repr_html_()


# Fonction pour créer la page
def simple_page(app, data_frame):
    affichage = Affichage(data_frame)

    # Création des cartes pour chaque option
    map_both_html = affichage.create_map(filter_option='both')
    map_lgv_html = affichage.create_map(filter_option='LGV')
    map_classique_html = affichage.create_map(filter_option='classique')
    map_lgvc_html = affichage.create_map(filter_option='LGVC')

    # Layout de la page avec les cartes en grille
    layout = html.Div(className="page-content-wrapper", children=[
        create_header(),
        create_navbar(),
        html.H1("Gapminder Dashboard - Cartes", className="header-title"),
        html.Div(className="map-grid", children=[
            html.Div(className="map-item", children=[
                html.H2("Toutes les lignes", className="map-title"),
                html.Iframe(srcDoc=map_both_html, className="map-iframe"),
            ]),
            html.Div(className="map-item", children=[
                html.H2("Lignes classiques", className="map-title"),
                html.Iframe(srcDoc=map_classique_html, className="map-iframe"),
            ]),
            html.Div(className="map-item", children=[
                html.H2("LGV", className="map-title"),
                html.Iframe(srcDoc=map_lgv_html, className="map-iframe"),
            ]),
            html.Div(className="map-item", children=[
                html.H2("LGV complété", className="map-title"),
                html.Iframe(srcDoc=map_lgvc_html, className="map-iframe"),
            ]),
        ]),
        create_footer(app)
    ])

    return layout
