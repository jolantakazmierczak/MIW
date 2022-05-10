import math
import numpy as np


def metrykaEuklidesowa(listaA, listaB):
    tmp = 0
    for x in range(len(listaA)-1):
        tmp+=(listaA[x]-listaB[x])**2

    return math.sqrt(tmp)

def metrykaEuklidesowaWektory(lista1, lista2, x=False):
    if x:
        lista1 = lista1[:-1]
        lista2 = lista2[:-1]
    res = np.array(lista1) - np.array(lista2)
    return math.sqrt(np.dot(res, res))



print(metrykaEuklidesowaWektory([3,5,6], [5,8,0], True))
print(metrykaEuklidesowa([3,5,6], [5,8,0]))
