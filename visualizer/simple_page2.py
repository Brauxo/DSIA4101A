from dash import dcc, html
import pandas as pd
import plotly.express as px
from visualizer.components.header import create_header
from visualizer.components.footer import create_footer
from visualizer.components.navbar import create_navbar

def simple_page2(app, data_frame):
    """
    Créer la mise en page de la page 2 avec plusieurs visualisations.
    """
    # Ignorer les lignes avec des valeurs manquantes
    data_frame = data_frame.dropna(subset=['pk_debut', 'pk_fin', 'vitesses']).copy()  # Création d'une copie

    # Créer un histogramme à partir des données nettoyées
    fig_histogram = px.histogram(data_frame, x='pk_debut', nbins=30,  
                                  title='Histogramme des Positions de Début (pk_debut)',
                                  labels={'pk_debut': 'Position de Début (pk_debut)'})
    


    # Disposition des graphiques sur la même page
    layout =  html.Div(style={'height': '100vh', 'width': '100vw'}, children=[
        create_header(),
        create_navbar(),
        html.H1("Page 2 - Analyses et Visualisations des Données de la Ligne"),

        # Graphique 1 : Histogramme des Positions de Début
        html.Div(style={'padding': '20px', 'height': '85vh', 'width': '100%'}, children=[  # Responsive container for the graph
            html.H2("Histogramme des Positions de Début"),
            dcc.Graph(
                id='histogram-page-2',
                figure=fig_histogram,
                style={'height': '100%', 'width': '100%'}  # Make the graph fill the container
            )
        ]),
        
        create_footer(app)
    ])

    return layout
