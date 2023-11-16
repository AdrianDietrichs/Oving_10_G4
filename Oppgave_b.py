from Oppgave_a import leser_datafil
from datetime import datetime
from Del_1_d import ListeIFTVerdi

data = leser_datafil()

result = [(j["Dato"], j["Snodybde"]) 
          for i in data
          for j in data[i]]

result = sorted(result, key=lambda a: a[0])

sesonger = []
i = 0
while i < len(result):
    if result[i][0].month == 10:
        sesong = []
        while result[i][0].month != 6:
            sesong.append(result[i])
            i+=1
        sesonger.append(sesong)
    else:
        i += 1

years = []
for i in sesonger:
    years.append(ListeIFTVerdi([j[1] for j in i if j[1]], 20))

if __name__ == "__main__":
    _ = [print(str(years[i-1980])+" dager mellom "+str(i)+"-"+str(i+1))
         for i in range(1980,2023)]

for a,i in enumerate(sesonger):
    print(years[a])
    for j in i:
        print(j[0], j[1])
    print("")

