from dash import dcc, html


def create_navbar():
    """
    Creates a navigation bar with links represented by icons.

    Returns:
        html.Div: A div containing the navbar with clickable icons.
    """
    return html.Div(className='navbar', children=[

        # Home link with icon
        dcc.Link([
            html.Img(src='/assets/home.png', className='nav-icon'),
        ], href='/', className='nav-link home-icon'),  # Adds a specific class for home link styling

        # Map page link with icon
        dcc.Link([
            html.Img(src='/assets/map.png', className='nav-icon'),
        ], href='/page-map', className='nav-link map-icon'),  # Adds a specific class for map link styling

        # Graph page link with icon
        dcc.Link([
            html.Img(src='/assets/bar_chart.png', className='nav-icon'),
        ], href='/page-graph', className='nav-link chart-icon'),  # Adds a specific class for graph link styling

        # About Us page link with icon
        dcc.Link([
            html.Img(src='/assets/us.png', className='nav-icon'),
        ], href='/page-about_us', className='nav-link us-icon'),  # Adds a specific class for about us link styling
    ])
