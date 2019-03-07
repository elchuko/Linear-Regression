dimx = 0
dimy = 0
mini = 0

def peque(a,b):
    if a > b:
        return b
    elif a < b:
        return a
    else:
        return a

def adic(l1, l2):
    ln = [0]*len(l1)
    for i in range(len(l1)):
        ln[i] = l1[i] + l2[i]
    return ln

def multi(l1, k):
    ln = [0]*len(l1)
    for i in range(len(l1)):
        ln[i] = k * l1[i]
    return ln

def swap_finder(m, l, x):
    if l == (x-1):
        print("creo que no funciona")
        return m, False
    else:
        for i in range(l, x):
            if m[i][l] != 0:
                m[l], m[i] = m[i], m[l]
                return m, True
        print("creo que tampoco funciona")
        return m, False

def solver(m,p):
    for i in range(p):
        boo = True
        if m[i][i] == 0:
            m, boo = swap_finder(m, i, p)
        if boo:
            m[i] = multi(m[i], 1/float(m[i][i]))
        else:
            return m
        for j in range(i+1,len(m)):
            m[j] = adic(m[j], multi(m[i], -1*float(m[j][i])))
    for k in range(p-1, -1, -1):
        for l in range(k-1, -1, -1):
            m[l] = adic(m[l], multi(m[k], -1*float(m[l][k])))
    return m

def gauss_jordan(matrix):
    columns = len(matrix[0])
    rows = len(matrix)

    mini=peque(columns,rows)
    return solver(matrix,mini)

