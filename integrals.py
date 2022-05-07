import random
import numpy as np
# ------- monte carlo method -------


# function to calculate the sin of a particular
# value of x
def f(x):
    return x

def monte_carlo(a, b, N):
    ar = np.zeros(N)   # array of zeros of length N

    # variable to store sum of the functions of
    # different values of x
    integral = 0.0

    # iterating over each Value of ar and filling
    # it with a random value between the limits a
    # and b
    for i in range(len(ar)):
        ar[i] = random.uniform(a, b)

    # iterates and sums up values of different functions
    # of x
    for i in ar:
        integral += f(i)

    ans = (b - a) / float(N) * integral

    return round(ans,1)

a = 0
b = 1  # gets the value of pi
N = 1000
print("----------------------------------")
print("Monte Carlo method:")
print(monte_carlo(a, b, N))

# ------- rectangle method -------

def func(x):
    return x

def rectangle(a, b, N):
    step = (b - a) / N
    integral = 0

    for i in range(N):
        integral += step * func(a + (i - 1) * step)

    return round(integral,1)


print("----------------------------------")
print("Rectangle method:")
print(rectangle(a, b, N))


