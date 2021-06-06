'''
reverse words in sentence

[A,l,i,c,e, ,l,i,k,e,s, ,B,o,b'] -> ['B,o,b, ,l,i,k,e,s, ,A,l,i,c,e']

first reverse the entire array
then reverse each individual word
'''

from typing import List
def reverseWords(s: List[str]) -> List[str]:
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
    for i in range((end - start) // 2):
        s[start + i], s[end - 1 - i] = s[end - 1 - i], s[start + i]

s = ['A','l','i','c','e',' ','l','i','k','e','s',' ','B','o','b'] 
# print(reverseWords(s))


'''
epi soln
reverserange is a useful method that can be reused. 
note: clarify if reverse() method is allowed
'''

def reverseWord2(s: List[str]) -> List[str]:
    def reverseRange(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
    
    reverseRange(s, 0, len(s) - 1)
    start, end = 0, 0
    while True:
        try:
            end = s.index(" ", start, len(s))
        except ValueError:
            break
        reverseRange(s, start, end - 1)
        start = end + 1
    reverseRange(s, start, len(s) - 1) # reverse last word
    return s

#print(reverseWord2(s))

def reverseWord3(s: List[str]) -> List[str]:
    def reverseRange(s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
    
    reverseRange(s, 0, len(s) - 1)
    start, end = 0, 0
    while True:
        end = start
        while end < len(s) and end != ' ':
            end += 1
        if end == len(s):
            break
        reverseRange(s, start, end - 1)
        start = end + 1
    reverseRange(s, start, len(s) - 1) # reverse last word
    return s

print(reverseWord3(s))
