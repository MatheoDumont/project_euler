"""
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
import math
from chronometer import print_chrono_with_func

def condition(a, b, c):
    return a+b+c == ABC and a**2 + b**2 == c**2


ABC = 1000

def brute_force():
    """
    brute force method, we know that a < b < c
    O(n^3)
    """
    for c in range(1, ABC+1):
        for b in range(1, c):
            for a in range(1, b):
                if condition(a, b, c):
                    return a, b, c


def s2():
    """
    better, we also know that
    a + b + c = 1000
    then a = 1000 - b - c allow to avoid loop [1, b] for each b for each c.
    Plus, a > b > c > 0, since a*b*c != 0, and since natural number, each start to one minimum hence none can be equal 
    to 1000 but 1000 - 3 <=> 1000 - 1-1-1
    O(n²) 
    """
    for c in range(1, ABC-3):
        for b in range(1, c):
            a = ABC - c - b
            if condition(a, b, c):
                return a, b, c


def s3():
    """
    probably a way to compute bounds of c, a or b.

    """
if __name__ == "__main__":
    print_chrono_with_func(brute_force)
    print_chrono_with_func(s2)
