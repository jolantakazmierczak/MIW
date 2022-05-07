import math
from collections import defaultdict
import numpy as np

lista = []


with open("australian.dat", "r") as file:
    for line in file:
        lista.append(line.replace('\n','').split())




for x in range(5):
    print(lista[x])

print("---------------------------------------------------------------------------------------------------------------")

lista2 = []

with open("australian.dat", "r") as file:
    for line in file:
        tmp = line.replace('\n','').split()
        result = list(map(lambda e: float(e), tmp))
        lista2.append(result)


for x in range(5):
    print(lista2[x])

print("---------------------------------------------------------------------------------------------------------------")


def metrykaEuklidesowa(listaA, listaB):
    tmp = 0
    for x in range(len(listaA)-1):
        tmp+=(listaA[x]-listaB[x])**2

    return round(math.sqrt(tmp))


# Do domu
# odległości pomiędzy pierwszym a pozostałymi
#  d(y,x), gdzie x należy do lista, bez elementu z indexem 0
#  { 0: [], 1: [], 3: [], 4: []}
#     |klasa decyzyjna          |lista z odległosćiami

# 2. funkacja która liczy wyznacznik macierzy kwadratowej
print("---------------------------------------------------------------------------------------------------------------")

def lab4(x,lista):
    result = []
    for item in lista:
        c = item[-1]
        dist = metrykaEuklidesowa(x, item)
        result.append((c, dist))
    return result


x =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
lista3 = lab4(x, lista2)

print(lista3)

# ---------------------------
print("---------------------------------------------------------------------------------------------------------------")

def kln(x, lista, k):
        slownik = defaultdict(list)
        slownik_finalny = {}
        for i in range(len(lista)):
            klasa_decyzyjna = (lista[i][len(lista[0]) - 1])
            odleglosc = metrykaEuklidesowa(x, lista[i])
            slownik[klasa_decyzyjna].append(odleglosc)
        for key in slownik:
            suma = 0
            slownik[key].sort()
            for i in range(k):
                suma += slownik[key][i]
            slownik_finalny[key] = suma
        return slownik_finalny



print(kln([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], lista2, 5))





# Do domu
# Jak obliczyć metrykę euklidesową dla 2 obiektów korzystając z wektora
print("---------------------------------------------------------------------------------------------------------------")

def euclidean_distance(a, b):
	return math.sqrt(sum((e1-e2)**2 for e1, e2 in zip(a,b)))

print(euclidean_distance([3,5,6], [5,8,0]))

print("---------------------------------------------------------------------------------------------------------------")

def metrykaEuklidesowaWektory(lista1, lista2):
    v1 = np.array(lista1)
    v2 = np.array(lista2)
    dist = v1 - v2
    tmp = np.dot(dist, dist)

    return math.sqrt(tmp)



print(metrykaEuklidesowaWektory([3,5,6], [5,8,0]))
print(metrykaEuklidesowa([3,5,6], [5,8,0]))




# 28 luty 10 minuta wykładu


# program do całkowania
# 1. metoda monte carlo
# 2. metoda prostokątów  /  metoda trapezów











def lab4(x,lista):
    result = []
    for item in lista:
        c = item[-1]
        dist = metrykaEuklidesowa(x, item)
        result.append((c, dist))
    return result


x =[1,1,1,1,1,1,1,1,1,1,1,1,1,1]
lista3 = lab4(x, lista2)

for x in range(5):
    print(lista3[x])


def pogrupuj(lista):
    my_dict = {}
    for k, v in lista:
        my_dict[k] = v
    return my_dict

# print("---------------------------------------------------------------------------------------------------------------")
# dict3 = pogrupuj(lista3)
#
# for key, value in dict3.items():
#     print(key, value)


# def group_list(lista):
#     sl = {}
#     for i in range(len(lista)):
#         c = (lista[i](len(lista[0])-1))
#         dist = metrykaEuklidesowa(x, lista[i])
#         sl[c.append(dist)]
#         return sl
#
# print("---------------------------------------------------------------------------------------------------------------")
# dict3 = group_list(lista3)
#
# for key, value in dict3.items():
#     print(key, value)





# Do domu
# Jak obliczyć metrykę euklidesową dla 2 obiektów korzystając z wektora