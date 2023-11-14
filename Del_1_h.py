def VoksendePlante(a):
    sum = 0
    for i in range(len(a)):
        if a[i] != None and a[i] > 5:
            sum += a[i]-5
    return sum
