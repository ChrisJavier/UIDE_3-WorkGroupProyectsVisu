# Callbacks — Tendencia Mensual ─────────────────────────────────────────────
# Importar librerias
from dash import Input, Output
import plotly.express as px
import pandas as pd

# Importar módulos
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
        Output("t-care","figure"), Output("t-adm","figure"), Output("t-map","figure")],
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

        # Cambiar las coordeenadas de cada clinica
        coords_df = pd.DataFrame({
                "Clinic Name": ["Lakeview Center", "Madison Center", "Surgery Center"],
                "lat": [41.8781, 43.0731, 34.0522],
                "lon": [-87.6298, -89.4012, -118.2437]
        })

        dff = dff.merge(coords_df, on="Clinic Name", how="left")
        dff["Wait Time Min"] = dff["Wait Time Min"].clip(lower=0)

        df_map = dff.groupby(["Clinic Name", "lat", "lon"])["Wait Time Min"].mean().reset_index()
        fig_map = px.scatter_mapbox(
                df_map,
                lat="lat",
                lon="lon",
                color="Wait Time Min",
                size="Wait Time Min",
                hover_name="Clinic Name",
                title = "Mapa de USA con las clinicas",
                zoom=4,
                color_continuous_scale=["cyan", "red"]
                )

        fig_map.update_layout(    
            mapbox_style="carto-darkmatter",
    paper_bgcolor=Colors["bg"],
    font=dict(color="white"),
    margin=dict(l=0, r=0, t=30, b=0))

        return fig_vol, fig_wait, fig_care, fig_adm, fig_map
