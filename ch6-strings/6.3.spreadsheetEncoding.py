'''
spreadsheets are made of letters A to Z. Compute the integer equivalent

AA -> 1*26^1 + 1*26^0
ZZ -> 26*26^1 + 26^26^0

the reduce implemention would work by multiplying the accumulator by 26 and adding the int representation of the current char
'''

def computeSpreadsheetEncoding(w):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = 0
    for i in range(len(w)):
        power = len(w) - 1 - i
        cIdx = letters.index(w[i])
        n += (cIdx + 1) * 26**power
    return n

print(computeSpreadsheetEncoding('AA'))
print(computeSpreadsheetEncoding('ZZ'))
print(computeSpreadsheetEncoding('A'))

def ss_decode_col_id(w: str) -> int:
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n = 0
    for i in range(len(w)):
        cIdx = letters.index(w[i])
        n = n * 26 + cIdx + 1
    return n


from functools import reduce
def ss_decode_col_id2(w: str) -> int:
    return reduce(lambda acc, c: 26 * acc + ord(c) - ord('A') + 1 , w, 0)

