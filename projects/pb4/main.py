"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


"""



def is_palindrome(nb) -> bool:
    s = str(nb)
    half = int(len(s) / 2)
    # print(s[:half])
    # print(s[half:][::-1])
    return s[:half] == s[half:][::-1]


def brute_force():
    l = 0

    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if is_palindrome(i*j):
            
                l = max(i*j, l) 

    return l



if __name__ == "__main__":

    print(brute_force())

