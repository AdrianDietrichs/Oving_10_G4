def minsteKvadratersMetode(x, y):
    n = len(x)
    upper = 0
    lower = 0

    xAverage = sum(x) / len(x)
    yAverage = sum(y) / len(y)

    for i in range(n):
        upper += (x[i] - xAverage) * (y[i] - yAverage)
        lower += (x[i] - xAverage) ** 2

    a = upper / lower
    b = yAverage - a * xAverage

    return a, b

# husk sett inn riktig data
years = [år 1, år 2, år 3, ]  # hvilke år det det er skiseong
skiDays = [90, 85, 100, 75, 110]  # hvor mange dager per år det er åpent


result = minsteKvadratersMetode(years, skiDays)


print("Trenden er: y = {:.2f}x + {:.2f}".format(result[0], result[1]))
