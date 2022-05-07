import numpy as np

file = open("australian.dat", "r")
lista = []


for line in file:
    lista.append(list(map(lambda x: float(x), line.split())))

for x in range(5):
    print(lista[x])

def metryka_euklidesowa(listaA, listaB):
    suma = 0
    for i in range(len(listaA) - 1):
        suma += (listaA[i] - listaB[i]) ** 2
    return round(suma ** 0.5)


y = lista[0]
slownik = {}

for element in lista[1: ]:
    if slownik.get(element[-1]) == None:
        slownik[element[-1]] = [metryka_euklidesowa(element, y)]
    else:
        slownik[element[-1]].append(metryka_euklidesowa(element, y))

for key, value in slownik.items():
    print(key, value)





def wyznacznik(macierz):
    wynik = 0
    if len(macierz) == 1:
        return macierz[0][0]
    for i in range(len(macierz)):
        new = [row[:] for row in macierz][1:]
        for row in new:
            del row[i]
        wynik += macierz[0][i] * (-1) ** (1+i+1) * wyznacznik(new)
    return wynik


C = [[1, 2, 3, 4], [4, 3, 5, 6], [8, 4, 2, 1], [3, 2, 4, 1]]

print("---------------------------------------------")
cDet = np.linalg.det(C)
print("The Numpy Determinant of B is", round(cDet,9))
print("The determinant of C --> ", wyznacznik(C))
