'''
takes in a valid Roman number string and returns the integer it corresponds to.
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
Roman numbers have to be in nondecreasing order with the following exceptions:
- I can immediately precede V and X
    - IX = 9, IV = 4
- X can immediately precede L and C
    - XL = 40, XC = 90
- C can immediately precede D and M
    - CD = 400, CM = 900

Examples:
XXXXXIIIIIIIII = 59
LVIIII = 59
LIX = 59
'''

def romanToInteger(s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    exceptions = {'IX': 9, 'IV': 4, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    total = 0
    toContinue = False
    for i, c in enumerate(s):
        if toContinue:
            toContinue = False
            continue
        if i + 1 < len(s) and s[i:i+2] in exceptions:
            total += exceptions[s[i:i+2]]
            toContinue = True
        else:
            total += values[c]
    return total

s = 'XXXXXIIIIIIIII'
s = 'LVIIII'
s = 'LIX'
print(romanToInteger(s))

def romanToInteger2(s: str) -> int:
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i in range(len(s) - 1, -1, -1):
        value = values[s[i]]
        total += -1 * value if i + 1 < len(s) and values[s[i]] < values[s[i + 1]] else value
    return total

print(romanToInteger2(s))