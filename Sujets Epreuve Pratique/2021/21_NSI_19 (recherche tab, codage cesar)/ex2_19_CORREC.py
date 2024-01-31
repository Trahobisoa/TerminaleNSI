# Créé par trahobisoa, le 03/02/2023 en Python 3.7


ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat

