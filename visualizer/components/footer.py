from dash import html

def create_footer(app):
    """
    Create a footer for the web page with copyright and attribution information.

    Args:
        app: The Dash app instance to access asset URLs.

    Returns:
        dash.html.Footer: An HTML <footer> element with copyright and
        attribution information.
    """
    return html.Footer([
        html.Div([
            # Logo Esiee
            html.Img(
                src=app.get_asset_url('logo.png'),
                className='logo'
            ),

            # Copyright
            html.Div(
                'Copyright © 2024 / 2025',
                className='copyright'
            ),

            # Credits
            html.Div(
                'CAMBIER Elliot / BRAUX Owen, encadrés par '
                'Monsieur COURIVAUD D.',
                className='credits'
            ),

            # Unit
            html.Div(
                'DSIA-4101A : Python pour la Data Science',
                className='unit'
            ),

            # Logo ESIEE Paris
            html.Img(
                src=app.get_asset_url('logo.png'),
                className='logo'
            ),
        ], className='footer')
    ])
