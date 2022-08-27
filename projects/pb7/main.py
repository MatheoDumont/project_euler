"""
https://projecteuler.net/problem=7



By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


"""


def nth_prime(n):
    assert(n>=1)
    i = 1
    preceding_primes = [2]
    count = 3
    while i != n:
        divisable = True

        for p in preceding_primes:
            if count % p == 0:
                divisable = False
                break
        if divisable:
            preceding_primes.append(count)   
            i +=1
        count += 1

    return preceding_primes[-1]


if __name__ == "__main__":
    print(f"10001 th prime is {nth_prime(10001)}")