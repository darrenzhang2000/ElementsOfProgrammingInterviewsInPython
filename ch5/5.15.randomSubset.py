

import random
def computeRandomSubset(arr): # O(n) time O(n) space
    bits = random.getrandbits(len(arr))
    res = []
    i = 0
    while bits:
        if bits & 0b1:
            res.append(arr[i])
        bits = bits >> 1
        i += 1
    return res


# arr = [1, 2, 3, 4, 5, 6, 7]
# print(computeRandomSubset(arr))

'''
random subset of size k

let size = 100 and elements go from 0 to 99
let k = 4
when i = 0, there is an equal chance of choosing all 100 numbers
    - suppose we choose 28
    - store (0, 28) and (28, 0) in ht
    - ht = {0:28, 28:0}
when i = 1, now we have 99 numbers to choose from. 
    - we need to keep track that index 0 can still be chosen
    - suppose we choose 28. since 28 is in the ht,
    that means we have already chosen 28 previously so now we choose
    the element stored at key=28, which is 0.
    - now the value at key=28 becomes 1
    - ht = {0:28, 28:1, 1:0}
when i = 2, we have 98 numbers to choose from. in order to not leave out 
    1, we had to change the value at key=28 to i=1 previously.
    - suppose we choose 2. 
    - since i = 2, and index equal value, we don't have to store it in the 
    ht. 
    - so far, we've chose 28, 0, and 2.
when i = 3, we have 97 numbers to choose from.
    - suppose we choose 3.
    - index = value so we don't have to store anything in ht
when i = 4, we have 96 numbers to choose from.
    - if we choose 28 again, store 4:1 in ht and update 28 to store 4
    - ht = {0:28, 28:4, 1:0}
'''
def computeRandomSubset2(arr, k): # O(n) time O(k) space
    ht = {}
    for i in range(k):
        n = random.randrange(i, len(arr))
        if i == n:
            continue
        else:
            if n in ht:
                ht[i] = ht[n] 
                ht[n] = i # need to save i somewhere so we have a chance of choosing it
            else:
                ht[i] = n
                ht[n] = i
    subsets = []
    for i in range(k):
        subsets.append(ht[i] if i in ht else i)
    return subsets

arr = [1, 2, 3, 4, 5, 6, 7]
print(computeRandomSubset2(arr, 4))