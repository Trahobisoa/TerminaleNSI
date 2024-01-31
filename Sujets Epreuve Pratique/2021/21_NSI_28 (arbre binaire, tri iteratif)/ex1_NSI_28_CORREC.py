def taille(arbre,lettre):
    """
    Fonction
    """

    if arbre[lettre][0]!="" and arbre[lettre][1]!="":
        return 1+taille(arbre,arbre[lettre][0])+taille(arbre,arbre[lettre][1])
    elif arbre[lettre][0]=="" and arbre[lettre][1]!="":
        return 1+taille(arbre,arbre[lettre][1])
    elif arbre[lettre][0]!="" and arbre[lettre][1]=="":
        return 1+taille(arbre,arbre[lettre][0])
    else :
        return 1


a= {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'],'H':['','']}
