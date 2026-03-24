# Callbacks — Tiempos de Espera ─────────────────────────────────────────────
# Importar librerias
from dash import Input, Output
import plotly.express as px

# Importar módulos
from config import Colors, LAYOUT_BASE

def register_callbacks(app, df, filt):
    """
    Registra los callbacks de la vista de tiempos de espera.

    Genera:
    - Histograma de tiempos de espera
    - Boxplot por departamento
    - Gráfico de espera promedio

    Aplica filtros dinámicos por:
    - Departamento
    - Tipo de admisión
    - Clínica
    """
    @app.callback(
        [Output("e-hist","figure"), Output("e-box","figure"), Output("e-bar","figure")],
        [Input("dp-esp","value"), Input("at-esp","value"), Input("cl-esp","value")],
    )
    def cb_espera(dp, at, cl):
        dff = filt(df.copy(), dp, at, cl)

        fig_hist = px.histogram(dff, x="Wait Time Min", 
                                nbins=40, 
                                color="Admit Type",
                                title="Distribución de Tiempos de Espera",
                                labels={
                                    "Wait Time Min": "Tiempo de espera en minutos"
                                },                                
                                barmode="overlay", 
                                opacity=0.75)
        fig_hist.update_layout(**LAYOUT_BASE,yaxis_title="Cantidad de atenciones")

        df_top8 = dff["Department"].value_counts().head(8).index.tolist()
        fig_box = px.box(dff[dff["Department"].isin(df_top8)],
                        x="Department", 
                        y="Wait Time Min", 
                        labels={
                            "Wait Time Min": "Tiempo de espera en minutos",
                            "Department": "Especialidad"
                        },                           
                        color="Department",
                        title="Distribución de Espera por Departamento (Top 8)")
        fig_box.update_layout(**LAYOUT_BASE, showlegend=False, xaxis_tickangle=-30)

        df_avg = (dff.groupby("Department")["Wait Time Min"]
                .mean().round(1).reset_index()
                .sort_values("Wait Time Min", ascending=False))
        df_avg.columns = ["Department","Avg Wait"]
        fig_bar = px.bar(df_avg, x="Department", 
                         y="Avg Wait",
                         title="Espera Promedio por Especialidad", 
                         labels={
                            "Avg Wait": "Promedio de tiempo de espera",
                            "Department": "Especialidad"
                         },                          
                         color="Avg Wait",
                         color_continuous_scale=[Colors["success"], Colors["warning"], Colors["danger"]])
        fig_bar.update_layout(**LAYOUT_BASE, xaxis_tickangle=-30, coloraxis_showscale=False)

        return fig_hist, fig_box, fig_bar
