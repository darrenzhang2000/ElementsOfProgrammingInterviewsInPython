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

# O(n) time, where n is the number of bits O(1) space
def parityCheck2(n): # input = binary string
    bin_n = int(n, 2)
    parity = 0
    while bin_n:
        bit = bin_n & 1
        parity ^= bit
        print('bit, parity', n, bit, parity)
        bin_n >>= 1
    return parity

# print(parityCheck2('1011'))

'''
How can we do better? Right now the overhead is having to check every bit. We could improve this by only 
counting the 1's bits.

We can do n&(n-1) to get rid of the last 1 bit.
That would make the time complexity O(k) where k is the number of 1 bits.

00101100 n
00101011 n - 1
00101000 n & n - 1 -> here, we dropped the least significant 1 bit.

'''

def parityCheck3(n):
    bin_n = int(n, 2)
    parity = 0
    while bin_n:
        bin_n = bin_n & (bin_n - 1) # drop least significant 1 bit
        parity = 1 - parity # toggles between 1 and 0
    return parity

# print(parityCheck3('10111'))