from dash import dcc, html
import pandas as pd
import plotly.express as px
from visualizer.components.header import create_header
from visualizer.components.footer import create_footer
from visualizer.components.navbar import create_navbar

def page_graph(app, data_frame):
    """
    Creates the layout for the data visualization page with various graphs.

    Args:
        app (Dash): The Dash application instance.
        data_frame (pd.DataFrame): A DataFrame containing railway data with columns

    Returns:
        html.Div: The layout structure for the visualization page containing several graphs.
    """
    # Drop rows with missing values in relevant columns to avoid errors
    data_frame = data_frame.dropna(subset=['pk_debut', 'pk_fin', 'vitesses']).copy()

    # Extract speed details per segment
    vitesses_df = pd.DataFrame(data_frame.explode('vitesses')['vitesses'].apply(pd.Series))
    vitesses_df['pk_debut'] = vitesses_df['from']
    vitesses_df = vitesses_df.dropna(subset=['detail'])  # Remove NULL values

    # Histogram for speed distribution
    fig_histogram_vitesses = px.histogram(
        vitesses_df, x='detail', nbins=30, title='Distribution des vitesses par segment',
        labels={'detail': 'Vitesse (km/h)'}
    )

    # Pie chart for speed distribution
    fig_pie_vitesses = px.pie(vitesses_df, names='detail', title='Répartition des vitesses')
    fig_pie_vitesses.update_traces(textinfo='none')
    fig_pie_vitesses.update_layout(showlegend=True)

    # Boxplot for speed by segment
    fig_boxplot_vitesses = px.box(
        vitesses_df, y='detail', title="Répartition des vitesses par segment",
        labels={'detail': 'Vitesse (km/h)'}
    )

    # Scatter plot for pk_debut vs. speeds
    fig_scatter_vitesses = px.scatter(
        vitesses_df, x='pk_debut', y='detail', title="Position de début vs Vitesses",
        labels={'pk_debut': 'Position de début (pk_debut)', 'detail': 'Vitesse (km/h)'}
    )

    # Histogram for segment distances
    data_frame['distance_troncon'] = data_frame['pk_fin'] - data_frame['pk_debut']
    fig_histogram_distances = px.histogram(
        data_frame, x='distance_troncon', nbins=20, title='Distribution des distances des segments',
        labels={'distance_troncon': 'Distance du segment (km)'}
    )

    # Pie chart for electrification types, excluding NULL values
    electrifications_df = pd.DataFrame(data_frame.explode('electrifications')['electrifications'].apply(pd.Series))
    electrifications_df = electrifications_df.dropna(subset=['detail'])
    fig_pie_electrification = px.pie(electrifications_df, names='detail', title="Types d'électrification")
    fig_pie_electrification.update_traces(textinfo='none')

    # Layout structure using Tabs for each chart
    layout = html.Div(style={'height': '100vh', 'width': '100vw'}, children=[
        create_header(),
        create_navbar(),
        html.H1("Analyse des Données et Visualisation :"),

        # Tabs for selecting the chart type
        dcc.Tabs([
            dcc.Tab(label='Histogramme des vitesses', children=[
                dcc.Graph(figure=fig_histogram_vitesses, style={'height': '70vh', 'width': '100%'})
            ]),
            dcc.Tab(label='Histogramme des distances des segments', children=[
                dcc.Graph(figure=fig_histogram_distances, style={'height': '70vh', 'width': '100%'})
            ]),
            dcc.Tab(label='Camembert des vitesses', children=[
                dcc.Graph(figure=fig_pie_vitesses, style={'height': '70vh', 'width': '100%'})
            ]),
            dcc.Tab(label='boxplot des vitesses', children=[
                dcc.Graph(figure=fig_boxplot_vitesses, style={'height': '70vh', 'width': '100%'})
            ]),
            dcc.Tab(label='Scatterplot des vitesses', children=[
                dcc.Graph(figure=fig_scatter_vitesses, style={'height': '70vh', 'width': '100%'})
            ]),
            dcc.Tab(label="Camembert des types d'électrification", children=[
                dcc.Graph(figure=fig_pie_electrification, style={'height': '70vh', 'width': '100%'})
            ])
        ], style={'width': '80%', 'margin': 'auto'}),

        create_footer(app)
    ])

    return layout
