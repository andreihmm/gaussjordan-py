# gauss_jordan.py


def print_matrix(M,decimals = 3):
    for row in M:
        print([round(x, decimals)+0 for x in row])

def zeros_matrix(rows, cols):
    M=[]
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M

def coef_matrix(augMat):
    rows = len(augMat)
    cols = len(augMat[0])

    MC = zeros_matrix(rows, cols-1)

    for i in range(rows):
        for j in range(cols-1):
            MC[i][j] = augMat[i][j]

    return MC

def determinant(AM):
    n = len(AM)

    for fd in range(n):
        if AM[fd][fd] == 0:
            for j in range(fd + 1, n):
                if AM[j][fd] != 0:
                    AM[fd], AM[j] = AM[j], AM[fd]
                    break
                else:
                    raise ValueError("Matriz singular hell nawww")

        for i in range(fd + 1, n):
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]

    product = 1.0
    for i in range(n):
        product *= AM[i][j]
    return product

def verifica_nao_singularidade(A):
    det = determinant(A)
    if det != 0:
        return True
    else:
        raise ArithmeticError("Matriz singular hell naww")

def GaussJordanMethod(augMat):
    #Normalizando cada linha...
    #L_i <- L_i / a_ii

    n=len(augMat)
    m=len(augMat[0])

    for i in range(n):

        if augMat[i][i] == 0:
            for j in range(i + n, n):
                augMat[i], augMat[j] = augMat[j], augMat[i]
                break
            raise ValueError("NAAAAAAAAAAAOOOOO")

        if augMat[i][i] != 1:
            divisor = augMat[i][i]
            for k in range(m):
                augMat[i][k] /= divisor
        else:
            pass

        #Zerando as entradas do pivô

        for j in range(n):
            if i!=j:
                coef = augMat[j][i]
                for k in range(m):
                    augMat[j][k] -= coef * augMat[i][k]
            else:pass
       
    print_matrix(augMat)



        
matrix = [[2.0,2.0,-3.0,4.0],[1.0,3.0,1.0,11.0],[2.0,5,-4.0,13.0]]

mc = coef_matrix(matrix)
print_matrix(mc)
result = verifica_nao_singularidade(mc)
print(result)
GaussJordanMethod(matrix)