import dash
from dash import dcc, html
from visualizer.simple_page_home import simple_page_home
from visualizer.simple_page import simple_page
from visualizer.simple_page2 import simple_page2
from visualizer.simple_page3 import simple_page3
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

class dashboardholder:
    
    def __init__(self, dataframe):
        self.data_frame = dataframe
        self.app = dash.Dash(__name__)

        # Utilisatiion d'un thème de dashboard 
        theme = dbc.themes.LUX
        self.app = dash.Dash(__name__, external_stylesheets=[theme])

        # Créer un premier layout
        self.app.layout = html.Div(style={'height': '100vh', 'width': '100vw'}, children=[
            dcc.Location(id='url', refresh=False),  # Track the URL
            html.Div(id='page-content', style={'height': '100%', 'width': '100%'})  # Responsive page content
        ])

        # Definit les callbacks
        @self.app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            if pathname == '/':
                return simple_page_home(self.app)  # Page d'acceuil
            elif pathname == '/page-1':
                return simple_page(self.app,self.data_frame)  # Page 1
            elif pathname == '/page-2':
                return simple_page2(self.app,self.data_frame)  # Page 2
            elif pathname == '/page-3':
                return simple_page3(self.app,self.data_frame)  # Page 3
            else:
                return simple_page_home(self.app, self.data_frame)  # Retourne sur la page d'acceuil

    def run(self):
        self.app.run_server(debug=True)
