'''
given two bases b1 and b2, and a number in base b1, convert that number to base b2.

let b1 = 2, b2 = 3 n = 1100
conv2 to base 10 -> 0*2^0+0*2^1+1*2^2+1*2^3 = 2 + 8 = 10

512 to base 2
512/2 = 256 R 0
256/2 = 128 R 0
128/2 = 64 R 0
64/2 = 32 R 0
32/2 = 16R0
16/2=8R0
8/2=4R0
4/2=2R0
2/2=1R0
1/2=0R1
1000000000

'''

def baseConv(b1, b2, n):
    base10N = convToBase10(b1, n)
    
    return convToBaseB2From10(b2, base10N)

def convToBase10(b1, n):
    strn = str(n)
    total = 0
    for i in range(len(strn)):
        power = len(strn) - 1 - i
        total +=  int(strn[i]) * b1**power
    return total

def convToBaseB2From10(b2, n):
    res = []
    while n:
        res.append(str(n % b2))
        n //= b2
    return int("".join(list(reversed(res))))

print(baseConv(2, 2, 110))
