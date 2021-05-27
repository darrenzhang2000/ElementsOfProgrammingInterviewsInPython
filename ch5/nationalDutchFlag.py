'''
Rerder entries so that even entires appear first

Input:
[1, 2, 3, 4, 5, 6]

Have two pointers i and j. Move i right and j left until an element out of place is found.
Then swap and move. 
[1, 2, 3, 4, 5, 6]
 |
                |

[6, 2, 3, 4, 5, 1]
       |
          |

[6, 2, 4, 3, 5, 1]
          |
       |

O(n) time and O(1) space. This algorithm is unstable.


Output:
[6, 2, 4, 3, 5, 1]
'''

def moveEvensFront(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        while i < len(arr) and arr[i] % 2 == 0:
            i += 1
        while j >= 0 and arr[j] % 2 == 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [6, 2, 4, 3, 5, 1]
# print(moveEvensFront(arr))

'''
EPI's soln.
This algorithm partitions the array into three parts: even, unclassified and odd. 
As the pointers move, the unclassified portion gets smaller and the even/odd portions get bigger.
The pointers are next_even and next_odd. 

[1, 2, 3, 4, 5, 6] next_even isn't even, so swap next_even and next_odd
 |
                |

[6, 2, 3, 4, 5, 1] we don't know whether next_even is actually pointing to an even number so we don't increment next_even after the swap.
 |                 but we do know that after the swap, next_odd points to an odd number. So we have to decrement next_odd.
             |

[6, 2, 3, 4, 5, 1] 2 is even, so increment next_even. 3 is odd, so perform the swap.
       |
             |

[6, 2, 5, 4, 3, 1] After the swap, we know for sure that next_odd is odd otherwise the swap wouldn't have occurred, so we decrement j.
       | 
          |

[6, 2, 4, 5, 3, 1] Swap and decrement j. at this point, i == j. It doesn't matter whether that element is odd or even.
       | 
       |
'''

def even_odd(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] % 2 == 0: # if even, arr[i] is already at the right place
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i] 
            j -= 1 # we know for sure that arr[j] is odd so it's in the right place. so decrement.
            # we don't increment i because arr[j] before the swap could be odd.
    return arr

# print(even_odd(arr))

'''
5.1. The Dutch National Flag Problem
Parition the array into three parts, there all elements smaller goes before the pivot and all elements bigger goes after the pivot.
O(n) time O(1) space.

Input:
[0, 1, 2, 0, 2, 1, 1]

Output:
[0, 0, 1, 1, 1, 2, 2]

pivot = 1
[0, 1, 2, 0, 2, 1, 1]    
 i
                   j

[0, 1, 2, 0, 2, 1, 1]   # 0 is already in its proper position so increment i
    i
                   j

[0, 1, 2, 0, 2, 1, 1]   # 1 is already in its proper position so increment i.
       i
                   j

 [0, 1, 1, 0, 2, 1, 2]   # 2 isn't in its proper place so swap. We know that el at j is in its proper position so decrement j.
        i
                 j
   
 [0, 1, 1, 0, 2, 1, 2]   
           i
                 j     

 [0, 1, 1, 0, 2, 1, 2]   
              i
                 j     

 [0, 1, 1, 0, 1, 2, 2]   # swap and decrement j
              i
              j     
     
The array is partitioned into two parts: elements smaller than pivot and elements bigger than pivot.
Now move the elements smaller than the pivot to the front of the array.

[0, 1, 1, 0, 1, 2, 2] # this time the algorithm is reversed
 i
                   j

[0, 1, 1, 0, 1, 2, 2] # 2 is in the right place so decrement j
 i
                j                

[0, 1, 1, 0, 1, 2, 2] # 2 is in the right place so decrement j
 i
             j                

[0, 1, 1, 0, 1, 2, 2] # 1 is in the right place so decrement j
 i
          j   

[0, 1, 1, 0, 1, 2, 2] # 0 is not in the right place
 i
          j   

[0, 1, 1, 0, 1, 2, 2] # swap i, j. now the element at i is in the right place, so increment i. 
    i
          j   

[0, 1, 1, 0, 1, 2, 2] # 0 is not in the right place
    i
          j       

[0, 0, 1, 1, 1, 2, 2] # swap i, j. now the element at i is in the right place, so increment i. 
       i
          j       

[0, 0, 1, 1, 1, 2, 2] # 1 is in its proper place, so decrement j. i == j and that element can be on either side of the partition so we're done.
       i
       j     

Since we moved the elements bigger to the end and elements smaller to the front, the elements equal to the pivot naturally fall in place.

This is the partition done in quicksort.
'''

def nationalDutchFlag(arr, pivot):
    i, j = 0, len(arr) - 1

    # partition elements bigger than pivot to the right
    while i < j:
        if arr[i] <= pivot: # in the right position
            i += 1
        else: # after swap, the element at idx j is in the right place, so decrement j
            arr[i], arr[j] = arr[j], arr[i] 
            j -= 1

    i = 0 # for the second pass, we can have j remain as is since the elements after j are greater than pivot
    # partition elements smaller than pivot to the left
    while i < j:
        if arr[j] >= pivot:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    return arr

# arr = [0, 1, 2, 0, 2, 1, 1]
# print(nationalDutchFlag(arr, 1))
# arr = [0, 1, 2, 1, 5, 7, 4, 2, 3, 5, 1, 10]
# print(nationalDutchFlag(arr, 3))

'''
epi soln

pass 1

[0, 1, 2, 0, 2, 1, 1]
 i
 s

[0, 1, 2, 0, 2, 1, 1] swap 
    i
    s

[0, 1, 2, 0, 2, 1, 1]  
       i
    s

[0, 1, 2, 0, 2, 1, 1]  
          i
    s

[0, 0, 2, 1, 2, 1, 1]  
                   i
       s

pass 2 

[0, 0, 1, 1, 1, 2, 2]  
                i                   
            l
'''

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def dutchFlagPartitioning(arr, pivotIdx):
    pivot = arr[pivotIdx]
    print('f', arr)
    # first pass - group elements smaller in the front
    smaller = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            swap(arr, smaller, i)
            smaller += 1
            
    print('a', arr)
    # second pass - group elements bigger in the back
    bigger = len(arr) - 1
    for i in reversed(range(len(arr))): # reversed is necessary because I don't want to swap the 2's that are grouped earlier in the iteration
        if arr[i] > pivot:
            swap(arr, bigger, i)
            bigger -= 1
    print('b', arr)
    return arr 

# arr = [0, 1, 2, 0, 2, 1, 1]
# print(dutchFlagPartitioning(arr, 1))
# arr = [0, 1, 2, 1, 5, 7, 4, 2, 3, 5, 1, 10]
# print(dutchFlagPartitioning(arr, 3))

'''
dutch flag partition problem w/ one pass

[0, 0, 1, 1, 1, 2, 2]
       s
             l
             i                 

'''

def onePassDutchFlagPartitioning(arr, pivotIdx):
    '''
    invariant:
    elements smaller than pivot -> arr[:smaller]
    elements equal to pivot -> arr[smaller: equal]
    unclassified -> arr[equal: larger]
    elements larget than pivot -> arr[larger:]
    '''
    pivot = arr[pivotIdx]
    smaller, larger = 0, len(arr) - 1
    equal = 0
    while equal < larger:
        if arr[equal] < pivot:
            swap(arr, smaller, equal)
            smaller += 1
            equal += 1
        elif arr[equal] > pivot:
            swap(arr, larger, equal)
            larger -= 1
        else:
            equal += 1
    return arr

# arr = [0, 1, 2, 0, 2, 1, 1]
# print(onePassDutchFlagPartitioning(arr, 1))
# arr = [0, 1, 2, 1, 5, 7, 4, 2, 3, 5, 1, 10]
# print(onePassDutchFlagPartitioning(arr, 3))
