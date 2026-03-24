import os
import pandas as pd

# ── Ruta del CSV ───────────────────────────────────────────────────────────────
# Opción 1: CSV en la misma carpeta que este script (recomendado)
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "clinical_analytics.csv")
# Opción 2: ruta absoluta — descomenta y edita:
# CSV_PATH = r"C:\Users\alvar\OneDrive\Documentos\clinical_analytics.csv"

# ── Data ───────────────────────────────────────────────────────────────────────
df = pd.read_csv(CSV_PATH)
df["Check-In Time"] = pd.to_datetime(df["Check-In Time"], format="mixed")
df["Month"]         = df["Check-In Time"].dt.month
df["Month Label"]   = df["Check-In Time"].dt.strftime("%b")

MONTH_ORDER = ["Jan","Feb","Mar","Apr","May","Jun",
               "Jul","Aug","Sep","Oct","Nov","Dec"]
DEPARTMENTS = sorted(df["Department"].unique())
CLINICS     = sorted(df["Clinic Name"].unique())
ADMIT_TYPES = [t for t in sorted(df["Admit Type"].unique())
               if t != "Information not Available"]