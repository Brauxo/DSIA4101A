import dash
from dash import dcc, html
from visualizer.page_home import page_home
from visualizer.page_map import page_map
from visualizer.page_graph import page_graph
from visualizer.page_aboutus import page_aboutus
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc


class DashboardHolder:
    """
    A class to create and manage a Dash dashboard application.

    This class initializes a Dash app with different pages, each displaying specific information.
    It takes a DataFrame as input and sets up URL-based navigation to switch between pages.

    Args:
        dataframe (pd.DataFrame): A DataFrame containing the data to be displayed.
    """

    def __init__(self, dataframe):
        """
        Initialize the DashboardHolder with the provided data and set up the Dash app.

        Args:
            dataframe (pd.DataFrame): The DataFrame used for generating dashboard content.
        """
        self.data_frame = dataframe
        self.app = dash.Dash(__name__)
        

        # Applying a theme to the dashboard
        theme = dbc.themes.LUX
        self.app = dash.Dash(__name__, external_stylesheets=[theme])


        # Set up the initial layout with a responsive wrapper
        self.app.layout = html.Div(style={'height': '100vh', 'width': '100vw'}, children=[
            dcc.Location(id='url', refresh=False),  # Track the URL for navigation
            html.Div(id='page-content', style={'height': '100%', 'width': '100%'})  # Dynamic page content
        ])
        

        # Define callbacks for URL-based page navigation
        @self.app.callback(
            Output('page-content', 'children'),
            Input('url', 'pathname')
        )
        def display_page(pathname):
            """
            Callback function to display the page content based on the URL path.

            Args:
                pathname (str): The URL path, used to select which page to display.

            Returns:
                dash.html.Div: The content of the selected page.
            """
            if pathname == '/':
                return page_home(self.app)
            elif pathname == '/page-map':
                return page_map(self.app, self.data_frame)
            elif pathname == '/page-graph':
                return page_graph(self.app, self.data_frame)
            elif pathname == '/page-about_us':
                return page_aboutus(self.app, self.data_frame)
            else:
                return page_home(self.app)

    def run(self):
        """
        Run the Dash server in debug mode.

        This method starts the Dash app server and enables debug mode to assist in development.
        """
        self.app.run_server(debug=False) #False becasue the project is finished
