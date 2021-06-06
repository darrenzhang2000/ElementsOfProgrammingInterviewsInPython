'''
given substring s and text string t, find the first occurence of s in t.

s = world
t = helloworldworld

brute force: O(n^2) time using 2 for loops. O(1) space.

hint: create a function signature

create a unique hash for 'world'. loop through the text string and see if it corresponds to anything
time O(s + t) space O(1)

if n = 3
first hash consists of idx 0, 1, 2
wor
world
start at i = 2, compute hash, then update hash


need protection against hash collision by comparing the strings if hashes are equal
'''

def rabin_karp(t: str, s: str) -> int:
    if len(s) > len(t): return -1

    n = len(s)
    sHash = computeHash(s, 0, n)
    curHash = computeHash(t, 0, n)
    for i in range(n - 1, len(t) - 1):
        startIdx = i - len(s) + 1
        if curHash == sHash:
            return startIdx
        curHash = 37 * (curHash - ord(t[startIdx]) * 37 ** (n - 1)) + ord(t[i + 1]) # rolling hash
    # compute hash once more
    if curHash == sHash:
        return len(t) - n
    return -1

def computeHash(s, start, end):
    n = 0
    for i in range(start, end):
        n = 37 * n + ord(s[i])
    return n


s = "CGC"
t = "GACGCCA"
print(rabin_karp(t, s))