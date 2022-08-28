# https://projecteuler.net/problem=1
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""
from functools import reduce
from math import floor
N = 1000


def is_multiple_of(left, right):
    return right % left == 0 or left % right == 0

# def sumOfMultipleUnder(mult, limit):
#     return reduce(lambda x, y: y + x, range(1, floor(limit/mult) + 1), 0) * mult


def sumOfMultipleUnder(mult, n):
    p = n // mult
    x = mult * p * (p+1)  // 2
    return x 


if __name__ == "__main__":
    n = 999

    sum = sumOfMultipleUnder(3, n) + sumOfMultipleUnder(5, n)  - sumOfMultipleUnder(15, n)

    print(f"The sum of all the multiples of 3 or 5 below 1000 is {sum}")
