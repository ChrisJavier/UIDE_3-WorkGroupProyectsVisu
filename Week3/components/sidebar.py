# Creación de barra lateral con los filtros

# Importación de librerias y dataframes para las opciones de filtrado
from dash import html, dcc
from config import Colors
from data import CLINICS, ADMIT_TYPES, DEPARTMENTS

def sidebar(page):
    return html.Div([
        html.P("FILTROS", 
               style={"color": Colors["muted"], 
                      "fontSize": "0.68rem",
                      "letterSpacing": "2px", 
                      "margin": "0 0 14px"}),
        html.Label("Clínica", 
                   style={"color": Colors["muted"], 
                          "fontSize": "0.78rem"}),
        dcc.Checklist(
            id=f"cl-{page}", options=CLINICS, value=CLINICS,
            labelStyle={"display": "block", 
                        "color": Colors["text"],
                        "fontSize": "0.83rem", 
                        "marginBottom": "3px"},
            inputStyle={"marginRight": "7px", 
                        "accentColor": Colors["primary"]},
        ),
        html.Hr(style={"borderColor": Colors["border"], 
                       "margin": "14px 0"}),
        html.Label("Tipo de Admisión", 
                   style={"color": Colors["muted"], 
                          "fontSize": "0.78rem"}),
        dcc.Checklist(
            id=f"at-{page}", options=ADMIT_TYPES, value=ADMIT_TYPES,
            labelStyle={"display": "block", 
                        "color": Colors["text"],
                        "fontSize": "0.83rem", 
                        "marginBottom": "3px"},
            inputStyle={"marginRight": "7px", 
                        "accentColor": Colors["primary"]},
        ),
        html.Hr(style={"borderColor": Colors["border"], 
                       "margin": "14px 0"}),
        html.Label("Departamentos", 
                   style={"color": Colors["muted"], 
                          "fontSize": "0.78rem"}),
        dcc.Dropdown(id=f"dp-{page}", 
                     options=DEPARTMENTS, 
                     value=[], 
                     multi=True,
                     placeholder="Todos",
            style={"backgroundColor": Colors["bg"], 
                   "fontSize": "0.83rem",
                    "color": "black"}
        ),
    ], style={
        "background": Colors["card"], 
        "border": f"1px solid {Colors['border']}",
        "borderRadius": "12px", 
        "padding": "18px",
        "width": "210px", 
        "flexShrink": "0",
        "color": Colors["text"]
    })
