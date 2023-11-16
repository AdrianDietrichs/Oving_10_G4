from datetime import datetime
from Del_1_f import longestZeroSequence
from Oppgave_a import leser_datafil
import matplotlib.pyplot as plt

data = leser_datafil()

result = []

for i in data:
    weather = [j["Nedbor"] for j in data[i] if j["Nedbor"] != None]

    if len(weather) >= 300:
        result.append(weather)
    else:
        result.append(None)

for i in range(len(result)):
    result[i] = longestZeroSequence(result[i]) if result[i] != None else None


if __name__ == "__main__":
    x = [i+1980 for i in range(len(result)) if result[i] != None]
    y = [i for i in result if i != None]

    plt.plot(x, y)
    plt.show()
