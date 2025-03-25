from sympy import Rational

def print_matrix(M, decimals=3):
    for row in M:
        print([round(x, decimals) + 0 for x in row])

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
                    raise ValueError("Matriz singular : (")
        for i in range(fd + 1, n):
            crScaler = AM[i][fd] / AM[fd][fd]
            for j in range(n):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
    product = 1.0
    for i in range(n):
        product *= AM[i][j]
    return product

def verifica_nao_singularidade(A):
    try:
        det = determinant(A)
        if det != 0:
            return True
        else:
            raise ArithmeticError("Matriz singular : (")
    except ArithmeticError as e:
        print(f"Erro: {e}")

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
            raise ValueError("Não deu certo")
        if augMat[i][i] != 1:
            divisor = augMat[i][i]
            for k in range(m):
                augMat[i][k] = Rational(augMat[i][k], divisor)
        else:
            pass
        #Zerando as entradas do pivô
        for j in range(n):
            if i!=j:
                coef = augMat[j][i]
                for k in range(m):
                    augMat[j][k] -= coef * augMat[i][k]
            else:pass
    return augMat
       
class GaussJordanClass:
    def __init__(self, augMat):
        self.augMat = augMat

    def resolverSL(self):
        mc = coef_matrix(self.augMat)
        if verifica_nao_singularidade(mc):
            print("Tudo certo!")

            self.augMat = GaussJordanMethod(self.augMat)
            print(self.augMat)
        else:
            print("Não foi possível aplicar o método de Gauss Jordan...")

# Sistema a)
a = [
    [2.0, 3.0, 5.0],  # 2x + 3y = 5
    [4.0, -1.0, 7.0]  # 4x - y = 7
]

# Sistema b)
b = [
    [2, 3, 1, 0],   # 2x + 3y + z = 0
    [1, -2, -1, 1], # x - 2y - z = 1
    [1, 4, 1, 2]    # x + 4y + z = 2
]

# Sistema c)
c = [
    [2, 2, -3, 4],  # 2x + 2y - 3z = 4
    [1, 3, 1, 11],  # x + 3y + z = 11
    [2, 5, -4, 13]  # 2x + 5y - 4z = 13
]

# Sistema d)
d = [
    [1, 1, 1, 1],   # x + y + z = 1
    [1, -1, 1, 2],  # x - y + z = 2
    [2, 2, 2, 5]    # 2x + 2y + 2z = 5
]

# Sistema e)
e = [
    [1, 1, 1, 1],   # x + y + z = 1
    [1, -1, 1, 2],  # x - y + z = 2
    [2, 0, 2, 3]    # 2x + 2z = 3
]

# Sistema f)
f = [
    [2, 1, -2, 10],  # 2x + y - 2z = 10
    [3, 2, 2, 1],    # 3x + 2y + 2z = 1
    [5, 4, 3, 4]     # 5x + 4y + 3z = 4
]

GJCa = GaussJordanClass(a)
GJCb = GaussJordanClass(b)
GJCc = GaussJordanClass(c)
GJCd = GaussJordanClass(d)
GJCe = GaussJordanClass(e)
GJCf = GaussJordanClass(f)
print("BATERIA DE TESTES!")
print("a)")
GJCa.resolverSL()
print("b)")
GJCb.resolverSL()
print("c)")
GJCc.resolverSL()
print("d)")
GJCd.resolverSL()
print("e)")
GJCe.resolverSL()
print("f)")
GJCf.resolverSL()