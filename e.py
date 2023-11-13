# Øving 4, Oppgave e)
def differanse(liste: list):
    diff = []
    for i in range(len(liste)-1):
        diff.append(liste[i+1]-liste[i])
    return diff

n = int(input("Skriv inn antall tall du vil ha i listen din: "))

liste = []
for i in range(n):
    tall = int(input())
    liste.append(tall)

resultat = differanse(liste)
print(resultat)
