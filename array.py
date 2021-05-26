'''
the bisect library is a good way to insert elements into sorted lists.
'''
import bisect

arr = [2, 3, 5, 6, 7, 8]
print(bisect.bisect(arr, 3)) # 2 is the index to insert element 3
print(bisect.bisect_left(arr, 3)) # 1 is the index to insert element 3
print(bisect.bisect_right(arr, 3)) # 2 is the index to insert element 3
print(bisect.bisect(arr, 4)) # 2 is the index to insert 4
print(bisect.bisect_left(arr, 4)) # also index 2

'''
insert elements 4, 8, 4, 2, 1 ,9, 4, 6, 3 to arr 
'''
toInsert = list(reversed([4, 8, 4, 2, 1 ,9, 4, 6, 3]))
arr2 = []
while toInsert:
    el = toInsert.pop()
    idxToInsert = bisect.bisect(arr2, el)
    arr2.insert(idxToInsert, el)

print(arr2)

