from Oppgave_a import leser_datafil
import matplotlib.pyplot as plt

data = leser_datafil()

result = []
for i in data:
    wind = [j["Hoyeste_middelvind"] for j in data[i] if j["Hoyeste_middelvind"] != None]

    if len(wind) >= 300:
        result.append(wind)
    else:
        result.append(None)


def median(array: list):
    if len(array)%2 == 1: 
        return array[(len(array)//2)]
    a1 = array[len(array)//2]
    a2 = array[(len(array)//2)-1]
    return (a1+a2)/2

#print(median([1,2,3]))
#print(median([1,1,1,5,6,1,1,1]))
#print(median([1,1,1,1,10,1,1,1,1]))

for i,v in enumerate(result):
    if v == None: continue
    result[i] = median(v)

if __name__ == "__main__":
    x = [i+1980 for i in range(len(result)) if result[i] != None]
    y = [i for i in result if i != None]

    plt.plot(x, y)
    plt.show()
