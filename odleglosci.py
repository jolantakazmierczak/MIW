import math

# Do domu
# odległości pomiędzy pierwszym a pozostałymi
#  d(y,x), gdzie x należy do lista, bez elementu z indexem 0
#  { 0: [], 1: [], 3: [], 4: []}
#     |klasa decyzyjna          |lista z odległosćiami


lista = []

with open("australian.dat", "r") as file:
    for line in file:
        tmp = line.replace('\n','').split()
        result = list(map(lambda e: float(e), tmp))
        lista.append(result)

def metrykaEuklidesowa(listaA, listaB):
    tmp = 0
    for x in range(len(listaA)-1):
        tmp+=(listaA[x]-listaB[x])**2

    return math.sqrt(tmp)

def distance(lista):
    list1 = []
    list2 = []
    lista0 = lista[0]
    for x in range(1, len(lista)):
        euclides = metrykaEuklidesowa(lista0, lista[x])
        if lista[x][len(lista[0]) -1] == 1:
            list1.append(euclides)
        elif lista[x][len(lista[0]) - 1] == 0:
            list2.append(euclides)
    pairs = {
        '0': list1,
        '1': list2,
    }
    return pairs


dist = distance(lista)
print(dist)
print('0:',dist['0'])
print('1:',dist['1'])
