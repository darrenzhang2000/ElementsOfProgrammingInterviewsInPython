'''
spreadsheets are made of letters A to Z. Compute the integer equivalent

AA -> 1*26^1 + 1*26^0
ZZ -> 26*26^1 + 26^26^0
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