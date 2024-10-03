from dash import dcc, html

def create_navbar():
    return html.Div(className='navbar', children=[
        dcc.Link([
            html.Img(src='/assets/map.png', className='nav-icon'),  # Icône histogramme
        ], href='/', className='nav-link'),
        dcc.Link([
            html.Img(src='/assets/bar_chart.png', className='nav-icon'),  # Icône carte
        ], href='/page-2', className='nav-link'),
    ])
