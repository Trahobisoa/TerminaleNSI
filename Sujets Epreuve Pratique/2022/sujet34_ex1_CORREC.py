def occurrence_max(chaine):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
    'q','r','s','t','u','v','w','x','y','z',' ']
    occurence = [0 for i in range(27)]
    for i in chaine:
        if i not in alphabet:
            return "La chaine ne doit contenir que des des lettres en minuscules et sans accent"
        occurence[alphabet.index(i)] += 1

    max = 0
    for k in occurence:
        if k > max:
            max = k

    return alphabet[occurence.index(max)]