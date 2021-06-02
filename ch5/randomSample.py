'''
given an array of elements and a size k, generate a subset of size k.
each element has to be equally likely to be picked.

arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G'], k = 4
'''

import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def randomSample(arr, k):
    for i in range(k):
        r = random.randrange(i, len(arr))
        swap(arr, i,r)
    return arr[:k]

arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
k = 4

def testRandomness(arr, k):
    ht = {}
    for _ in range(10000):
        arr = randomSample(arr, k)
        for el in arr:
            if el not in ht:
                ht[el] = 1
            else:
                ht[el] += 1
    return ht

