def xor(bin1, bin2):
    """Fonction qui effectue le OU EXCLUSIF sur deux nombres binaires passés en paramètres
        @param : bin1, bin2 listes d'entiers représentants 2 nombres binaires
        @return : result liste d'entiers représentant un nombre binaire
    """
    result = []
    
    for i in range(len(bin1)):
        
        if bin1[i] == bin2[i]:
            result.append(1)
        else:
            result.append(0)
            
    return result

a = [1,0,1,0,1,1,0,1]
b = [0,1,1,1,0,1,0,0]
c = [1,1,0,1]
d = [0,0,1,1]

print(xor(a,b))
print(xor(c,d))