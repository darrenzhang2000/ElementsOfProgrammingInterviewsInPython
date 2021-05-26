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
print(moveEvensFront(arr))
