'''
delete duplicate from sorted array

[1, 2, 3, 4, 3, 4]
             |
                |
'''

def deleteDuplicate(arr): # O(n) time O(n) space
    return list(set(arr))

def deleteDuplicate2(arr): # O(n) time O(1) space
    if not arr: 
        return
    i = 0
    for j in range(len(arr)):
        if j == len(arr) - 1 or arr[j] != arr[j + 1]:
            arr[i] = arr[j]
            i += 1
    for idx in range(len(arr) - 1, i - 1, -1):
        del arr[idx]
    return arr
    
arr = [1, 2, 2, 3, 3, 4]
print(deleteDuplicate2(arr))
