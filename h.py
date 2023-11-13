liste = [2,3,4,5,7,10,2,19]

def VoksendePlante(a):
    sum = 0
    for i in range(len(a)):
        if a[i] > 5:
            sum += a[i]-5
    return sum

print("Total vekst: ",VoksendePlante(liste))
