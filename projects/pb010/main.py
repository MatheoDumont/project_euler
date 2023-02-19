import pb3.main as primes
import matplotlib.pyplot as plt
import numpy as np
from chronometer import print_chrono_with_func


def pour_n(n):
    sum = 0
    count = 0
    primes_under_n = []
    for i in range(3, n, 2):
        if primes.is_prime(i):
            sum += i
            count += 1
            primes_under_n += [i]

    return sum, count, primes_under_n


def derivate(x):
    derivative = [0]
    for i in range(1, len(x)):
        derivative += [(x[i] - x[i-1]) / 2]
    return derivative


def research():
    unique_sum = {}
    MIN_SUM = 10
    MAX_SUM = 500
    for n in range(MIN_SUM, MAX_SUM):
        sum, count, primes = pour_n(n)
        unique_sum[sum] = (n, count, primes)

    ks = list(unique_sum.keys())

    first_derivative = derivate(ks)
    second_derivative = derivate(first_derivative)
    third_derivative = derivate(second_derivative)
    fourth_derivative = derivate(third_derivative)

    print(len(second_derivative), len(ks))
    plt.figure()
    plt.plot(ks, first_derivative, color='r')
    # plt.plot(ks, second_derivative, color='g')
    # plt.plot(ks, third_derivative, color='b')
    plt.plot(ks, fourth_derivative, color='b')

    plt.savefig('derivatives.png')

    for i in range(0, len(ks)):
        sum = ks[i]

        d = first_derivative[i]

        dd = second_derivative[i]
        ddd = third_derivative[i]
        dddd = fourth_derivative[i]
        n, count, primes = unique_sum[sum]
        _d = n - d
        # print(f"SUM until [{n}] is [{sum}] with [{count}] prime numbers. Derivatives 1 [{d}], 2 [{dd}], 3 [{ddd}], 4 [{dddd}]")
        decomp = primes.prime_factor_decomposition(sum)
        print(
            f"SUM until [{n}] is [{sum}] with [{count}] prime numbers. Derivatives 1 [{d}], Diff N/Deriv [{_d}]")
        print(f"==> decomp is {decomp}")

    print(primes.prime_factor_decomposition(10**6))


def pour_n_2(n):
    sum = 2+3
    count = 2
    primes_under_n = [2, 3]
    for i in range(5, n, 2):
        if primes.is_prime_with_previous_primes(i, primes_under_n):
            sum += i
            count += 1
            primes_under_n += [i]

    return primes_under_n, count, sum


if __name__ == "__main__":
    print_chrono_with_func(pour_n, 1000)
    print_chrono_with_func(pour_n_2, 2*10**6)
