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
        vitesses_df, x='detail', nbins=30, title='Speed Distribution by Segment',
        labels={'detail': 'Speed (km/h)'}
    )

    # Pie chart for speed distribution
    fig_pie_vitesses = px.pie(vitesses_df, names='detail', title='Speed Distribution')
    fig_pie_vitesses.update_traces(textinfo='none')
    fig_pie_vitesses.update_layout(showlegend=True)

    # Boxplot for speed by segment
    fig_boxplot_vitesses = px.box(
        vitesses_df, y='detail', title="Speed Distribution by Segment",
        labels={'detail': 'Speed (km/h)'}
    )

    # Histogram for segment distances
    data_frame['distance_troncon'] = data_frame['pk_fin'] - data_frame['pk_debut']
    fig_histogram_distances = px.histogram(
        data_frame, x='distance_troncon', nbins=20, title='Segment Distance Distribution',
        labels={'distance_troncon': 'Segment Distance (km)'}
    )

    # Pie chart for electrification types, excluding NULL values
    electrifications_df = pd.DataFrame(data_frame.explode('electrifications')['electrifications'].apply(pd.Series))
    electrifications_df = electrifications_df.dropna(subset=['detail'])
    fig_pie_electrification = px.pie(electrifications_df, names='detail', title="Electrification Types")
    fig_pie_electrification.update_traces(textinfo='none')

    # Scatter plot for pk_debut vs. speeds
    fig_scatter_vitesses = px.scatter(
        vitesses_df, x='pk_debut', y='detail', title="Start Position vs. Speeds",
        labels={'pk_debut': 'Start Position (pk_debut)', 'detail': 'Speed (km/h)'}
    )

    # Page layout structure
    layout = html.Div(style={'height': '100vh', 'width': '100vw'}, children=[
        create_header(),
        create_navbar(),
        html.H1("Page 2 - Data Analysis and Visualization"),
        html.H2("_"),  # Spacer for design purposes

        # Speed distribution histogram and pie chart
        html.Div(style={'display': 'flex', 'justify-content': 'space-around', 'align-items': 'center', 'height': '40vh'}, children=[
            html.Div(style={'width': '45%', 'padding': '10px'}, children=[
                dcc.Graph(id='histogram-vitesses-page-2', figure=fig_histogram_vitesses, style={'height': '100%', 'width': '100%'})
            ]),
            html.Div(style={'width': '45%', 'padding': '10px'}, children=[
                dcc.Graph(id='pie-vitesses-page-2', figure=fig_pie_vitesses, style={'height': '100%', 'width': '100%'})
            ])
        ]),

        # Segment distance histogram and electrification types pie chart
        html.Div(style={'display': 'flex', 'justify-content': 'space-around', 'align-items': 'center', 'height': '40vh'}, children=[
            html.Div(style={'width': '45%', 'padding': '10px'}, children=[
                dcc.Graph(id='histogram-distances-troncons', figure=fig_histogram_distances, style={'height': '100%', 'width': '100%'})
            ]),
            html.Div(style={'width': '45%', 'padding': '10px'}, children=[
                dcc.Graph(id='pie-electrification', figure=fig_pie_electrification, style={'height': '100%', 'width': '100%'})
            ])
        ]),

        # Scatter plot for pk_debut vs. speed
        html.Div(style={'width': '100%', 'padding': '20px'}, children=[
            dcc.Graph(id='scatter-pkdebut-vitesses', figure=fig_scatter_vitesses, style={'height': '60vh', 'width': '100%'})
        ]),

        # Boxplot for speed distribution
        html.Div(style={'width': '100%', 'padding': '20px'}, children=[
            dcc.Graph(id='boxplot_vitesses', figure=fig_boxplot_vitesses, style={'height': '60vh', 'width': '100%'})
        ]),

        create_footer(app)
    ])

    return layout
