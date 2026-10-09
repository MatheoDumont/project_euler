"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains
terms 21, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
from ..libs import primes as pl

UPPER_BOUND=1_000_000

primes = pl.generate_primes_until(UPPER_BOUND)
print(f"{len(primes)} nombres premiers inférieur à {UPPER_BOUND}")
"""
array where tab[i] = sum of 0 to ith prime number
ie, tab[6] = 41 = 2+3+5+7+11+13

can do tab[6] - tab[7] = 7th prime number
with tab[7] = 58 = 2+3+5+7+9+11+13+17, 58-41 = 17
and the sum of prime numbers fropm i to j can be obtain by doing tab[j] - tab[i]
"""
def build_sum_of_prime_array(primes, max_count):
    n = min(len(primes), max_count)
    arr = [0 for i in range(n)]
    for i in range(n):
        for j in range(i, n):
            arr[j] += primes[i]
    return arr

def max_sum_before_bound(primes, bound, starting_step=0):
    s = 0
    for i in range(starting_step, len(primes)):
        if s + primes[i] > UPPER_BOUND:
            break
        s += primes[i]
    return i-starting_step, s

set_primes = set(primes)
first_prime = 0
for i in range(100):
    i, s = max_sum_before_bound(primes, UPPER_BOUND, i)
    if s in set_primes:
        first_prime = (i, s)
        break

max_window = max_sum_before_bound(primes, UPPER_BOUND, 0)[0]
tab = build_sum_of_prime_array(primes, max_window)

print(f"le nombre max de nombres premiers sommés inférieur à {UPPER_BOUND} est {max_window} et donne {tab[max_window-1]}\n")
print(f"Résultat:\nLe nombre premier {first_prime[1]} est le plus grand avant {UPPER_BOUND} avec {first_prime[0]} nombres premiers sommés")

