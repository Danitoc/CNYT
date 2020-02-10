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
    res = dato1[0]/dato2, dato1[1]/dato2
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


# def fase():


def radianesGrados(num):
    return (num / 180) * math.pi


def gradosRadianes(num):
    return (num * 180) / math.pi


def sumaVectores(vec1, vec2):
    res = [0] * len(vec1)
    if len(vec1) != len(vec2):
        print('La suma de vectores no es posible')
    else:
        for i in range(len(vec1)):
            res[i] = sumaComplejos(vec1[i], vec2[i])
        return res


def invertirSignos(com):
    pos1 = com[0] * - 1
    pos2 = com[1] * - 1
    return pos1, pos2


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


def main():
    numero1 = (1, 1)
    numero2 = (8, -2)
    vector1 = [(1, 4), (2, 1), (3, 2)]
    vector2 = [(1, 2), (1, 1)]
    mat1 = [[(1 / math.sqrt(2), 0), (1, 0)], [(1, 0), (0, 0)]]
    mat2 = [[(3, 0), (4, 0)], [(2, 0), (1, 0)]]
    # suma = sumaVectores(vector1, vector2)
    #producTensor = prodTensorVect(vector1, vector2)
    #producTensorMat = prodTensorMatr(mat1, mat2)
    # print(suma)
    #print(producTensor)
    #for i in producTensorMat:
    #    print(i)
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
    cartApolar = cart_pola(numero1)
    print(cartApolar)
    porlAcart = pola_cart(cartApolar)
    print(porlAcart)


main()
