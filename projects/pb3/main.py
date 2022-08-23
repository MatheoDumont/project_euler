"""
https://projecteuler.net/problem=3


The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
from math import floor, sqrt


def is_prime(val):
    """
    is_prime is O(n - 3) so O(n)
    """
    for i in range(2, val):
        if val % i == 0:
            return False
    return True


def is_prime_factor(x, val):
    """
    is_prime_factor is O(n)
    """
    if is_prime(x) and val % x == 0:
        return True
    return False


def prime_factor_decomposition(val):
    """
    prime_decomposition is O(n-3)*O(n-3) = O(n²)
    """
    if is_prime(val):
        return [val]

    for i in range(2, floor(sqrt(val))+1):
        if is_prime_factor(i, val):
            return [i, *prime_factor_decomposition(int(val/i))]


if __name__ == "__main__":
    primes = prime_factor_decomposition(600851475143 )
    print(f"The prime factors of 600851475143  are {primes}")
    



    

