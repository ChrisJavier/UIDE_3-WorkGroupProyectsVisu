from dash import html, dcc

## Importar modulos

from config import Colors
def layout_popup_welcome():

    return html.Div([
        dcc.Store(id="show-modal", data=True),  # controla si se muestra

        html.Div(
            id="modal",
            children=[
                html.Div([
                    html.H3("Bienvenido 👋 a nuestro Trabajo 3: Ejercicio de Aplicacion Autónoma", style={"marginBottom": "10px"}),
                    html.H4("📋 Información del Proyecto", style={"marginTop": "10px"}),
                    html.Div([
                        html.P("Autores:", style={"fontWeight": "600"}),

                        html.Ul([
                            html.Li("CARRERA DIAZ CHRISTIAN JAVIER"),
                            html.Li("CERNA PACHECO ROMEL MICHAEL"),
                            html.Li("LUNA ARTEAGA ALEXANDER PAUL"),
                        ], style={"paddingLeft": "20px"}),

                        html.P("Versión: 1.0.0"),
                        html.P("Licencia: MIT"),
                        html.P("No olvides ingresar a nuestro Git para revisar la fuente 👇"),
                    ]),
                    html.A(
                        html.Img(
                            src="/assets/25231.png",
                            className="logo-hover",
                            title="Ver repositorio en GitHub",
                            style={
                                "height": "80px",  # más grande
                                "display": "block",
                                "margin": "0 auto"  # centrado horizontal
                            }
                        ),
                        href="https://github.com/ChrisJavier/UIDE_3-WorkGroupProyectsVisu/tree/main/Week3",
                        target="_blank"
                    ), 
                    html.Button("Entrar", id="close-modal", style={
                            "marginTop": "20px",  # separación con la imagen
                            "padding": "8px 16px",
                            "border": "none",
                            "borderRadius": "6px",
                            "background": Colors["primary"],
                            "color": "white",
                            "cursor": "pointer",
                            "display": "block",
                            "marginLeft": "auto",
                            "marginRight": "auto"  # centrar botón
                    })
                ], style={
 "background": "#1e293b",
    "padding": "25px",
    "borderRadius": "12px",
    "textAlign": "left",
    "color": "white",
    "width": "350px",
    "boxShadow": "0 10px 30px rgba(0,0,0,0.5)"
                })
            ],
            style={
                "position": "fixed",
                "top": "0",
                "left": "0",
                "width": "100%",
                "height": "100%",
                "background": "rgba(0,0,0,0.6)",
                "display": "flex",
                "justifyContent": "center",
                "alignItems": "center",
                "zIndex": "9999"
            }
        )
    ])