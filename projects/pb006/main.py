import functools
from math import factorial
"""
https://projecteuler.net/problem=6


The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


"""
if __name__ == "__main__":
    print(functools.reduce(lambda x,b : x + b**2, range(1, 11)))
    print(functools.reduce(lambda x,b : x + b, range(1, 11))**2)

    print(functools.reduce(lambda x,b : x + b**2, range(1, 101)))
    print(functools.reduce(lambda x,b : x + b, range(1, 101))**2)


    """
    avec puissance = 2
    x = (a + b)² = a² + b² + 2ab
    y = a² + b² 
    x - y = 2ab

    avec puissance = 3
    x = (a + b + c)² = a² + b² + c² + 2ab + 2ac + 2bc
    y = a² + b² + c² 
    x - y = 2ab + 2ac + 2b


    donc la différence est 
    """

    diff = 0
    N = 100
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            diff += i*j

    diff *= 2

    print(diff)
