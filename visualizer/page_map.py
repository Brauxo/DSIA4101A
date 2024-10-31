from dash import dcc, html
import folium
import dash
from visualizer.components.header import create_header
from visualizer.components.footer import create_footer
from visualizer.components.navbar import create_navbar


# Class for creating the map visualization
class Affichage:
    """
    A class to create a map with specific visualizations based on provided data.

    Args:
        cleaned_data (pd.DataFrame): A DataFrame containing cleaned data with
        coordinates and line information.
    """

    def __init__(self, cleaned_data):
        """
        Initialize the Affichage class with the cleaned data.

        Args:
            cleaned_data (pd.DataFrame): Data for generating map lines with various attributes.
        """
        self.cleaned_data = cleaned_data

    def create_map(self, filter_option="both"):
        """
        Generate a Folium map based on the filtered option.

        Args:
            filter_option (str): Filter option to display specific lines ('both', 'LGV', 'classique', 'LGVC').

        Returns:
            str: An HTML representation of the generated map.
        """
        map_center = [46.603354, 1.888334]  # Center of France
        map_object = folium.Map(location=map_center, zoom_start=5, tiles='cartodb positron')
        line_count = 3347  # Limit of lines to be displayed for performance

        for index, row in self.cleaned_data.head(line_count).iterrows():
            coordinates = row['coordinates']

            if coordinates and len(coordinates) > 0:
                filtered_coordinates = []
                for coord in coordinates:
                    if isinstance(coord, (list, tuple)) and len(coord) == 2:
                        lon, lat = coord
                        filtered_coordinates.append((lat, lon))

                if len(filtered_coordinates) >= 2:
                    # Extract speed details if available
                    if 'vitesses' in row and len(row['vitesses']) > 0:
                        vitesses_detail = [v['detail'] for v in row['vitesses'] if 'detail' in v]
                        max_vitesse = max(vitesses_detail) if vitesses_detail else 0
                    else:
                        max_vitesse = 0

                    # Get line code and name if available
                    code_ligne = row.get('code_ligne', "Not specified")
                    nom_ligne = row.get('nom_ligne', "Name not specified")

                    # Set color based on speed
                    color = "green" if max_vitesse >= 250 else "royalblue"
                    if filter_option == "LGV" and max_vitesse < 250:
                        continue
                    if filter_option == "classique" and max_vitesse >= 250:
                        continue
                    if filter_option == "LGVC" and max_vitesse < 250 and code_ligne not in [14000, 5000]:
                        continue
                    if filter_option == "LGVC":
                        color = "green"

                    # Create popup with line code and name
                    popup_content = f"Line Code: {code_ligne}<br>Line Name: {nom_ligne}"
                    popup = folium.Popup(popup_content, max_width=300)

                    # Add the line to the map with the popup
                    folium.PolyLine(
                        locations=filtered_coordinates,
                        color=color,
                        weight=1,
                        opacity=1,
                        popup=popup
                    ).add_to(map_object)

        return map_object._repr_html_()


# Function to create the page layout with maps
def page_map(app, data_frame):
    """
    Generate the layout for the simple page with various map views.

    Args:
        app (Dash): The Dash application instance.
        data_frame (pd.DataFrame): The DataFrame containing map data.

    Returns:
        html.Div: A Dash HTML layout containing the map grids and components.
    """
    affichage = Affichage(data_frame)

    # Generate maps for each option
    map_both_html = affichage.create_map(filter_option='both')
    map_lgv_html = affichage.create_map(filter_option='LGV')
    map_classique_html = affichage.create_map(filter_option='classique')
    map_lgvc_html = affichage.create_map(filter_option='LGVC')

    # Page layout with maps in a grid structure
    layout = html.Div(className="page-content-wrapper", children=[
        create_header(),
        create_navbar(),
        html.H1("Gapminder Dashboard - Maps", className="header-title"),
        html.Div(className="map-grid", children=[
            html.Div(className="map-item", children=[
                html.H2("Toutes les lignes", className="map-title"),
                html.Iframe(srcDoc=map_both_html, className="map-iframe"),
            ]),
            html.Div(className="map-item", children=[
                html.H2("Lignes classique", className="map-title"),
                html.Iframe(srcDoc=map_classique_html, className="map-iframe"),
            ]),
            html.Div(className="map-item", children=[
                html.H2("Ligne a grande vitesse(LGV)", className="map-title"),
                html.Iframe(srcDoc=map_lgv_html, className="map-iframe"),
            ]),
            html.Div(className="map-item", children=[
                html.H2("Ligne a grande vitesse complété(LGVC)", className="map-title"),
                html.Iframe(srcDoc=map_lgvc_html, className="map-iframe"),
            ]),
        ]),
        create_footer(app)
    ])

    return layout
