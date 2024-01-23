# BAC 2023 Groupe 1 : Jour 1 : Exercice 3

# Structure de données abstraite : File

from random import randint

def creer_file_vide():
    #retourne une file vide
    return []

def est_vide(f):
    """ renvoie True si la file est vide
    False sinon """
    return f == []

def enfiler(f, element):
    #ajoute element à la file f
    f.append(element)
    return f

def defiler(f):
    #enleve et renvoie le premier element de la file
    assert not est_vide(f), "file vide"
    return f.pop(0)

def taille(f):
    #retourne la taille de la file
    return len(f)

# Question 1
def ajout(f):
    couleurs = ("bleu", "rouge", "jaune", "vert")
    indice = randint(0,3)
    enfiler(f,couleurs[indice])
    return f

# Question 2
def vider(f):
    for i in range(taille(f)):
        defiler(f)

# Question 3
def affich_seq(sequence):
    stock = creer_file_vide()
    ajout(sequence)
    while not est_vide(sequence) :
        c = defiler(sequence)
        affichage(c)
        time.sleep(0.5)
        enfiler(stock,c) 
    while not est_vide(stock) :
        enfiler(sequence,defiler(stock))

def tour_de_jeu(sequence):
    affich_seq(sequence)
    stock = creer_file_vide()
    while not est_vide(sequence) :
        c_joueur = saisie_joueur()
        c_seq = defiler(sequence)
        if c_joueur == c_seq:
            enfiler(stock,c_seq)
        else:
            vider(sequence)
    while not est_vide(stock):
        enfiler(sequence,defiler(stock))

def tour_de_jeu2(sequence):
    affich_seq(sequence)
    stock = creer_file_vide()
    longueur = taille(sequence)
    while not est_vide(sequence) :
        c_joueur = saisie_joueur()
        c_seq = defiler(sequence)
        if c_joueur == c_seq:
            enfiler(stock,c_seq)
        else:
            vider(sequence)
            
    if taille(stock) == longueur:
        while not est_vide(stock) :
            enfiler(sequence,defiler(stock))
        affich_seq(sequence)
        tour_de_jeu2(sequence)
    else:
        vider(sequence)
        affiche_seq(sequence)
        tour_de_jeu2(sequence)



f = creer_file_vide()

for i in range(5):
    couleurs = ("bleu", "rouge", "jaune", "vert")
    i = randint(0,3)
    enfiler(f,couleurs[i])

print(f)
a = defiler(f)
print(a)
print(f)
print(est_vide(f))

print(taille(f))

print(f)

print(enfiler(f,couleurs[randint(0,3)]))
