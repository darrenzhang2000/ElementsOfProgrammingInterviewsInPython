import string
import functools

def stringToInt(s):
    '''
    12345
    -12345
    '''
    if not s:
        return
    sign = -1 if s[0] == '-' else 1
    n = 0
    for i in range(len(s)):
        if s[i].isdigit():
            digit = string.digits.index(s[i])
            n += digit * 10**(len(s) - 1 - i)
    return sign * n

def stringToInt2(s):
    if not s:
        return 
    sign = 1
    if s[0] == '-':
        sign *= -1
        s = s[1:]
    return sign * functools.reduce(lambda acc, n: 10 * acc + string.digits.index(n), list(s), 0)

def intToString(n):
    isNegative = False
    if n < 0:
        isNegative = True
        n *= -1
    res = []
    while n:
        res.append(chr(ord('0') + n % 10))
        n /= 10
    res = list(reversed(res))
    return ("-" if isNegative else "") + "".join(res)

print(intToString(-12345))
print(stringToInt2('-1234'))