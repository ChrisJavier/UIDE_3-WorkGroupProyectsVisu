# Creación de barra de navegación

# Importacion de librerias
from dash import html, dcc
from config import Colors

def navlink(label, href):
    """
    Crea un enlace de navegación estilizado para el navbar.

    Parámetros:
    - label: texto visible del enlace
    - href: ruta a la que navega

    Retorna:
    - Componente dcc.Link con estilos personalizados
    """
    return dcc.Link(label, href=href, style={
        "color": Colors["muted"],
        "textDecoration": "none",
        "fontSize": "0.9rem",
        "padding": "8px 16px",
        "borderRadius": "8px",
    })


def create_navbar():
    """
    Construye la barra de navegación principal del dashboard.

    Incluye:
    - Título de la aplicación
    - Enlaces a las diferentes páginas

    Retorna:
    - Componente html.Div que representa el navbar completo
    """
    return html.Div([
        html.Div([
            html.Div([
                html.Span("🏥", style={"fontSize": "1.3rem"}),
                html.Span("Clinical Analytics", style={
                    "color": Colors["text"],
                    "fontWeight": "700",
                    "fontSize": "1.05rem",
                    "marginLeft": "10px"
                }),
            html.A(
                html.Img(
                    src="/assets/25231.png",
                    className="logo-hover",
                    title="Ver repositorio en GitHub",
                    style={
                    "height": "40px",
                    "marginLeft": "10px"
                    }
                ),
                href="https://github.com/ChrisJavier/UIDE_3-WorkGroupProyectsVisu/tree/main/Week3",
                target="_blank"
            )                 
            ], style={"display": "flex", "alignItems": "center"}),

            html.Div([
                navlink("Vista General", "/"),
                navlink("Tiempos de Espera", "/espera"),
                navlink("Departamentos", "/departamentos"),
                navlink("Tendencia Mensual", "/tendencia"),
            ], style={"display": "flex", 
                      "gap": "4px"}),

        ], style={
            "display": "flex",
            "justifyContent": "space-between",
            "alignItems": "center",
            "maxWidth": "1400px",
            "margin": "0 auto",
            "padding": "0 22px"
        }),
    ], style={
        "background": Colors["card"],
        "borderBottom": f"1px solid {Colors['border']}",
        "padding": "14px 0",
        "position": "sticky",
        "top": "0",
        "zIndex": "1000",
    })