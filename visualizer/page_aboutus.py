from dash import dcc, html
from visualizer.components.header import create_header
from visualizer.components.footer import create_footer
from visualizer.components.navbar import create_navbar


def page_aboutus(app, data_frame):
    """
    Creates the layout for the About Us page, showcasing team profiles, contact information,
    and software used in the project.

    Args:
        app (Dash): The Dash application instance.
        data_frame (pd.DataFrame): Placeholder argument; not used in this function.

    Returns:
        html.Div: The layout structure for the About Us page with team profiles, contact, and software sections.
    """
    layout = html.Div([
        create_header(),
        create_navbar(),
        html.H1("About Us", className="page-title"),

        # Section with two side-by-side profile cards for photos, names, and texts
        html.Div([
            html.Div([
                html.H3("Elliot CAMBIER", className="name-title"),
                html.Img(src='/assets/elliot.jpg', className="profile-img"),
                html.P(
                    "Étudiant en 4ème année d'ingénierie à l'ESIEE Paris, spécialisé en Data Science et Intelligence Artificielle (DSIA). Les projets liés à la Data Science m'intéressent particulièrement, notamment après avoir choisi l'année dernière des électives en Data Science, IA et Deep Learning.",
                    className="profile-text")
            ], className="profile-card"),

            html.Div([
                html.H3("Owen BRAUX", className="name-title"),
                html.Img(src='/assets/owen.jpg', className="profile-img"),
                html.P(
                    "Actuellement étudiant, en 4ème année à l'ESIEE Paris. Je suis passionné par l'analyse de données et l'intelligence artificielle, j'ai choisi de suivre la filière DSIA pour approfondir mes connaissances et compétences dans ces domaines en plein essor.",
                    className="profile-text")
            ], className="profile-card")

        ], className="profile-section"),

        # Contact section with clickable email links
        html.H1("Contact", className="page-title"),
        html.P([
            html.A("elliot.cambier@edu.esiee.fr", href="mailto:elliot.cambier@edu.esiee.fr"),
            " & ",
            html.A("owen.braux@edu.esiee.fr", href="mailto:owen.braux@edu.esiee.fr")
        ], className="contact-info"),

        # Software used section with 5 logos and their titles
        html.H1("Logiciels utilisés", className="page-title"),
        html.Div([

            # Python logo
            html.Div([
                html.Img(src='/assets/python_logo.png', className="software-logo"),
            ], className="software-item"),

            # Dash logo
            html.Div([
                html.Img(src='/assets/dash_logo.png', className="software-logo"),
            ], className="software-item"),

            # PyCharm logo
            html.Div([
                html.Img(src='/assets/pycharm_logo.png', className="software-logo"),
            ], className="software-item"),

            # GitHub logo
            html.Div([
                html.Img(src='/assets/github_logo.png', className="software-logo"),
            ], className="software-item"),

            # CSS logo
            html.Div([
                html.Img(src='/assets/css_logo.png', className="software-logo"),
            ], className="software-item")

        ], className="software-section"),

        create_footer(app)
    ])

    return layout
