from dash import html
from config import Colors

def data_dictionary():
    """
    Panel colapsable que muestra el diccionario de datos del dataset clinical_analytics.csv.

    Incluye la descripción de cada campo para facilitar la interpretación
    del dashboard sin afectar la visualización principal.
    """
    return html.Details([
        
        # 🔹 Título desplegable
        html.Summary(
            "📘 Descripción de los campos (clinical_analytics.csv)",
            style={
                "cursor": "pointer",
                "color": Colors["text"],
                "fontWeight": "600",
                "fontSize": "0.9rem",
                "marginBottom": "10px"
            }
        ),

        # 🔹 Lista de campos
        html.Ul([
            html.Li([
                html.B("Admit Source (Origen de la admisión): "),
                "El punto de origen de la visita del paciente (p. ej., Urgencias, derivación de clínica, sin cita previa)."
            ]),
            html.Li([
                html.B("Admit Type (Tipo de admisión): "),
                "Tipo de visita (p. ej., Urgencia, Programada, Urgente)."
            ]),
            html.Li([
                html.B("Appt Start Time (Hora de inicio de la cita): "),
                "Hora programada para la cita del paciente."
            ]),
            html.Li([
                html.B("Care Score (Puntuación de atención): "),
                "Métrica numérica que indica la satisfacción del paciente o la calidad de la atención."
            ]),
            html.Li([
                html.B("Check-In Time (Hora de llegada): "),
                "Hora real a la que el paciente llegó a la clínica."
            ]),
            html.Li([
                html.B("Clinic Name (Nombre de la clínica): "),
                "Nombre del centro o de la clínica especializada."
            ]),
            html.Li([
                html.B("Department (Departamento): "),
                "Departamento específico visitado (p. ej., Radiología, Pediatría)."
            ]),
            html.Li([
                html.B("Diagnosis Primary (Diagnóstico principal): "),
                "Afección principal o código de diagnóstico asignado a la visita."
            ]),
            html.Li([
                html.B("Discharge Datetime new (Fecha y hora de alta): "),
                "Fecha y hora en que finalizó la visita del paciente."
            ]),
            html.Li([
                html.B("Encounter Number (Número de consulta): "),
                "Identificador único de la visita específica."
            ]),
            html.Li([
                html.B("Encounter Status (Estado de la consulta): "),
                "Estado actual de la visita (p. ej., completada, cancelada, no se presentó)."
            ]),
            html.Li([
                html.B("Number of Records (Número de registros): "),
                "Normalmente un contador (1 por cada fila) para agregar el total de visitas."
            ]),
            html.Li([
                html.B("Wait Time Min (Tiempo de espera mínimo): "),
                "Diferencia calculada entre la hora de registro y la hora real de inicio del servicio (en minutos)."
            ]),
        ],
        style={
            "paddingLeft": "18px",
            "color": Colors["text"],
            "fontSize": "0.82rem",
            "lineHeight": "1.5"
        })

    ],
    style={
        "background": Colors["card"],
        "border": f"1px solid {Colors['border']}",
        "borderRadius": "12px",
        "padding": "14px",
        "marginTop": "12px"
    })