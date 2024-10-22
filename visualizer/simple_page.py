from dash import dcc, html, Input, Output
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
        map_object = folium.Map(location=map_center, zoom_start=6, tiles='cartodb positron')
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


# Fonction pour créer la page et gérer les callbacks
def simple_page(app, data_frame):
    affichage = Affichage(data_frame)
    map_html = affichage.create_map(filter_option='both')

    @app.callback(
        Output('map', 'srcDoc'),
        Input('lgv-dropdown', 'value'),
    )
    def update_map(selected_option):
        map_html = affichage.create_map(filter_option=selected_option)
        return map_html

    # Layout de la page
    layout = html.Div(style={'height': '100vh', 'width': '100vw'}, children=[
            create_header(),
            create_navbar(),
            html.H1("Gapminder Dashboard - Carte"),
            dcc.Dropdown(
                id='lgv-dropdown',
                options=[
                    {'label': 'Toutes les lignes', 'value': 'both'},
                    {'label': 'LGV', 'value': 'LGV'},
                    {'label': 'Lignes classiques', 'value': 'classique'},
                    {'label': 'LGV complété', 'value': 'LGVC'}
                ],
                value='both',
                clearable=False,
                style={'width': '50%', 'margin': 'auto'}
            ),
            html.Iframe(id='map', srcDoc=map_html, width='100%', height='800px', className='map-iframe'),
            create_footer(app)
        ]
    )

    return layout