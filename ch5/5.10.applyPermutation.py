'''
apply permutation [3, 0, 1, 2] to n=[1,2,3,4] yields n=[2,3,4,1]


[3, 0, 1, 2] to n=[2,3,4,1]
2

curIdx = 1
newIdx = 3
temp = arr[newIdx] = 3
arr[newIdx] = n[curIdx] = 2




'''

def applyPermutation(perm, arr):
    # assume valid permutation
    newArr = [0] * len(arr)
    for i, v in enumerate(perm):
        newArr[v] = arr[i]
    return newArr

# print(applyPermutation([3, 0, 1, 2], [1, 2, 3, 4]))

def applyPermutationInPlace(perm, arr):
    newIdx = perm[0]
    curVal = arr[0]
    for _ in range(len(arr)):
        temp = arr[newIdx]
        arr[newIdx] = curVal
        
        curVal = temp
        newIdx = perm[newIdx]
    return arr


# print(applyPermutationInPlace([3, 0, 1, 2], [1, 2, 3, 4]))

def applyPermutationInPlace2(perm, arr):
    for i in range(len(arr)):
        if perm[i] == i: # already in its proper index
            continue
        while perm[i] != i:
            arr[perm[i]], arr[i] = arr[i], arr[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    return arr

# print(applyPermutationInPlace2([3, 0, 4, 2, 5, 1], ['A', 'B', 'C', 'D', 'E', 'F']))
# ['B', 'F', 'D', 'A', 'C', 'E', 'G', 'H'] [0, 1, 2, 3, 4, 5, 6, 7]

