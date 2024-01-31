# Créé par trahobisoa, le 03/02/2023 en Python 3.7

def recherche (tab, n):
    deb = 0
    fin = len(tab)-1
    indice = -1
    while deb <= fin and indice == -1:
        mil = (deb+fin)//2
        if tab[mil] == n:
            indice = mil
        elif n > tab[mil]:
            deb = mil + 1
        else :
            fin = mil - 1
    return indice
