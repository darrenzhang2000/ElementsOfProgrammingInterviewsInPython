'''
compute alternation
[3, 3, 13, 14, 5, 7, 3, 10, 11, 14]

brute force: sort then interweave

[3, 3, 3, 5, 7, 10, 11, 13, 14, 14]
[3, 3, 3, 5, 7] [10, 11, 13, 14, 14]
[3, 14, 3, 14, 3, 13, 5, 11, 7, 10]
'''

def computeAlternation(arr):
    arr.sort()
    res = []
    for i in range(len(arr) // 2):
        res.append(arr[i])
        res.append(arr[len(arr) - 1 - i])

    if len(arr) % 2 == 1:
        res.append(arr[len(arr) // 2])
        if len(arr) >= 3 and (arr[-1] >= arr[-2] >= arr[-3] or arr[-1] <= arr[-2] <= arr[-3]):
            arr[-1], arr[-2] = arr[-2], arr[-2]
    return res

# arr = [3, 3, 13, 14, 5, 100, 3, 10, 11, 14, 0]
# print(computeAlternation(arr))


'''
approach 2: use a minheap and maxheap -> O(n) time O(n) space
[3, 3, 13, 14, 5, 7, 3, 10, 11, 14]

approach 3: find median , sort relative to median (using quickselect)
then interweave -> O(n) time O(n) space 

[3, 3, 13, 14, 5, 100, 3, 10, 11, 14, 0]

[3, 13, 3, 14, 5, 100, 3, 11, 10, 14, 0]
   i   d   i  d  i   d   i   d   i   d
   
[1, 3, 2, 5, 4, 7, 6]
   i  d  i  d  i  d
[1, 2, ]
'''

def computeAlternation2(arr):
    for i in range(len(arr) - 3):
        arr[i:i+3] = sorted(arr[i:i+3], reverse=bool(i%2))
    return arr

arr = [3, 3, 13, 14, 5, 100, 3, 10, 11, 14, 0]
print(computeAlternation2(arr))
