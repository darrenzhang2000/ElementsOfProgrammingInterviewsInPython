'''
find all primes from 1 to n
'''

def enumeratePrimesToN(n):
    primes = []
    for i in range(2, n + 1): # O(n^2)
        isPrime = True
        for j in range(2, int(math.sqrt(i))):
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
    for i in range(2, int(math.sqrt(n))): # O(sqrt(n)) time
        if isPrime(i): # O(sqrt(n)) since we're only checking up to sqrt(n)
            removeMultiplesFromSet(i, s, n) # remove at most n elements from set
    return list(s)

def isPrime(i):
    for j in range(2, int(math.sqrt(i))):
        if i % j == 0:
            return False
    return True

def removeMultiplesFromSet(i, s, n):
    for p in range(2*i, n + 1, i):
        if p in s:
            s.remove(p)

#print(enumeratePrimesToN2(100))

'''
epi soln
'''
def generatePrimes(n):
    if n < 2:
        return []
    size = (n - 3) // 2 + 1
    primes = [2]
    isPrime = [True] * size
    for i in range(size):
        if isPrime[i]:
            p = i * 2 + 3
            primes.append(p)
            for j in range(p*p, size, p):
                isPrime[j] = False
    return primes

print(generatePrimes(100))
