'''
parity check
'''
def parityCheck(n):
    even = True
    while n:
        bit = n & 1
        if bit == 1:
            even = not even
        n >>= 1
    return 0 if even else 1

def parityCheck2(n):
    bin_n = int(n, 2)
    parity = 0
    while bin_n:
        bit = bin_n & 1
        parity ^= bit
        print('bit, parity', n, bit, parity)
        bin_n >>= 1
    return parity

print(parityCheck2('1011'))