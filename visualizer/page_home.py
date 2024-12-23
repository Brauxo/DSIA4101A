from dash import dcc, html
from visualizer.components.header import create_header
from visualizer.components.footer import create_footer
from visualizer.components.navbar import create_navbar

def page_home(app):
    """
    Creates the layout for the home page of the railway dashboard.

    Args:
        app (Dash): The Dash application instance.

    Returns:
        html.Div: The layout structure for the home page with introductory information,
                  regional train network visualization, and interactive data insights.
    """
    layout = html.Div([
        # Insert header and navbar
        create_header(),
        create_navbar(),

        # Page title
        html.H1("Bienvenue sur le Dashboard des Chemins de Fer",
                style={'textAlign': 'center', 'marginTop': '30px'}),

        # Paragraph explaining the site's purpose
        html.P(
            """
            Ce dashboard a pour objectif de fournir une vue d'ensemble sur l'infrastructure des chemins de fer en France. 
            Grâce aux données publiques, nous explorons la répartition géographique des lignes de train et analysons plusieurs 
            aspects des chemins de fer français, tels que la densité des lignes par région, la longueur moyenne des lignes, 
            ainsi que leur évolution historique.

            L'importance des chemins de fer en France ne se limite pas à la simple infrastructure de transport, mais joue un rôle clé dans le développement économique, 
            l’aménagement territorial et la réduction de l'empreinte carbone. Ce dashboard permet à ses utilisateurs d'explorer visuellement ces aspects à l'aide de cartes et 
            de graphiques interactifs qui fournissent des perspectives précieuses sur l'état et l'évolution du réseau ferroviaire.
            """,
            style={'textAlign': 'justify', 'padding': '0 10%', 'marginTop': '20px'}
        ),

        # First section: Text on the left and map (image) on the right
        html.Div([
            html.Div([
                html.H3("Les Chemins de Fer en France"),
                html.P(
                    """
                    La carte ci-contre illustre le réseau des chemins de fer en France, permettant une vue d'ensemble des 
                    lignes ferroviaires à travers le pays. Ce réseau est un élément essentiel du transport national, reliant 
                    les régions entre elles et facilitant le transport de personnes et de marchandises.

                    Vous pourrez explorer ici les principales lignes à grande vitesse (LGV), les lignes régionales ainsi que les 
                    trajets internationaux. Cette carte met en lumière les zones les plus denses du réseau, telles que la région 
                    Île-de-France, ainsi que les zones plus rurales où le réseau est moins développé. Ce tableau interactif permet 
                    d’explorer la répartition géographique des lignes ferroviaires.
                    """,
                    style={'textAlign': 'justify'}
                )
            ], style={'width': '45%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingRight': '20px'}),

            html.Div([
                html.Img(src='/assets/map_example.PNG',
                         style={'width': '100%', 'borderRadius': '10px'})
            ], style={'width': '45%', 'display': 'inline-block', 'verticalAlign': 'top'})

        ], style={'textAlign': 'center', 'padding': '30px 10%'}),  # Center the section

        # Second section: Image (histogram) on the left and text on the right
        html.Div([
            html.Div([
                html.Img(src='/assets/data_example.PNG',
                         style={'width': '100%', 'borderRadius': '10px'})
            ], style={'width': '45%', 'display': 'inline-block', 'verticalAlign': 'top', 'paddingRight': '20px'}),

            html.Div([
                html.H3("Analyse Statistique des Lignes de Chemins de Fer"),
                html.P(
                    """
                    Les graphiques interactifs de cette section montrent diverses statistiques liées au réseau ferroviaire français. 
                    Vous pourrez découvrir la répartition des lignes selon leur longueur, la densité des chemins de fer dans chaque 
                    région, et analyser l'évolution de la construction du réseau au fil du temps.

                    Les histogrammes illustrent également les différences entre les zones urbaines et rurales, mettant en lumière 
                    les disparités en termes d'infrastructures de transport. De plus, les données montrent les tendances dans 
                    l’extension du réseau ferroviaire, en lien avec les politiques publiques récentes visant à promouvoir des 
                    modes de transport plus durables et écologiques.
                    """,
                    style={'textAlign': 'justify'}
                )
            ], style={'width': '45%', 'display': 'inline-block', 'verticalAlign': 'top'})

        ], style={'textAlign': 'center', 'padding': '30px 10%'}),  # Center the section

        # Footer
        create_footer(app)
    ])

    return layout
