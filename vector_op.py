import numpy as np
import math


# W oparciu o operacje wektorowe proszę napisać funkcję do obliczania
# średniej arytmetycznej oraz wariancji i odchylenia standardowego

# średnia arytmetyczna iloczyn skalarny

def scalarMean(wektor):
    w1 = np.ones(len(wektor))
    return np.dot(wektor, w1) / len(wektor)



def aritmeticMean(wektor):
    return sum(wektor) / len(wektor)

def variance(wektor):
    ans = 0
    length = len(wektor)
    for i in range (length):
        ans += (wektor[i] - aritmeticMean(wektor)) ** 2
    return ans / length

def standardDeviation(wektor):
    ans = 0
    length = len(wektor)
    for i in range (length):
        ans += (wektor[i] - aritmeticMean(wektor)) ** 2
    return math.sqrt(ans / length)

def vectorOperations(wektor):
    ans = 0
    length = len(wektor)
    for i in range (length):
        ans += (wektor[i] - sum(wektor) / len(wektor)) ** 2
    print("Aritmetic mean: ", sum(wektor) / len(wektor), "\nVariance: ", ans / length, "\nStandard deviation: ", math.sqrt(ans / length))



wk = [1, 3, 4, 5]

print('Średnia arytmetyczna:')
print('Numpy: ', np.mean(wk))
print('aritmeticMean(): ',aritmeticMean(wk))
print('scalarMean(): ',scalarMean(wk))


print("----------------------------------")

print('Wariancja:')
print('Numpy: ', np.var(wk))
print('variance(): ', variance(wk))

print("----------------------------------")

print('Odchylenie standardowe:')
print('Numpy: ', np.std(wk))
print('standardDeviation(): ', standardDeviation(wk))

print("----------------------------------")

vectorOperations(wk)

print("----------------------------------")
