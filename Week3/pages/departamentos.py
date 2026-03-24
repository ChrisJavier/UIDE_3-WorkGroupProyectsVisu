# Importar librerias
from dash import html
from data import df

# Importar módulos
from components.ui_components import card, row2, create_graph
from components.sidebar import sidebar
from config import Colors

def layout_departamentos():
    """
    Genera la vista de análisis por departamentos.

    Incluye:
    - Volumen de consultas por departamento
    - Heatmap departamento vs clínica
    - Care score promedio por departamento
    - Relación entre espera y calidad (scatter)

    Permite análisis comparativo entre áreas médicas.
    """
    return html.Div([
        html.Div([
            html.Div([
                row2(card(create_graph("d-vol", h=360)), 
                     card(create_graph("d-heat", h=360))),
                row2(card(create_graph("d-care")), 
                     card(create_graph("d-scat"))),
            ], style={"flex": "1"}
            ),
            sidebar("dep"),
        ], style={"display": "flex", 
                  "gap": "18px", 
                  "alignItems": "flex-start"
                  }),
    ], style={"padding": "22px", 
              "maxWidth": "1400px", 
              "margin": "0 auto"
              })    