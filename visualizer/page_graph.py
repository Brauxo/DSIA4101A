from dash import dcc, html, Input, Output
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

    # Histogram for segment distances
    data_frame['distance_troncon'] = data_frame['pk_fin'] - data_frame['pk_debut']
    fig_histogram_distances = px.histogram(
        data_frame, x='distance_troncon', nbins=20, title='Distribution des distances des segments',
        labels={'distance_troncon': 'Distance du segment (km)'}
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

        # Dropdown for selecting line type for speed histogram
        html.Div(children=[
            html.Label("ATTENTION : il faut actualiser (f5) une unique fois pour que les données s'affichent. L'histogramme des distances des segments ainsi que le camembert des types d'électrifications ne sont pas dynamiques."),
            dcc.Dropdown(
                id='line-type-dropdown',
                options=[
                    {'label': 'Toutes les lignes', 'value': 'both'},
                    {'label': 'Lignes grande vitesse (LGV)', 'value': 'LGV'},
                    {'label': 'Lignes classiques', 'value': 'classique'}
                ],
                value='both',
                clearable=False,
                style={'width': '50%', 'margin': 'auto'}
            )
        ]),

        # Tabs for selecting the chart type
        dcc.Tabs([
            dcc.Tab(label='Histogramme des vitesses', children=[
                dcc.Graph(id='speed-histogram', style={'height': '70vh', 'width': '100%'})
            ]),
            dcc.Tab(label='Histogramme des distances des segments', children=[
                dcc.Graph(id='distance-histogram', style={'height': '70vh', 'width': '100%'})
            ]),
            dcc.Tab(label='Camembert des vitesses', children=[
                dcc.Graph(id='speed-pie-chart', style={'height': '70vh', 'width': '100%'})
            ]),
            dcc.Tab(label='Boxplot des vitesses', children=[
                dcc.Graph(id='speed-boxplot', style={'height': '70vh', 'width': '100%'})
            ]),
            dcc.Tab(label='Scatterplot des vitesses', children=[
                dcc.Graph(id='speed-scatter', style={'height': '70vh', 'width': '100%'})
            ]),
            dcc.Tab(label="Camembert des types d'électrification", children=[
                dcc.Graph(id='electrification-pie', style={'height': '70vh', 'width': '100%'})
            ])
        ], style={'width': '80%', 'margin': 'auto'}),

        create_footer(app)
    ])

    # Callback to update the speed histogram based on selected line type
    @app.callback(
        Output('speed-histogram', 'figure'),
        Input('line-type-dropdown', 'value')
    )
    def update_speed_histogram(line_type):
        if line_type == 'LGV':
            filtered_data = vitesses_df[vitesses_df['detail'] >= 250]
        elif line_type == 'classique':
            filtered_data = vitesses_df[vitesses_df['detail'] < 250]
        else:
            filtered_data = vitesses_df
        return px.histogram(
            filtered_data, x='detail', nbins=30, title='Distribution des vitesses par segment',
            labels={'detail': 'Vitesse (km/h)'}
        )

    # Callback for updating the distance histogram
    @app.callback(
        Output('distance-histogram', 'figure'),
        Input('line-type-dropdown', 'value')
    )
    def update_distance_histogram(line_type):
        filtered_data = data_frame.copy()
        if line_type == 'LGV':
            filtered_data = filtered_data[filtered_data['vitesses'].apply(lambda v: any(speed >= 250 for speed in v))]
        elif line_type == 'classique':
            filtered_data = filtered_data[filtered_data['vitesses'].apply(lambda v: all(speed < 250 for speed in v))]
        return px.histogram(
            filtered_data, x='distance_troncon', nbins=20, title='Distribution des distances des segments',
            labels={'distance_troncon': 'Distance du segment (km)'}
        )

    # Callback for updating the speed pie chart
    @app.callback(
        Output('speed-pie-chart', 'figure'),
        Input('line-type-dropdown', 'value')
    )
    def update_speed_pie_chart(line_type):
        filtered_data = vitesses_df.copy()
        if line_type == 'LGV':
            filtered_data = filtered_data[filtered_data['detail'] >= 250]
        elif line_type == 'classique':
            filtered_data = filtered_data[filtered_data['detail'] < 250]
        return px.pie(filtered_data, names='detail', title='Répartition des vitesses')

    # Callback for updating the speed boxplot
    @app.callback(
        Output('speed-boxplot', 'figure'),
        Input('line-type-dropdown', 'value')
    )
    def update_speed_boxplot(line_type):
        filtered_data = vitesses_df.copy()
        if line_type == 'LGV':
            filtered_data = filtered_data[filtered_data['detail'] >= 250]
        elif line_type == 'classique':
            filtered_data = filtered_data[filtered_data['detail'] < 250]
        return px.box(filtered_data, y='detail', title="Répartition des vitesses par segment")

    # Callback for updating the scatter plot
    @app.callback(
        Output('speed-scatter', 'figure'),
        Input('line-type-dropdown', 'value')
    )
    def update_speed_scatter(line_type):
        filtered_data = vitesses_df.copy()
        if line_type == 'LGV':
            filtered_data = filtered_data[filtered_data['detail'] >= 250]
        elif line_type == 'classique':
            filtered_data = filtered_data[filtered_data['detail'] < 250]
        return px.scatter(
            filtered_data, x='pk_debut', y='detail', title="Position de début vs Vitesses"
        )

    # Callback for updating the electrification pie chart
    @app.callback(
        Output('electrification-pie', 'figure'),
        Input('line-type-dropdown', 'value')
    )
    def update_electrification_pie(line_type):
        filtered_data = electrifications_df.copy()
        if line_type == 'LGV':
            filtered_data = filtered_data[filtered_data['detail'].str.contains('LGV', na=False)]
        elif line_type == 'classique':
            filtered_data = filtered_data[filtered_data['detail'].str.contains('classique', na=False)]
        return px.pie(filtered_data, names='detail', title="Types d'électrification")

    return layout

