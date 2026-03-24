# Creación de la pagina VISION GENERAL

#importacion de librerias
from dash import html
from data import df

# Importar módulos
from components.ui_components import card, kpi, row2, create_graph
from components.sidebar import sidebar
from config import Colors

def layout_general():
    """
    Genera la vista general del dashboard.

    Incluye:
    - KPIs principales (total, espera, score, cancelaciones)
    - Gráficos de distribución (clínica, fuente, estado, care score)
    - Panel de filtros lateral

    Retorna:
    - Layout completo de la página "Vista General"
    """    
    return html.Div([
        html.Div([
            kpi("Total Consultas", f"{len(df):,}", "Registros año 2014", Colors["primary"]),
            kpi("Espera Promedio", f"{df['Wait Time Min'].mean():.0f} min",
                f"Mediana: {df['Wait Time Min'].median():.0f} min", Colors["warning"]),
            kpi("Care Score Prom.", f"{df['Care Score'].mean():.2f}", "Escala 2–10", Colors["success"]),
            kpi("Tasa Cancelación",
                f"{(df['Encounter Status']=='Cancelled').mean()*100:.1f}%",
                f"{(df['Encounter Status']=='Cancelled').sum():,} cancelados", Colors["danger"]),
        ], style={
            "display": "grid", 
            "gridTemplateColumns": "repeat(4,1fr)",
            "gap": "16px", 
            "marginBottom": "18px"}),
        html.Div([
            html.Div([
                row2(card(create_graph("g-pie")), 
                     card(create_graph("g-src"))),
                row2(card(create_graph("g-sta")), 
                     card(create_graph("g-care"))),
            ], style={"flex": "1"}),
            sidebar("gen"),
        ], style={
            "display": "flex", 
            "gap": "18px", 
            "alignItems": "flex-start"
            }),
    ], style={
        "padding": "22px", 
        "maxWidth": "1400px", 
        "margin": "0 auto",
        "background": Colors["bg"]
        })