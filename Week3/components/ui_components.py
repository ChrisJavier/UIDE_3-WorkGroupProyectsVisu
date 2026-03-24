from dash import html, dcc
from config import Colors

# ── Capa grafica 
def card(*children):
    return html.Div(list(children), style={
        "backgr ound": Colors["card"], "border": f"1px solid {Colors['border']}",
        "borderRadius": "12px", "padding": "16px",
    })

def kpi(title, value, sub, color):
    return html.Div([
        html.P(title, style={"color": Colors["muted"], "fontSize": "0.72rem",
                              "margin": "0 0 4px", "textTransform": "uppercase",
                              "letterSpacing": "1px"}),
        html.H3(value, style={"color": color, "fontSize": "1.9rem",
                               "fontWeight": "700", "margin": "0"}),
        html.P(sub, style={"color": Colors["muted"], "fontSize": "0.72rem",
                            "margin": "4px 0 0"}),
    ], style={
        "background": Colors["card"], "border": f"1px solid {Colors['border']}",
        "borderLeft": f"4px solid {color}", "borderRadius": "12px", "padding": "18px",
    })

def row2(*cols):
    return html.Div(list(cols), style={
        "display": "grid",
        "gridTemplateColumns": " ".join(["1fr"] * len(cols)),
        "gap": "16px", "marginBottom": "18px",
    })

def create_graph(graph_id, h=320):
    return dcc.Graph(id=graph_id, style={"height": f"{h}px"},
                     config={"displayModeBar": False})