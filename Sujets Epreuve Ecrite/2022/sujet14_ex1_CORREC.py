def correspond(mot, mot_a_trous):
    i = 0
    n = len(mot)
    m = len(mot_a_trous)
    if n != m :
        return False
    for i in range(n):
        if mot_a_trous[i] != '*':
            if mot[i] != mot_a_trous[i]:
                return False
    return True