
"""
Crible d'eratosthene
 1      2      3    4       5      6 <= entiers
[True, True, True, False, True, False, ...] <= primalité
https://fr.wikipedia.org/wiki/Crible_d%27%C3%89ratosth%C3%A8ne
"""
def _eratosthene_crible(upper_bound):
    # 1. Initialisation plus rapide et synthétique en Python
    bool_array = [True] * upper_bound

    # 2. 0 et 1 ne sont pas premiers
    bool_array[0] = bool_array[1] = False

    # 3. Inutile d'aller au-delà de sqrt(upper_bound) pour le terme k
    limit = int(upper_bound**0.5) + 1

    for k in range(2, limit):
        # 4. On ne rayera les multiples de k QUE si k est lui-même premier
        if bool_array[k]:
            for j in range(k * k, upper_bound, k):
                bool_array[j] = False

    return bool_array

def generate_primes_until(upper_bound):
    # créer la liste à partir du tableau de boolean
    prime_numbers = []
    rr = _eratosthene_crible(upper_bound)
    for i, val in enumerate(rr):
        if val:
            prime_numbers.append(i)
    return prime_numbers

def is_prime(val):
    """
    is_prime is O(n - 3) so O((n-3)/2)
    """
    arr = set(generate_primes_until(val+1))
    
    return val in arr


