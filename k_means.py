import math
from collections import defaultdict
from random import randint


import numpy as np

### Australian.dat podzielić na 2 zbiory, tak jak robi to klasa decyzyjna, tyle ze bez niej
#
# pierwsze przybliżenie, losowe malowanie wszystkich kropek za pomoca rng
#
# bierzemy odległość wszystkich kropek od siebie(tego samego koloru),
# np odległość kropki [1] od [2,3,4] -> [2] od [1,3,4] itd
# ta która ma najmniejszą sume odległości b��dzie środkiem
# teraz mierzymy odległość każdej kropki od tej środkowej czarnej i niebieskiej
# jeżeli bliżej do czarnej i była czarna to zostawiamy
# jezeli blizej niebieskiej i była czarna to malujemy na niebiesko
# powtarzamy aż do póki nic sie nie zmieni
#

def load_file(file):
    lista = []
    with open(file, 'r') as file:
        for line in file:
            lista.append(list(map(lambda e: float(e), line.replace('\n', '').split())))
    return lista

# usunięcie klasy decyzyjnej
def remove_class(lista):
    dane = []
    for x in lista:
        dane.append(x[:-1])
    return dane

# przypisanie losowej klasy decyzyjnej
def random_class(lista):
    for i in range(len(lista)):
        lista[i][len(lista[i])-1] = float(randint(0, 1))
    return lista

# grupowanie listy po klasie decyzyjnej
def group_list(lista):
    sl = defaultdict(list)
    for i in range(len(lista)):
        k_decyzyjna = (lista[i][len(lista[0]) - 1])
        sl[k_decyzyjna].append(lista[i])
    return sl

def metrykaEuklidesowaWektory(lista1, lista2, x=False):
    if x:
        lista1 = lista1[:-1]
        lista2 = lista2[:-1]
    res = np.array(lista1) - np.array(lista2)
    return math.sqrt(np.dot(res, res))

# suma odległości
def distance_sum(tmp, lista):
    suma = 0
    for i in range(len(lista)):
        suma += metrykaEuklidesowaWektory(tmp, lista[i])
    return suma

# minimalna odległość
def center_of_gravity(id: list, listaA: list):
    dist = []
    tmp = 0
    for i in id:
        for j in id:
            tmp += metrykaEuklidesowaWektory(listaA[i], listaA[j])
        dist.append(tmp)
        tmp = 0
    min = 0
    for i in range(1, len(dist)):
        if dist[min] > dist[i]:
            min = i

    return min


# kolorowanie
def color(listaA):
    randomList = random_class(listaA)
    changes = True

    while(changes):
        changes = False
        sl = dict()

        for i in range(len(randomList)):
            classD = randomList[i][-1]

            if classD in sl.keys():
                sl[classD].append(i)
            else:
                sl[classD] = [i]

        newTab = []

        for el in sl.values():
            newTab += el

        centers = []

        for tab in sl.values():
            centers.append(tab[center_of_gravity(tab, randomList)])

        dist = []

        for el in newTab:
            for c in centers:
                dist.append(metrykaEuklidesowaWektory(
                    randomList[el], randomList[c]))

            min = 0
            count = 1

            for i in range(1, len(dist)):
                if dist[min] > dist[i]:
                    min = i
                    count = 1

                elif dist[min] == dist[i]:
                    count = count+1

            if count == 1:
                if randomList[el][-1] != randomList[centers[min]][-1]:
                    randomList[el][-1] = randomList[centers[min]][-1]
                    changes = True

            elif count > 1:
                randomList[el][-1] = None
                changes = True

            dist = []

    return randomList



lista = load_file('australian.dat')
print(lista)
dane = remove_class(lista)
print(dane)

kMeans = color(dane)


dict = group_list(kMeans)
print('0:',dict[0])
print('1:',dict[1])



for key in dict.keys():
    print("{0}: {1}".format(key, len(dict[key])))