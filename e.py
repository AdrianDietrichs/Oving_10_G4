# Øving 4, Oppgave e)
def differanse(input_list):
    liste = []  #Oppretter en tom liste
    n = int(input("Skriv inn antall tall du vil ha i listen din: "))
    for i in range(0, n):
        tall = int(input())
        liste.append(tall)
    diff = []
    for i in range(n-1):
        diff.append(liste[i+1]-liste[i])
    return diff

resultat = differanse(list)
print(resultat)








