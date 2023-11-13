def leser_datafil():
    fil = open("Oving_10/snoedybder_vaer_en_stasjon_dogn.csv", "r")

    linjer = fil.readlines()

    liste = []

    for i in linjer:
        if i[0] == "#":
            i = ""
        data = i.strip().split(";")
        liste.append(data)
    print(liste[5])
    return liste

leser_datafil()

"""
Dataene starter fra liste[1], grunnet linje 1 i datafil er bare tekst
liste[i][0] = Navn
liste[i][1] = stasjonsid
osv...
"""