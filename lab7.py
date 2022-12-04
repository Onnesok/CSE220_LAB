
def keyidx(a):
    mx = a[0]
    mn = a[0]
    for i in range(len(a)):
        if mx < a[i]:
            mx = a[i]
        if mn > a[i]:
            mn = a[i]
    aux = [0] * (mx + (mn * -1) + 1)
    val = [0] * (mx + (mn * -1) + 1)
    for i in range(len(a)):
        if a[i] < 0:
            aux[a[i]-mn] += 1
        else:
            aux[a[i]-mn] += 1
    for i in range(len(aux)):
        indx = a[i] - mn # aux idx position
        cash = aux[indx]
        print(indx, a[i], cash)
        val[i] = aux[indx] * a[i]
    return val

a = [1,2,3,4,-2, -2,6,-1,5]
print(keyidx(a))