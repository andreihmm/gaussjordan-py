# gauss_jordan.py

matrix = [[1.0,2.0,-4.0,3.0],[2.0,3.0,3.0,15.0],[5.0,-3,1.0,14.0]]
matrixComZero = [[],[],[],[]]

def print_matrix(M,decimals = 3):
    for row in M:
        print([round(x, decimals)+0 for x in row])

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



        
GaussJordanMethod(matrix)
