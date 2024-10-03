from dash import dcc, html
import plotly.express as px
from visualizer.components.header import create_header
from visualizer.components.footer import create_footer
from visualizer.components.navbar import create_navbar

def simple_page2(app, data_frame):
    """
    Crée la mise en page de la page 2 avec un histogramme.
    """
    # Crée un histogramme à partir des données nettoyées
    fig = px.histogram(data_frame, x='pk_debut', nbins=30,  # Choisissez la colonne appropriée pour l'histogramme
                       title='Histogramme des Positions de Début (pk_debut)',
                       labels={'pk_debut': 'Position de Début (pk_debut)'})

    layout = html.Div([
        create_header(),
        create_navbar(),
        html.H1("Page 2 - Histogramme des Positions de Début"),
        dcc.Graph(
            id='histogram-page-2',
            figure=fig  # Le graphique de l'histogramme
        ),
        create_footer(app)
    ])

    return layout
