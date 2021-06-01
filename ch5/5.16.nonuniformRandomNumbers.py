'''
arr = [3, 5, 7, 11]
p = [9/18, 6/18, 2/18, 1/18]

brute force O(n) time O(1) space if we modify p:
get decimal ranges for each element
p1 = [0.5, 8333333333333333, 0.9444444444444444, 1]
choose a random number between 0 and 1. 
choose 0.9 -> this corresponds to el 7.
'''

import random
def generateNonuniformRandomNumbers(arr, p):
    for i in range(1, len(p)):
        p[i] += p[i - 1]
        # print(p[i - 1])
    n = random.random()
    print(p)
    for i in range(len(arr)): # O(n), could be better if binary search is used
        print(n, p)
        if n <= p[i]:
            return arr[i]
arr = [3, 5, 7, 11]
p = [9/18, 6/18, 2/18, 1/18]
# print(generateNonuniformRandomNumbers(arr, p))


'''
test doesn't work for my code b/c i'm mutating array p 
'''
# def test(arr, p):
#     n = 10
#     ht = {arr[i]: 0 for i in range(len(arr))}
#     for _ in range(n):
#         num = generateNonuniformRandomNumbers(arr, p)
#         ht[num] += 1
#     return ht

# print(test(arr, p))

'''
epi soln
'''
import bisect
import itertools
def nonuniform_rand_num(values, probabilities):
    prefixSumProbabilities = list(itertools.accumulate(probabilities))
    intervalIdx = bisect.bisect(prefixSumProbabilities, random.random())
    return values[intervalIdx]

print(nonuniform_rand_num(arr, p))