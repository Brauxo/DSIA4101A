import dash
from dash import dcc, html
from visualizer.components.header import create_header
from visualizer.components.footer import create_footer
from visualizer.components.navbar import create_navbar
from visualizer.simple_page import simple_page
from visualizer.simple_page2 import simple_page2
from dash.dependencies import Input, Output

class dashboardholder:
    def __init__(self, dataframe):
        self.data_frame = dataframe
        self.app = dash.Dash(__name__)

        # Set up the initial layout with dcc.Location
        self.app.layout = html.Div([
            dcc.Location(id='url', refresh=False),  # Track the URL
            html.Div(id='page-content'),  # Content changes based on the URL
        ])

        # Define the callback for URL changes
        @self.app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')]
        )
        def display_page(pathname):
            if pathname == '/':
                return simple_page(self.app, self.data_frame)  # Default page
            elif pathname == '/page-2':
                return simple_page2(self.app,self.data_frame)  # Page 2
            else:
                return simple_page(self.app, self.data_frame)  # Fallback to default

    def run(self):
        self.app.run_server(debug=True)
