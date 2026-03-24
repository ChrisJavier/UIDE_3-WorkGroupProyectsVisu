# Importar librerias
from dash import html
from data import df

# Importar módulos
from components.ui_components import card, row2, create_graph
from components.sidebar import sidebar
from config import Colors

def layout_tendencia():
    """
    Genera la vista de tendencia temporal.

    Incluye:
    - Volumen mensual de consultas
    - Tiempo de espera promedio por mes
    - Care score promedio mensual
    - Distribución de tipos de admisión por mes

    Permite análisis evolutivo del sistema.
    """
    return html.Div([
        html.Div([
            html.Div([
                card(create_graph("t-map", h=500)),
                card(create_graph("t-vol", h=320)),
                html.Div(style={"height": "18px"}),
                row2(card(create_graph("t-wait")), 
                     card(create_graph("t-care"))),
                html.Div(style={"height": "18px"}),
                card(create_graph("t-adm", h=300)),
            ], style={"flex": "1"}),
            sidebar("ten"),
        ], style={"display": "flex", 
                  "gap": "18px", 
                  "alignItems": "flex-start"
                  }),
    ], style={"padding": "22px", 
              "maxWidth": "1400px", 
              "margin": "0 auto",
        "background": Colors["bg"]})    