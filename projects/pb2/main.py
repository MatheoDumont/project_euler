"""
https://projecteuler.net/problem=2


Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

"""

import functools


def fibonacci(n):
    prec = 0
    fibo = 1

    while fibo < int(n):
        tmp = fibo
        fibo = fibo + prec
        prec = tmp

        yield fibo


def fn():

    sum = 0
    for i in fibonacci(4e6):
        if i % 2 == 0:

            sum += i
    return sum


def even_fibonacci(n):
    """
    2 3 5 8 13 21 34 55 89 144 
    +     +       +         +
    every 3 is even in the fibonacci sequence
    and even there is a property,

    Even(n) = 4 * even(n-1) + even(n-1) 
    even(2) = 4 * even(1) + even(0) = 4*2 + 0 = 8
    even(3) = 4 * even(2) + even(1) = 4*8 + 2 = 32
    even(4) = 4 * even(3) + even(2) = 4*34 + 8 = 136 + 8 = 144

    """
    n_minus_two = 0
    n_minus_one = 2

    while n_minus_one < int(n):
        yield n_minus_one
        tmp = n_minus_one
        n_minus_one = 4*n_minus_one + n_minus_two
        n_minus_two = tmp


def fn2():
    return functools.reduce(lambda a, x: a+x, even_fibonacci(4e6), 0)


if __name__ == "__main__":
    sum = fn2()

    print(
        f"By considering the terms in the Fibonacci sequence whose values do not exceed four million, the sum of the even-valued terms is {sum}")
