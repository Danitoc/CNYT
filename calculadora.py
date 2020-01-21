from sys import stdin


def sumaComplejos(num1, num2):
    com1 = num1[0] + num2[0]
    com2 = num1[1] + num2[1]
    return com1,com2


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
    return pos1,pos2


def inverso(vector):
    


def main():
    vector1 = [(2,3), (3,4), (4,5)]
    vector2 = [(6,7), (5,2), (3,1)]
    suma = sumaVectores(vector1, vector2)
    print(suma)

main()
