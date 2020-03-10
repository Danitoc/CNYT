import math


def sumaComplejos(num1, num2):
    com1 = num1[0] + num2[0]
    com2 = num1[1] + num2[1]
    return com1, com2


def restaComplejos(num1, num2):
    com1 = num1[0] - num2[0]
    com2 = num1[1] - num2[1]
    return com1, com2


def multiplicacionComplejos(num1, num2):
    val1 = num1[0] * num2[0]
    val2 = num1[0] * num2[1]
    val3 = num1[1] * num2[0]
    val4 = num1[1] * num2[1]
    res1 = val1 + val4 * -1
    res2 = val2 + val3
    return res1, res2


def division(num1, num2):
    dato1 = multiplicacionComplejos(num1, conjugado(num2))
    dato2 = complejoPorConjugado(num2)
    res = dato1[0] / dato2, dato1[1] / dato2
    return res


def modulo(num):
    res = math.sqrt(num[0] ** 2 + num[1] ** 2)
    return res


def conjugado(num):
    num = num[0], num[1] * -1
    return num


def complejoPorConjugado(num):
    dato1 = num[0] ** 2
    dato2 = ((num[1] ** 2) * -1) * -1
    res = dato1 + dato2
    return res


def cart_pola(num):
    p = math.sqrt(num[0] ** 2 + num[1] ** 2)
    ang = gradosRadianes(math.atan(num[1]/num[0]))
    res = p, ang
    return res


def pola_cart(num):
    p = num[0]
    ang = radianesGrados(num[1])
    res = p * math.cos(ang), p * math.sin(ang)
    return res


def fase(num):
    res = math.atan2(num[1], num[0])
    return res


def radianesGrados(num):
    return (num / 180) * math.pi


def gradosRadianes(num):
    return (num * 180) / math.pi


"""            Operaciones de vetores y matrices            """


def sumaVectores(vec1, vec2):
    res = [0] * len(vec1)
    if len(vec1) != len(vec2):
        print('La suma de vectores no es posible')
    else:
        for i in range(len(vec1)):
            res[i] = sumaComplejos(vec1[i], vec2[i])
        return res


def inversoAditivo(vec):
    for i in range(len(vec)):
        vec[i] = invertirSignos(vec[i])
    return vec


def escalarPorVector(num, vec):
    res = []
    for i in range(len(vec)):
        res.append(multiplicacionComplejos(num, vec[i]))
    return res


def sumaMatrices(mat1, mat2):
    res = [0] * len(mat1)
    if len(mat1) != len(mat2):
        print('No se pueden sumar las matrices')
    for i in range(len(mat1)):
        res[i] = sumaVectores(mat1[i], mat2[i])
    return res


def inversaAditivaMatriz(mat):
    res = [0] * len(mat)
    for i in range(len(mat)):
        res[i] = inversoAditivo(mat[i])
    return res


def prodTensorVect(vec1, vec2):
    res = []
    for i in range(len(vec1)):
        for j in range(len(vec2)):
            res.append(multiplicacionComplejos(vec1[i], vec2[j]))
    return res


def prodTensorMatr(mat1, mat2):
    tens = []
    for i in range(len(mat1)):
        for j in range(len(mat2)):
            tens.append(prodTensorVect(mat1[i], mat2[j]))
    return tens


def invertirSignos(com):
    pos1 = com[0] * - 1
    pos2 = com[1] * - 1
    return pos1, pos2


def probabilidad(pos, vec):
    num = modulo(vec[pos]) ** 2
    total = 0
    for i in range(len(vec)):
        total += modulo(vec[i]) ** 2
    return (num/total) * 100


def main():
    numero1 = (3, 2)
    numero2 = (6, 3)
    vector1 = [(2, 1), (-1, 2), (0, 1), (1, 0), (3, -1), (2, 0), (0, -2), (-2, 1), (1, -3), (0, -1)]
    vector2 = [(1, 2), (1, 1)]
    mat1 = [[(1, 0), (1, 0)], [(1, 0), (0, 0)]]
    mat2 = [[(3, 0), (4, 0)], [(2, 0), (1, 0)]]
    #multcomple = multiplicacionComplejos(numero1, numero2)
    #print(multcomple)
    #suma = sumaVectores(vector1, vector2)
    #producTensor = prodTensorVect(vector1, vector2)
    #producTensorMat = prodTensorMatr(mat1, mat2)
    #print(suma)
    #print(producTensor)
    #for i in producTensorMat:
    #print(i)
    #mod = modulo(numero1)
    #mod2 = modulo(nuemro2)
    #print(mod)
    #print(mod2)
    #con = conjugado(numero2)
    #print(con)
    #comConj = complejoPorConjugado(numero1)
    #print(comConj)
    #div = division(numero1, numero2)
    #print(div)
    #cartApolar = cart_pola(numero1)
    #print(cartApolar)
    #porlAcart = pola_cart(cartApolar)
    #print(porlAcart)
    #inver = inversoAditivo(vector1)
    #print(inver)
    #escalaVector = escalarPorVector(numero1, vector1)
    #print(escalaVector)
    prob = probabilidad(7, vector1)
    print(prob)
    """for i in range(len(mat1)):
        print(mat1[i])
    print()
    for i in range(len(mat2)):
        print(mat2[i])
    print()
    sumMat = sumaMatrices(mat1, mat2)
    for i in range(len(sumMat)):
        print(sumMat[i])
    print()
    invMat = inversaAditivaMatriz(sumMat)
    for i in range(len(invMat)):
        print(invMat[i])"""


main()
