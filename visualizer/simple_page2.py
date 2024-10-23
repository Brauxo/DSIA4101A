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
    # Evite les erreurs en ignorant les valeurs manquantes
    data_frame = data_frame.dropna(subset=['pk_debut', 'pk_fin', 'vitesses']).copy()

    # Extraction des vitesses par tronçon
    vitesses_df = pd.DataFrame(data_frame.explode('vitesses')['vitesses'].apply(pd.Series))
    vitesses_df['pk_debut'] = vitesses_df['from']  
    vitesses_df = vitesses_df.dropna(subset=['detail'])  # Enlève les valeurs NULL

    # Histogramme répartition des vitesses
    fig_histogram_vitesses = px.histogram(vitesses_df, x='detail', nbins=30,  
                                          title='Histogramme des Vitesses par Tronçon',
                                          labels={'detail': 'Vitesse (km/h)'})

    # Camembert répartition des vitesses
    fig_pie_vitesses = px.pie(vitesses_df, names='detail', title='Répartition des Vitesses')
    #design :
    fig_pie_vitesses.update_traces(textinfo='none')  
    fig_pie_vitesses.update_layout(showlegend=True)

    # Boxplot vitesses par tronçon
    fig_boxplot_vitesses = px.box(vitesses_df, y='detail', title="Distribution des Vitesses par Tronçon",
                                  labels={'detail': 'Vitesse (km/h)'})

    # Histogramme distances de tronçon 
    data_frame['distance_troncon'] = data_frame['pk_fin'] - data_frame['pk_debut']
    fig_histogram_distances = px.histogram(data_frame, x='distance_troncon', nbins=20,  
                                           title='Histogramme des Distances de Tronçon',
                                           labels={'distance_troncon': 'Distance du Tronçon (km)'})

    # Camembert des types d'électrification sans valeurs nulles
    electrifications_df = pd.DataFrame(data_frame.explode('electrifications')['electrifications'].apply(pd.Series))
    electrifications_df = electrifications_df.dropna(subset=['detail'])  # Enlève les valeurs NULL
    fig_pie_electrification = px.pie(electrifications_df, names='detail', title="Répartition des Types d'Électrification")
    fig_pie_electrification.update_traces(textinfo='none')  

    # Scatterplot pk_debut vs vitesses
    fig_scatter_vitesses = px.scatter(vitesses_df, x='pk_debut', y='detail',
                                      title="Relation entre Position (pk_debut) et Vitesses",
                                      labels={'pk_debut': 'Position de Début (pk_debut)', 'detail': 'Vitesse (km/h)'})

    # structure de la page 
    layout = html.Div(style={'height': '100vh', 'width': '100vw'}, children=[
        create_header(),
        create_navbar(),
        html.H1("Page 2 - Analyses et Visualisations des Données de la Ligne"),
        html.H2("_"), #permet de mettre un espace pour le edesign du site

        # Histogramme des Vitesses
        html.Div(style={'display': 'flex', 'justify-content': 'space-around', 'align-items': 'center', 'height': '40vh'}, children=[
            html.Div(style={'width': '45%', 'padding': '10px'}, children=[
                dcc.Graph(
                    id='histogram-vitesses-page-2',
                    figure=fig_histogram_vitesses,
                    style={'height': '100%', 'width': '100%'}
                )
            ]),

            # Camembert des Vitesses
            html.Div(style={'width': '45%', 'padding': '10px'}, children=[
                dcc.Graph(
                    id='pie-vitesses-page-2',
                    figure=fig_pie_vitesses,
                    style={'height': '100%', 'width': '100%'}
                )
            ])
        ]),

        # Histogramme des Distances de Tronçon
        html.Div(style={'display': 'flex', 'justify-content': 'space-around', 'align-items': 'center', 'height': '40vh'}, children=[
            html.Div(style={'width': '45%', 'padding': '10px'}, children=[
                dcc.Graph(
                    id='histogram-distances-troncons',
                    figure=fig_histogram_distances,
                    style={'height': '100%', 'width': '100%'}
                )
            ]),

            # Camembert des Types d'Électrification
            html.Div(style={'width': '45%', 'padding': '10px'}, children=[
                dcc.Graph(
                    id='pie-electrification',
                    figure=fig_pie_electrification,
                    style={'height': '100%', 'width': '100%'}
                )
            ])
        ]),

        # Scatterplot du pk_debut face à vitesses
        html.Div(style={'width': '100%', 'padding': '20px'}, children=[
            dcc.Graph(
                id='scatter-pkdebut-vitesses',
                figure=fig_scatter_vitesses,
                style={'height': '60vh', 'width': '100%'}
            )
        ]),

        # boxplot des vitesses
        html.Div(style={'width': '100%', 'padding': '20px'}, children=[
            dcc.Graph(
                id='boxplot_vitesses',
                figure=fig_boxplot_vitesses,
                style={'height': '60vh', 'width': '100%'}
            )
        ]),

        create_footer(app)
    ])

    return layout
