def moyenne(tab):
    s_valeur = 0
    s_coef = 0
    for v in tab:
        s_valeur = s_valeur + v[0]*v[1]
        s_coef = s_coef + v[1]
    if s_coef == 0:
        return None
    else :
        return s_valeur/s_coef