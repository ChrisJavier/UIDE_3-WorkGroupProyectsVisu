# ***** Prueba data *****
#from data import df

#print(df.head())

# ***** Prueba config *****
#from config import Colors

#print(Colors["primary"])

# ***** prueba Utils *****

#from data import df
#from utils import filt
#print(filt(df, None, None, None).shape)

# ***** Prueba de componentes interfaz grafica *****
#from components.ui_components import card
#print(card("test"))

# ***** Prueba de sidebar *****
#from components.sidebar import sidebar

#print(sidebar("gen"))

# ***** Prueba de navbar *****
#from components.navbar import create_navbar
#print("Prueba de navbar")
#print(create_navbar())

# ***** Prueba de pagina Vision General
#from pages.general import layout_general
#print("Prueba de layout de Vision General")
#print(layout_general())

from pages.espera import layout_espera
print("Prueba de layout de espera")
print(layout_espera())

from pages.departamentos import layout_departamentos
print("Prueba de layout de departamentos")
print(layout_departamentos())

from pages.tendencia import layout_tendencia
print("Prueba de layout de tendencia")
print(layout_tendencia())

# ***** Prueba general_cb ******
#print("Prueba de general_cb")
#from callbacks.general_cb import register_callbacks

#print("Prueba de espera_cb")
#from callbacks.espera_cb import register_callbacks

#print("Prueba de departamentos_cb")
#from callbacks.departamentos_cb import register_callbacks

#print("Prueba de tendencia_cb")
#from callbacks.tendencia_cb import register_callbacks