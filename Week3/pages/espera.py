# Importar librerias
from dash import html
from data import df

# Importar módulos
from components.ui_components import card, kpi, row2, create_graph
from components.sidebar import sidebar
from config import Colors

def layout_espera():
    """
    Genera la vista de análisis de tiempos de espera.

    Incluye:
    - KPIs de tiempo de espera (promedio, máximo, mínimo, mediana)
    - Histograma de distribución de espera
    - Boxplot por departamento
    - Gráfico de espera promedio

    Permite análisis detallado de eficiencia operativa.
    """
    return html.Div([
        html.Div([
            kpi("Espera Promedio", f"{df['Wait Time Min'].mean():.1f} min", "Global", Colors["primary"]),
            kpi("Espera Máxima", f"{df['Wait Time Min'].max()} min", "Caso más largo", Colors["danger"]),
            kpi("Espera Mínima", f"{df['Wait Time Min'].min()} min", "Caso más rápido", Colors["success"]),
            kpi("Mediana", f"{df['Wait Time Min'].median():.0f} min", "Percentil 50", Colors["warning"]),
        ], style={"display": "grid", 
                  "gridTemplateColumns": "repeat(4,1fr)",
                  "gap": "16px", 
                  "marginBottom": "18px"
                  }),
        html.Div([
            html.Div([
                row2(card(create_graph("e-hist")), card(create_graph("e-box"))),
                card(create_graph("e-bar", h=300)),
            ], style={"flex": "1"}),
            sidebar("esp"),
        ], style={"display": "flex", 
                  "gap": "18px", 
                  "alignItems": "flex-start"
                  }),
    ], style={"padding": "22px", 
              "maxWidth": "1400px", 
              "margin": "0 auto"
              })    