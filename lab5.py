import math
from collections import defaultdict
import numpy as np

lista = []


with open("australian.dat", "r") as file:
    for line in file:
        lista.append(line.replace('\n','').split())

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

def metryka_euklidesowa_wektory(obj_1, obj_2):
    wynik = 0
    for a, b in zip(obj_1, obj_2):
        wynik += (a - b) ** 2
    return math.sqrt(wynik)


print(metryka_euklidesowa_wektory([1, 2, 4, 6], [5, 8, 7, 6]))



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
#
#
# =2 iteracje
# całka = pole pod krzywą
# całkowanie numeryczne
# metoda monte carlo, objaśnienie działania
# drugi sposób całkowania
# suma górna, suma dolna
# mamy krzywą bożą
# dzielimy na sumę górną i dolną, taki prostokąt(górny = nad krzywą, dolny = pod krzywą),
# im mniejszy podział tym większa dokładność
#