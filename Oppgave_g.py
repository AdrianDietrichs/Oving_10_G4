from Oppgave_a import leser_datafil
from datetime import datetime
import matplotlib.pyplot as plt


data = leser_datafil()


result = [(j["Dato"], j["Skydekke"]) 
          for i in data
          for j in data[i]]
result = sorted(result, key=lambda a: a[0])


clearArray = []
control = []

currYear = result[0][0].year

validDays = 0
clearDays = 0

for i,v in enumerate(result):
    if currYear != result[i][0].year:
        currYear = result[i][0].year
        control.append(validDays)
        clearArray.append(clearDays)
        clearDays = 0
        validDays = 0

    if v[1] != None:
        if v[1] <= 3:
            clearDays += 1
            validDays += 1
        else:
            validDays += 1


y = []
x = []

for i,v in enumerate(clearArray):
    if control[i] >= 300:
        x.append(i+1980)
        y.append(v)

plt.plot(x,y)
plt.show()
