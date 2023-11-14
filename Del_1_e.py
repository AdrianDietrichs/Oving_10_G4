# Øving 4, Oppgave e)
def differanse(x: list, y:list):
    diff = []
    for i in range(len(x)-1):
        h = (x[i+1]-x[i])
        f = y[i]
        fxh = y[i+1]
        diff.append((fxh - f)/h)
    return diff

ListeX = [1,2,3,4,5,6]
ListeY = [1,4,9,16,25,36]

resultat = differanse(ListeX,ListeY)
print(resultat)