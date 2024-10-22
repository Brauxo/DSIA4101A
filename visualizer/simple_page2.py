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

    #  Extraction des vitesses par tronçon
    # "Exploser" la colonne 'vitesses' pour obtenir chaque tronçon de vitesse sur une ligne
    vitesses_df = pd.DataFrame(data_frame.explode('vitesses')['vitesses'].apply(pd.Series))
    vitesses_df['pk_debut'] = vitesses_df['from']  # Utilisation de 'from' pour représenter le pk_debut

    # Histogramme sur la réparition  des vitesses
    fig_histogram_vitesses = px.histogram(vitesses_df, x='detail', nbins=30,  
                                          title='Histogramme des Vitesses par Tronçon',
                                          labels={'detail': 'Vitesse (km/h)'})
    

    # Camembert sur la réparition  des vitesses
    fig_pie_vitesses = px.pie(vitesses_df, names='detail', title='Répartition des Vitesses')

    # Créer un histogramme des positions de debut
    fig_histogram = px.histogram(data_frame, x='pk_debut', nbins=30,  
                                  title='Histogramme des Positions de Début (pk_debut)',
                                  labels={'pk_debut': 'Position de Début (pk_debut)'})
                                  




    # Disposition des graphiques sur la même page
    layout =  html.Div(style={'height': '100vh', 'width': '100vw'}, children=[
        create_header(),
        create_navbar(),
        html.H1("Page 2 - Analyses et Visualisations des Données de la Ligne"),

        # Histogramme des Vitesses
        html.Div(style={'padding': '20px', 'height': '85vh', 'width': '100%'}, children=[
            html.H2("Histogramme des Vitesses par Tronçon"),
            dcc.Graph(
                id='histogram-vitesses-page-2',
                figure=fig_histogram_vitesses,
                style={'height': '100%', 'width': '100%'}
            )
        ]),

        # Camembert des vitesses
        html.Div(style={'padding': '20px', 'height': '85vh', 'width': '100%'}, children=[
            html.H2("Répartition des Vitesses (Camembert)"),
            dcc.Graph(
                id='pie-vitesses-page-2',
                figure=fig_pie_vitesses,
                style={'height': '100%', 'width': '100%'}
            )
        ]),

        
        # Histogramme des Positions de Début
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
