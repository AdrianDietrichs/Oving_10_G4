def minsteKvadratersMetode(x: list, y: list):
    n = len(x)

    upper = 0
    lower = 0

    xAverage = sum(x) / len(x)
    yAverage = sum(y) / len(y)

    for i in range(n):
        upper += (x[i]-xAverage)*(y[i]-yAverage)
        lower += (x[i]-xAverage)**2

    a = upper / lower
    b = yAverage - a * xAverage

    return (a,b)

print(minsteKvadratersMetode([1,2,3,4,5],[1,2,3,4,5]))
