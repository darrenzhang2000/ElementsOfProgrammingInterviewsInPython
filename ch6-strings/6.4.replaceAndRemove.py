'''
replace A's with 2 D's and remove B's

[a,b,a,c,_] -> [d,d,d,d,c]

first remove b's
[a,b,a,c,_] -> [a,a,c, _, _] 

[a,a,c, _, _] -> [d,d,c, _, a] 
 |                    |     |

[d,d,d, d, c] 
          ||  

[b,b,a]
 

'''

def replaceAndRemove(size, s):
    removeBs(size, s)
    replaceAs(size, s)
    return s

def removeBs(size, s):
    slow = fast = 0
    while fast < size:
        if s[fast] != 'b':
            s[slow] = s[fast]
            slow += 1
        fast += 1
    for i in range(slow, size):
        s[i] = None
    
def replaceAs(size, s):
    if None not in s: # no 'a's
        return 
    lastElIdx = s.index(None) - 1 
    indexCopyTo = size - 1
    for i in range(lastElIdx, -1, -1):
        if s[i] == 'a':
            s[indexCopyTo - 1: indexCopyTo + 1] = ['d', 'd']
            indexCopyTo -= 2
        else:
            s[indexCopyTo] = s[i]
            indexCopyTo -= 1
            


arr = ['a','b','a','c', None]
arr = ['d']
print(replaceAndRemove(1, arr))
    



