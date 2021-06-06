'''
reverse words in sentence

[A,l,i,c,e, ,l,i,k,e,s, ,B,o,b'] -> ['B,o,b, ,l,i,k,e,s, ,A,l,i,c,e']

first reverse the entire array
then reverse each individual word
'''

from typing import List
def reverseWords(s: List) -> List:
    s.reverse()
    start, end = 0, 0
    while True:
        try:
            end = s.index(" ", start, len(s))
        except ValueError:
            break
        reverseWord(s, start, end)
        start = end + 1
    reverseWord(s, start, len(s))
    return s

def reverseWord(s, start, end):
    print(s, start,end)
    for i in range((end - start) // 2):
        print(i, start + i, end - 1 - i)
        s[start + i], s[end - 1 - i] = s[end - 1 - i], s[start + i]
    print(s, start,end)

        
s = ['A','l','i','c','e',' ','l','i','k','e','s',' ','B','o','b'] 
print(reverseWords(s))
