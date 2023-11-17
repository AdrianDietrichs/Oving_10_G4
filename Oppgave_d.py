from Oppgave_b import dager, years
from Oppgave_c import result
import matplotlib.pyplot as plt

def f(x, ab):
    a,b = ab
    return a*x+b

x1 = [i for i in range(1980,2023)]
y1 = [f(i, result) for i in range(0,43)]
plt.plot(x1,y1)

x2 = []
y2 = []

for i, v in enumerate(years):
    if dager[i] >= 200:
        x2.append(i+1980)
        y2.append(v)

plt.plot(x2,y2)
plt.show()



