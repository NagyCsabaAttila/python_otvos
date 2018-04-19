import numpy as np
import math

#5. FELADAT


#11. FELADAT
def palindrome():
    palind = None
    for n in range(100, 1000):
        for m in range(100, 1000):
            prod = n * m
            if str(prod) == str(prod)[::-1]:
                if palind is None or prod > palind:
                    palind = prod
    return palind

print(palindrome())

#12. FELADAT

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def n_prime(n):
    i = 2
    while n > 0:
        if is_prime(i):
            n = n - 1
            if n == 0:
                return i
        i = i + 1
    return -1

print(n_prime(10001))
