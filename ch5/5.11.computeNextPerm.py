'''
Compute next permutation

[1, 2, 3, 1] -> [1, 3, 2, 1]

Observations:
- if also sorted in descending order, there is no next permutation.

[1, 2] -> [2, 1]  2 is bigger than 1 so swap 1, 2
[1, 2, 3] -> [1, 2, 3]  3 is bigger than 2 so swap 2, 3
[1, 2, 3, 1] -> [1, 3, 2, 1] -> [1, 3, 1, 2] 3 is bigger than 2 so swap (2, 3) then sort everything to the right of 3
This operation takes O(nlogn) where n is length of arr. Can be better

[0, 7, 0, 5, 6, 3, 5, 4, 2, 2]

[0, 7, 0, 5, 6, 3, 5, 4, 2, 2] -> [0, 7, 0, 5, 6, 4, 5, 3, 2, 2] 5 > 3 so swap 3 with next biggest in the dec sequence


'''
def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def computeNextPermutation(A): # O(n) time O(1) space
    idx = findFirstDecIdx(A)
    if idx == -1:
        return []
    idxToSwap = findNextBigger(A, A[idx - 1])
    swap(A, idx - 1, idxToSwap)
    A[idx::] = reversed(A[idx:])
    return A

def findNextBigger(A, el):
    for i in reversed(range(len(A))):
        if A[i] > el:
            return i

def findFirstDecIdx(A):
    for i in reversed(range(1, len(A))):
        if A[i] > A[i - 1]:
            return i
    return -1

print(computeNextPermutation([1, 2, 3, 1]))
print(computeNextPermutation([0, 7, 0, 5, 6, 3, 5, 4, 2, 2]))
print(computeNextPermutation([3, 2, 1]))

'''
Take away: try a bunch of examples before actually assuming that my algorithm is correct
If I do find an algorithm that works, try it on a few more inputs.

[1, 2, 3, 9, 8, 7, 5, 3, 2, 1]
old algorithm would've swapped idx 2 and idx 3 then sort and reverse everything after idx 2 which is incorrect.
the correct approach is to identify idx 3 is the first element not part of the decreasing sequence,
swap it with the next biggest element in the sequence (to minimize the increase),
then reverse the array after idx 3.


'''