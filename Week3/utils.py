# Filtros

def filt(dff, dp, at, cl):
    if dp: dff = dff[dff["Department"].isin(dp)]
    if at: dff = dff[dff["Admit Type"].isin(at)]
    if cl: dff = dff[dff["Clinic Name"].isin(cl)]
    return dff