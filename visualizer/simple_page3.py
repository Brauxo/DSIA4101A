from dash import dcc, html
from visualizer.components.header import create_header
from visualizer.components.footer import create_footer
from visualizer.components.navbar import create_navbar


def simple_page3(app, data_frame):
    layout = html.Div([
        create_header(),
        create_navbar(),
        html.H1("About Us", style={'textAlign': 'center', 'marginTop': '0px', 'marginBottom': '0px'}),  # Titre centré

        # Section avec deux cases côte à côte pour les photos, noms, et textes
        html.Div([
            html.Div([  # Première case pour la première photo, nom et texte
                html.H3("Elliot CAMBIER", style={'marginTop': '10px', 'marginBottom': '10px', 'textAlign': 'center'}),  # Nom ajouté au-dessus de la photo
                html.Img(src='/assets/elliot.jpg', style={'width': '150px', 'height': '200px', 'borderRadius': '10px', 'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                # Image centrée dans la case
                html.P("Étudiant en 4ème année d'ingénierie à l'ESIEE Paris, spécialisé en Data Science et Intelligence Artificielle (DSIA). Les projets liés à la Data Science m'intéressent particulièrement, notamment après avoir choisi l'année dernière des électives en Data Science, IA et Deep Learning.",
                       style={'textAlign': 'justify', 'marginTop': '1rem', 'padding': '0 10px'})  # Texte justifié
            ], style={
                'width': '300px',  # Largeur fixe pour les boîtes
                'height': 'auto',  # Hauteur automatique
                'display': 'inline-block',
                'textAlign': 'center',
                'verticalAlign': 'top',
                'border': '1px solid gray',  # Bordure grise
                'borderRadius': '10px',  # Coins arrondis
                'padding': '10px',  # Espacement interne
                'boxSizing': 'border-box',  # Assure que padding + width sont pris en compte
                'margin': '15px'  # Espacement autour de la case
            }),

            html.Div([  # Deuxième case pour la seconde photo, nom et texte
                html.H3("Owen BRAUX", style={'marginTop': '0px', 'marginBottom': '0px', 'textAlign': 'center'}),  # Nom ajouté au-dessus de la photo
                html.Img(src='/assets/owen.jpg', style={'width': '150px', 'height': '200px', 'borderRadius': '10px', 'display': 'block', 'marginLeft': 'auto', 'marginRight': 'auto'}),
                # Image centrée dans la case
                html.P("Actuellement étudiant, en 4ème année à l'ESIEE Paris. Je suis passionné par l'analyse de données et l'intelligence artificielle, j'ai choisi de suivre la filière DSIA pour approfondir mes connaissances et compétences dans ces domaines en plein essor.",
                       style={'textAlign': 'justify', 'marginTop': '1rem', 'padding': '0 10px'})  # Texte justifié
            ], style={
                'width': '300px',  # Largeur fixe pour les boîtes
                'height': 'auto',  # Hauteur automatique
                'display': 'inline-block',
                'textAlign': 'center',
                'verticalAlign': 'top',
                'border': '1px solid gray',  # Bordure grise
                'borderRadius': '10px',  # Coins arrondis
                'padding': '20px',  # Espacement interne
                'boxSizing': 'border-box',  # Assure que padding + width sont pris en compte
                'margin': '15px'  # Espacement autour de la case
            })

        ], style={
            'display': 'flex',  # Flexbox pour centrer
            'justifyContent': 'center',  # Centre les deux cases horizontalement
            'alignItems': 'flex-start',  # Aligne les éléments en haut
            'flexWrap': 'wrap',  # Si l'écran est trop petit, les boîtes passeront l'une sous l'autre
            'marginTop': '0.5rem',  # Réduction de la marge entre "About Us" et les cases
            'padding': '0 5%'  # Marges sur les côtés
        }),

        # Section Contact avec des emails cliquables
        html.H1("Contact", style={'textAlign': 'center', 'marginTop': '5px', 'marginBottom': '0px'}),
        # Titre "Contact"
        html.P([
            html.A("elliot.cambier@edu.esiee.fr", href="mailto:elliot.cambier@edu.esiee.fr"),
            " & ",
            html.A("owen.braux@edu.esiee.fr", href="mailto:owen.braux@edu.esiee.fr")
        ], style={'textAlign': 'center', 'marginTop': '10px', 'padding': '0 10px'}),  # Emails centrés et cliquables

        # Section Logiciels utilisés avec 5 images et leurs titres
        html.H1("Logiciels utilisés", style={'textAlign': 'center', 'marginTop': '20px', 'marginBottom': '0px'}),
        html.Div([

            # Python logo
            html.Div([
                html.Img(src='/assets/python_logo.jpg',
                         style={'width': 'auto', 'height': '80px', 'display': 'block', 'marginLeft': 'auto',
                                'marginRight': 'auto'}),
            ], style={
                'width': 'auto',
                'display': 'inline-block',
                'textAlign': 'center',
                'margin': '10px'
            }),

            # Dash logo
            html.Div([
                html.Img(src='/assets/dash_logo.png',
                         style={'width': 'auto', 'height': '80px', 'display': 'block', 'marginLeft': 'auto',
                                'marginRight': 'auto'}),
            ], style={
                'width': 'auto',
                'display': 'inline-block',
                'textAlign': 'center',
                'margin': '10px'
            }),

            # PyCharm logo
            html.Div([
                html.Img(src='/assets/pycharm_logo.png',
                         style={'width': 'auto', 'height': '80px', 'display': 'block', 'marginLeft': 'auto',
                                'marginRight': 'auto'}),
            ], style={
                'width': 'auto',
                'display': 'inline-block',
                'textAlign': 'center',
                'margin': '10px'
            }),

            # GitHub logo
            html.Div([
                html.Img(src='/assets/github_logo.png',
                         style={'width': 'auto', 'height': '80px', 'display': 'block', 'marginLeft': 'auto',
                                'marginRight': 'auto'}),
            ], style={
                'width': 'auto',
                'display': 'inline-block',
                'textAlign': 'center',
                'margin': '10px'
            }),

            # CSS logo
            html.Div([
                html.Img(src='/assets/css_logo.png',
                         style={'width': 'auto', 'height': '80px', 'display': 'block', 'marginLeft': 'auto',
                                'marginRight': 'auto'}),
            ], style={
                'width': 'auto',
                'display': 'inline-block',
                'textAlign': 'center',
                'margin': '10px'
            })

        ], style={
            'display': 'flex',
            'justifyContent': 'center',
            'alignItems': 'center',
            'flexWrap': 'wrap',
            'marginTop': '0px'
        }),

        create_footer(app)  # Footer en bas de page
    ])

    return layout
