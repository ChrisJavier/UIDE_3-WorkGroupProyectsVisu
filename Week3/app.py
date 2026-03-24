import dash
from dash import html, dcc, Input, Output

# ── Data y utilidades ─────────────────────────────────────────────
from data import df
from utils import filt
from config import Colors

# ── Componentes ───────────────────────────────────────────────────
from components.navbar import create_navbar

# ── Páginas ───────────────────────────────────────────────────────
from pages.general import layout_general
from pages.espera import layout_espera
from pages.departamentos import layout_departamentos
from pages.tendencia import layout_tendencia
from pages.popup_welcome import layout_popup_welcome

# ── Callbacks ─────────────────────────────────────────────────────
from callbacks.general_cb import register_callbacks as general_cb
from callbacks.espera_cb import register_callbacks as espera_cb
from callbacks.departamentos_cb import register_callbacks as dep_cb
from callbacks.tendencia_cb import register_callbacks as ten_cb
from callbacks.popup_welcome_cb import register_callbacks as popup_cb

# ── Inicialización de la app ──────────────────────────────────────
# Solo una vez, con todos los parámetros necesarios
app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True,
    external_stylesheets=[# Si usas alguna fuente externa o CSS, ponlo aquí
    ]
)

# ESTO ES VITAL: Definir server DESPUÉS de crear la app definitiva
server = app.server 

app.title = "Clinical Analytics Dashboard"

# ── Layout principal ──────────────────────────────────────────────
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    create_navbar(),
    layout_popup_welcome(),
    html.Div(id="page-content", 
             style={"minHeight": "calc(100vh - 68px)"})
],
style={
    "background": Colors["bg"],
    "color": Colors["text"],
    "minHeight": "100vh",
    "fontFamily": "Inter, sans-serif" 
})


# ── Router de páginas ─────────────────────────────────────────────
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def router(path):
    """
    Controla la navegación entre páginas del dashboard.

    Dependiendo de la URL:
    - "/" → Vista General
    - "/espera" → Tiempos de espera
    - "/departamentos" → Análisis por departamento
    - "/tendencia" → Tendencia mensual

    Retorna el layout correspondiente.
    """
    if path == "/espera":
        return layout_espera()
    elif path == "/departamentos":
        return layout_departamentos()
    elif path == "/tendencia":
        return layout_tendencia()
    else:
        return layout_general()


# ── Registro de callbacks ─────────────────────────────────────────
general_cb(app, df, filt)
espera_cb(app, df, filt)
dep_cb(app, df, filt)
ten_cb(app, df, filt)
popup_cb(app, df, filt)


# ── Run app ───────────────────────────────────────────────────────
# Version local
#if __name__ == "__main__":
#    app.run(debug=True, port=8050)
# Version Render
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=10000)   