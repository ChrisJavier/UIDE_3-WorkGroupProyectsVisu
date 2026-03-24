
# Callbacks — Departamentos ──────────────────────────────────────────────────
# Importar librerias
from dash import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Importar módulos
from config import Colors, LAYOUT_BASE
from data import CLINICS

def register_callbacks(app, df, filt):
    """
    Registra los callbacks de la vista de departamentos.

    Genera:
    - Volumen de consultas por departamento
    - Heatmap de departamento vs clínica
    - Care score promedio
    - Relación entre tiempo de espera y calidad (scatter)

    Incluye manejo de:
    - Filtros dinámicos
    - Datos vacíos
    - Estructuras pivotadas
    """
    # ── Callbacks — Departamentos ──────────────────────────────────────────────────
    @app.callback(
        [Output("d-vol","figure"), Output("d-heat","figure"),
        Output("d-care","figure"), Output("d-scat","figure")],
        [Input("dp-dep","value"), Input("at-dep","value"), Input("cl-dep","value")],
    )
    
    def cb_departamentos(dp, at, cl):
        dff = filt(df.copy(), dp, at, cl)

        # --- Gráfico 1: Volumen por departamento ---
        if dff.empty:
            empty = go.Figure()
            empty.update_layout(**LAYOUT_BASE, title="Sin datos para los filtros seleccionados")
            return empty, empty, empty, empty

        df_vol = dff["Department"].value_counts().reset_index()
        df_vol.columns = ["Department", "Encounters"]
        fig_vol = px.bar(df_vol, x="Encounters", y="Department", orientation="h",
                        title="Volumen de Consultas por Departamento", 
                        labels={
                                "Encounters": "N° Consultas",
                                "Department": "Especialidad"
                            },                        
                        color="Encounters",
                        color_continuous_scale=[Colors["primary"], Colors["success"]])
        fig_vol.update_layout(**LAYOUT_BASE, coloraxis_showscale=False)
        fig_vol.update_yaxes(categoryorder="total ascending", gridcolor=Colors["border"])

        # --- Gráfico 2: Heatmap departamento x clínica (pivot_table es más robusto que pivot) ---
        try:
            heat = dff.pivot_table(
                index="Department", columns="Clinic Name",
                values="Encounter Number", aggfunc="count", fill_value=0
            )
            # Aseguramos que todas las clínicas aparezcan aunque no tengan datos
            for clinic in CLINICS:
                if clinic not in heat.columns:
                    heat[clinic] = 0
            heat = heat[sorted(heat.columns)]
            fig_heat = go.Figure(go.Heatmap(
                z=heat.values,
                x=heat.columns.tolist(),
                y=heat.index.tolist(),
                colorscale=[[0, Colors["card"]], [0.01, "#2a2d3e"], [1, Colors["primary"]]],
                text=heat.values.astype(int),
                texttemplate="%{text}",
                hoverongaps=False,
            ))
            fig_heat.update_layout(**LAYOUT_BASE, title="Consultas: Departamento × Clínica")
        except Exception:
            fig_heat = go.Figure()
            fig_heat.update_layout(**LAYOUT_BASE, title="Heatmap no disponible con estos filtros")

        # --- Gráfico 3: Care Score promedio por departamento ---
        df_care = (dff.groupby("Department")["Care Score"]
                .mean().round(2).reset_index()
                .sort_values("Care Score", ascending=False))
        fig_care = px.bar(df_care, x="Department", y="Care Score",
                      labels={
                                "Care Score": "Puntaje de Atención",
                                "Department": "Especialidad"
                            },                            
                        title="Care Score Promedio por Departamento", color="Care Score",
                        color_continuous_scale=[Colors["danger"], Colors["warning"], Colors["success"]])
        fig_care.update_layout(**LAYOUT_BASE, xaxis_tickangle=-30, coloraxis_showscale=False)

        # --- Gráfico 4: Scatter espera vs care score ---
        df_score = dff.groupby("Department").agg(
            Wait=("Wait Time Min", "mean"),
            Care=("Care Score", "mean"),
            Count=("Number of Records", "sum")
        ).reset_index()
        # size necesita valores > 0
        df_score["Count"] = df_score["Count"].clip(lower=1)
        fig_scat = px.scatter(df_score, x="Wait", y="Care", 
                            labels={
                                "Care": "Puntaje de Atención",
                                "Wait": "Tiempo de Espera"
                            },                                  
                            text="Department", size="Count",
                            title="Espera vs Care Score por Departamento",
                            color_discrete_sequence=[Colors["primary"]])
        fig_scat.update_traces(textposition="top center", textfont_size=9)
        fig_scat.update_layout(**LAYOUT_BASE)

        return fig_vol, fig_heat, fig_care, fig_scat
