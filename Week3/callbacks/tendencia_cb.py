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
                          labels={
                           "Month Label": "Mes",
                           "Encounters": "Consultas"
                          },                            
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
                           labels={
                            "Month Label": "Mes",
                            "Wait Time Min": "Tiempo de espera en minutos"
                           },                                
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
                           labels={
                            "Month Label": "Mes",
                            "Care Score": "Puntaje de Atención"
                           },  
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

        # Vamos a realizar un mapa con las clinicas que tienen mayor tiempo de atencion 
        # Agregamos las coordenas de acuerdo a google maps
        coords_df = pd.DataFrame({
        "Clinic Name": ["Lakeview Center", "Madison Center", "Surgery Center"],
        "lat": [41.8781, 43.0731, 34.0522],
        "lon": [-87.6298, -89.4012, -118.2437]
        })

        dff = dff.merge(coords_df, on="Clinic Name", how="left")
        dff["Wait Time Min"] = dff["Wait Time Min"].clip(lower=0)

        # Agrupación segura (Wait Time y Patients al mismo tiempo) Pacientes con el numero de atencion
        # Aunque no tenemos informacion del paciente tenemos el id de la consulta que nos sirve
        df_map = dff.groupby(["Clinic Name", "lat", "lon"]).agg(
        **{"Wait Time Min": pd.NamedAgg(column="Wait Time Min", aggfunc="mean")},
        Patients=pd.NamedAgg(column="Encounter Number", aggfunc="count")
        ).reset_index()

        # Creamos una nueva columna de categoria por tiempo de espera
        df_map["Category"] = pd.cut(
        df_map["Wait Time Min"],
        bins=[0, 20, 40, 100],
        labels=["Bajo", "Medio", "Alto"]
        )

        # Dibujamos el mapa
        fig_map = px.scatter_mapbox(
        df_map,
        lat="lat",
        lon="lon",
        color="Wait Time Min",
        size="Wait Time Min",
        zoom= 3 ,
        labels={
        "Wait Time Min": "Tiempo de espera en minutos"
        },         
        title="Mapa de Estados Unidos con ubicación de las clinicas y su mayor tiempo de atención",
        hover_data={
                "Wait Time Min": True,
                "Patients": True
        },
        hover_name="Clinic Name"
        )

        # Tenemos el peor tiempo de consulta maximo dentro de las 3 clinicas
        worst = df_map.loc[df_map["Wait Time Min"].idxmax()]

        fig_map.add_scattermapbox(
        lat=[worst["lat"]],
        lon=[worst["lon"]],
        mode='markers+text',
        marker=dict(size=10, color='blue'),
        text=["⚠️ Mayor espera"],
        textposition="top center",
        name="Clínica con mayor espera"
        )

        fig_map.update_layout(    
            mapbox_style="open-street-map",
                paper_bgcolor=Colors["bg"],
                font=dict(color="white"),
                margin=dict(l=0, r=0, t=30, b=0),
                legend=dict(
                yanchor="top",
                y=0.95,       
                xanchor="left",
                x=0.02,       
                bgcolor="rgba(0, 0, 0, 0.5)", 
                bordercolor="white",
                borderwidth=1
        ))

        return fig_vol, fig_wait, fig_care, fig_adm, fig_map
