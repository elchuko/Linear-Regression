dimx = 0
dimy = 0
mini = 0


def error_test2(x):
    try:
        int(x)
        return False
    except:
        return True


def error_test3(x):
    try:
        float(x)
        return False
    except:
        return True

# Revision general
def error_test(y, z=1):
    if z == 1:
        while error_test2(y):
            print("\n\n\t\tERROR!!!\n\t\tSe han ingresado valores o caracteres no validos.")
        return int(y)
    elif z == 2:
        while error_test3(y):
            print ("\n\n\t\tERROR!!!\n\t\tSe han ingresado valores o caracteres no validos.")
        return float(y)

def generador(y,x):
    mat = []
    for k in range(y):
        mat.append([])
    for i in range(y):
        for j in range(x):
            print
            mat[i].append(error_test(raw_input("a_" + str(i+1) + str(j+1) + " = "), 2))
    return mat

def impri(m):
    print("\n")
    print("\t||" + ("\t" * (len(m[0]) + 1)) + "||")
    for i in range(len(m)):
        print("\t||\t"),
        print("||")
        print("\t||" + ("\t" * (len(m[0]) + 1)) + "||")
    print("\n")

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
        print("La matriz es una matriz singular.")
        print("Eso implica que no se puede resolver.\n\n")
        return m, False
    else:
        for i in range(l, x):
            if m[i][l] != 0:
                m[l], m[i] = m[i], m[l]
                return m, True
        print("La matriz es una matriz singular.")
        print("Eso implica que no se puede resolver.\n\n")
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

