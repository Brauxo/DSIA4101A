from dash import html

def create_header():
    return html.Div([
        html.H2("Le réseau de chemin de fer en France", className='header-title'),
        html.Hr(className='header-hr')  # Ajoute une ligne horizontale sous le titre
    ], className='header')  # Ajoute une classe pour le style du header
