# ── Callbacks — Vista General ──────────────────────────────────────────────────

# Importar librerias
from dash import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Importar módulos
from config import Colors, LAYOUT_BASE

def register_callbacks(app, df, filt):
    """
    Registra los callbacks de la vista general.

    Maneja:
    - Gráfico de clínicas (pie)
    - Fuente de admisión
    - Estado de consultas
    - Distribución de care score

    Aplica filtros dinámicos según selección del usuario.
    """
    # ── Callbacks — Vista General ──────────────────────────────────────────────────
    @app.callback(
        [Output("g-pie","figure"), Output("g-src","figure"),
        Output("g-sta","figure"), Output("g-care","figure")],
        [Input("dp-gen","value"), Input("at-gen","value"), Input("cl-gen","value")],
    )
    def cb_general(dp, at, cl):
        dff = filt(df.copy(), dp, at, cl)

        df_vc = dff["Clinic Name"].value_counts().reset_index()
        df_vc.columns = ["Clinic","N"]
        fig_pie = go.Figure(
            go.Pie(
                labels=df_vc["Clinic"], 
                values=df_vc["N"], 
                hole=0.55,
                marker_colors=[Colors["primary"], 
                               Colors["success"], 
                               Colors["warning"]],
                               textinfo="percent+label")
                               )
        fig_pie.update_layout(**LAYOUT_BASE, title="Consultas por Clínica", showlegend=False)

        df_src = dff["Admit Source"].value_counts().head(6).reset_index()
        df_src.columns = ["Source","Count"]
        fig_src = px.bar(df_src, y="Source", x="Count", orientation="h",
                        title="Fuente de Admisión (Top 6)",
                        color_discrete_sequence=[Colors["primary"]])
        fig_src.update_layout(**LAYOUT_BASE)
        fig_src.update_yaxes(categoryorder="total ascending")

        df_st = dff["Encounter Status"].value_counts().reset_index()
        df_st.columns = ["Status","Count"]
        col_map = [Colors["success"] if "Discharged" in s else
                Colors["danger"]  if s == "Cancelled" else Colors["warning"] for s in df_st["Status"]]
        fig_st = go.Figure(go.Bar(x=df_st["Status"], 
                                  y=df_st["Count"], 
                                  marker_color=col_map))
        fig_st.update_layout(**LAYOUT_BASE, title="Estados de la Consulta")

        fig_care = px.histogram(dff, x="Care Score", 
                                nbins=9,
                                title="Distribución del Care Score",
                                color_discrete_sequence=[Colors["success"]])
        fig_care.update_layout(**LAYOUT_BASE)

        return fig_pie, fig_src, fig_st, fig_care