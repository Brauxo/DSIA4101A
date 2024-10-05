from dash import dcc, html

def create_navbar():
    return html.Div(className='navbar', children=[
        dcc.Link([
            html.Img(src='/assets/home.png', className='nav-icon'),
        ], href='/', className='nav-link home-icon'),  # Ajout d'une classe spécifique

        dcc.Link([
            html.Img(src='/assets/map.png', className='nav-icon'),
        ], href='/page-1', className='nav-link map-icon'),  # Ajout d'une classe spécifique

        dcc.Link([
            html.Img(src='/assets/bar_chart.png', className='nav-icon'),
        ], href='/page-2', className='nav-link chart-icon'),  # Ajout d'une classe spécifique

        dcc.Link([
            html.Img(src='/assets/us.png', className='nav-icon'),
        ], href='/page-3', className='nav-link us-icon'),  # Ajout d'une classe spécifique
    ])
