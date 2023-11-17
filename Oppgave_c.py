from Oppgave_b import years
from Del_1_g import minsteKvadratersMetode

y = years
x = [i for i in range(len(years))]

result = minsteKvadratersMetode(x,y)

if __name__ == "__main__":
    print(result)
    print("Trenden er: y = {:.2f}x + {:.2f}".format(result[0], result[1]))
