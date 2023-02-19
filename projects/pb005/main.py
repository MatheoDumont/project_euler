"""
https://projecteuler.net/problem=5



2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
evenly divisible = remainder of division is zero
"""
from math import sqrt, floor


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
    for i in range(0, 30):
        if is_prime(i):
            print(i)

"""
le plus petit entier divisble par les entiers dans [1...20]

donc on cherche un p tel que

for i in range(1, 20):
    assert p % i == 0

on pourrait faire :
p = 1

for i in range(2,20):
    p*=i

mais p ne serait pas le plus petit possible,
pour qu'il soit le plus petit possible, il faut que tous les facteurs de p soit non reductible donc premier.

on peut commencer par prendre tous les entiers premiers car ils n'ont pas de plus petit diviseur hormis eux-mêmes,
donc p = 1*2*3*5*7*11*13*17*19

Sachant que pour qu'un nombre entier a divise un autre b, la valuation p-adique de chaque exposant doit etre présente dans p,
cad: 
avec a et b deux entiers positif,  pour que a divise b, il faut que sa décomposition en facteurs premiers contienne celle de b
donc si 
    b = 20, pfd(20) = 2 * 2 * 5 = 2^2 * 5
donc pfd(a) = f1^p1_x1 * f2^p2_x2 * ... fn^pn_x tel que

for p in pfd(b):
    p is in pfd(a) ou autrement dit pfd(a) % p == 0

puis pour chaque chiffre non compris dans ceux-ci x_i = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
on decompose xi en ses facteurs premiers 
puis ajoute les facteurs manquant 
donc :

pfd(4) = [2, 2] <-- il manque un facteur 2 dans p
p = 2*3*5*7*11*13*17*19*2
pfd(6) = [2, 3] <-- c'est bon, il ne manque rien, donc p reste le meme
pfd(8) = [2, 2, 2] <-- il manque un facteur 2 dans p
p = 2*3*5*7*11*13*17*19*2*2
pfd(9) = [3, 3] <-- il manque un facteur 3 dans p
p = 2*3*5*7*11*13*17*19*2*2*3
pfd(10) = [2, 5] 
pfd(12) = [2, 2, 3]
pfd(14) = [2, 7]
pfd(15) = [3, 5]
pfd(16) = [2, 2, 2, 2] <-- il manque un facteur 2 dans p
p = 2*3*5*7*11*13*17*19*2*2*3*2
pfd(18) = [2, 3, 3]
pfd(20) = [2, 2, 5]


donc p = 2**4 * 3**2 *5*7*11*13*17*19

p = 2*3*5*7*11*13*17*19*2*2*3*2 = 232792560

"""