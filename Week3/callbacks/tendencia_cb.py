# Callbacks — Tendencia Mensual ─────────────────────────────────────────────
# Importar librerias
from dash import Input, Output
import plotly.express as px

# Importar módulos
from config import Color
from config import Colors, LAYOUT_BASE
from data import MONTH_ORDER

def register_callbacks(app, df, filt):
    """
    Registra los callbacks de la vista de tendencia mensual.

    Genera:
    - Volumen de consultas por mes (area chart)
    - Tiempo de espera promedio mensual
    - Care score promedio mensual
    - Distribución de tipos de admisión por mes

    Usa ordenamiento temporal correcto mediante MONTH_ORDER.
    """    
    # ── Callbacks — Tendencia Mensual ───────  
    @app.callback(
        [Output("t-vol","figure"), Output("t-wait","figure"),
        Output("t-care","figure"), Output("t-adm","figure")],
        [Input("dp-ten","value"), Input("at-ten","value"), Input("cl-ten","value")],
    )
    def cb_tendencia(dp, at, cl):
        dff = filt(df.copy(), dp, at, cl)
        cat = {"Month Label": MONTH_ORDER}

        df_vol = (dff.groupby(["Month","Month Label"]).size()
                .reset_index(name="Encounters").sort_values("Month"))
        fig_vol = px.area(df_vol, 
                          x="Month Label", 
                          y="Encounters",
                          title="Consultas Mensuales — 2014", 
                          category_orders=cat,
                          color_discrete_sequence=[Colors["primary"]])
        fig_vol.update_traces(fill="tozeroy", fillcolor="rgba(108,99,255,0.15)", line_width=2.5)
        fig_vol.update_layout(**LAYOUT_BASE)

        df_wait = (dff.groupby(["Month","Month Label"])["Wait Time Min"]
                .mean().round(1).reset_index().sort_values("Month"))
        fig_wait = px.line(df_wait, 
                           x="Month Label", 
                           y="Wait Time Min",
                           title="Espera Promedio Mensual", 
                           markers=True,
                           category_orders=cat, 
                           color_discrete_sequence=[Colors["warning"]])
        fig_wait.update_layout(**LAYOUT_BASE)

        df_care = (dff.groupby(["Month","Month Label"])["Care Score"]
                .mean().round(3).reset_index().sort_values("Month"))
        fig_care = px.line(df_care, 
                           x="Month Label", 
                           y="Care Score",
                           title="Care Score Promedio Mensual", 
                           markers=True,
                           category_orders=cat, 
                           color_discrete_sequence=[Colors["success"]])
        fig_care.update_layout(**LAYOUT_BASE)

        df_adm = (dff.groupby(["Month","Month Label","Admit Type"])
                .size().reset_index(name="Count").sort_values("Month"))
        fig_adm = px.bar(df_adm, 
                         x="Month Label", 
                         y="Count", 
                         color="Admit Type",
                         barmode="stack", 
                         title="Tipo de Admisión por Mes", 
                         category_orders=cat)
        fig_adm.update_layout(**LAYOUT_BASE)

        return fig_vol, fig_wait, fig_care, fig_adm
