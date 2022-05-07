# zad 2:
# napisac funkcje, która wyliczny wyznacznik macierzy kwadratowej

import copy
import numpy as np


# Funkcja new_matrix() przyjmuje tablicę i liczbę „i”. Następnie tworzy kopię tablicy, a następnie usuwa pierwszy wiersz
# , a następnie z każdego z pozostałych wierszy usuwa element i-ty i zwraca tablicę wynikową.
# Jeśli długość skopiowanej tablicy wynosi tylko 2, to po prostu zwróci samą tablicę bez porzucania czegokolwiek.

def new_matrix(a, i):
    arr = copy.deepcopy(a)

    if len(arr) == 2:

        return arr
    else:
        arr.pop(0)
        for j in arr:
            j.pop(i)

        return arr

#
def determinant(a):  # FUNCTION TO FIND THE DETERMINANT OF A MATRIX
    # Pobiera tablicę, a jeśli długość tablicy wynosi 1, zwróci jedyny element w tej tablicy.
    if len(a) == 1:
        pro = a[0]
        return pro
    # Jeśli przekazana tablica ma długość 2, to uruchamia się warunek bazowy naszej funkcji rekurencyjnej i zwraca ona odpowiedź z następującego równania:
    elif len(a) == 2:
        pro = a[0][0] * a[1][1] - a[1][0] * a[0][1]
        return pro
    else:
        pro = 0
        for i in range(len(a[0])):
            pro += ((-1) ** i) * a[0][i] * determinant(new_matrix(a, i))
        return pro
    # Jeśli przekazana tablica ma długość większą niż 2, inicjuje zmienną pro jako 0 i iteruje przez długość pierwszego wiersza,
    # i znajduje wartość ((-1)**i)*a[0][ i]*wyznacznik(nowa_macierz(a,i)) i dodaje ją pro. W każdej iteracji wytworzona wartość jest
    # iloczynem i-tego elementu pierwszego wiersza i zwróconej wartości funkcji determinant(), w której funkcja new_matrix()
    # jest nazywana przekazywaniem tablicy i zmiennej iteracji i. Jest to w zasadzie część iteracyjna całego procesu. F
    # unkcja wyznaczająca jest wywoływana sama (rekurencja), dopóki macierz przekazywana wewnątrz funkcji new_matrix jest macierzą 2x2.
    # Po tym wszystkim jest pomnożone przez -1 lub 1. Jeśli i jest nieparzyste, to wartość jest pomnożona przez -1, a jeśli jest parzysta,
    # zostanie pomnożona przez 1.
    # Po każdej iteracji uzyskana wartość jest dodawana do zmiennej pro.

A = [2]
B = [[1, 2, 4], [3, 4, 7], [5, 6, 7]]
C = [[1,   2, 3, 4], [4, 3, 5, 6], [8, 4, 2, 1], [3, 2, 4, 1]]
D = [[1, 3, 5, 7, 9], [4, 6, 3, 7, 5], [5, 10, 8, 3, 1], [1, 5, 3, 7, 6], [8, 1, 7, 5, 8]]


print("The determinant of A --> ", determinant(A))

print("---------------------------------------------")
bDet = np.linalg.det(B)
print("The Numpy Determinant of B is", round(bDet,9))
print("The determinant of B --> ", determinant(B))

print("---------------------------------------------")
cDet = np.linalg.det(C)
print("The Numpy Determinant of B is", round(cDet,9))
print("The determinant of C --> ", determinant(C))

print("---------------------------------------------")
dDet = np.linalg.det(D)
print("The Numpy Determinant of B is", round(dDet,9))
print("The determinant of D --> ", determinant(D))