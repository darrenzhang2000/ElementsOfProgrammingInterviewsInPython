'''
find all primes from 1 to n
'''

def enumeratePrimesToN(n):
    primes = []
    for i in range(2, n + 1):
        isPrime = True
        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    return primes

# print(enumeratePrimesToN(100))

import math
def enumeratePrimesToN2(n):
    s = set(i for i in range(2, n + 1))
    for i in range(2, int(math.sqrt(n))):
        if isPrime(i):
            removeMultiplesFromSet(i, s, n)
    return list(s)

def isPrime(i):
    for j in range(2, i):
        if i % j == 0:
            return False
    return True

def removeMultiplesFromSet(i, s, n):
    multiplicity = 2
    while multiplicity * i <= n:
        if multiplicity * i in s:
            s.remove(multiplicity * i)
        multiplicity += 1

print(enumeratePrimesToN2(100))
