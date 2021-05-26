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

print(even_odd(arr))