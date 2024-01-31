def  occurence_lettres(phrase):
    """
  Fonction qui compte les occurences de chaque caractère dans une phrase
  @param phrase : chaine de caracteres (str)
  @return dico : dictionnaire contenant les lettres (clés) et les occurences respectives (valeurs)
    """

    dico = {}

    for l in phrase:

        if l not in dico:
            dico[l] = 1
        else :
            dico[l] = dico[l]+1

    return dico

dict = occurence_lettres("Hello world! ")


print(dict)
print(dict.keys())
print(dict.values())