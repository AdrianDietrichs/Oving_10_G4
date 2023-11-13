def ListeIFTVerdi(a,b):
    resultat = 0
    for i in range(len(a)):
        if a[i] > b:
            resultat += 1
        
    return resultat
