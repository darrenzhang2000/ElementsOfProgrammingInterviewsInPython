'''
compute all valid ip addresses

a decimal string contains digits between 0 and 9.
IP addresses can be written as 4 decimal strings separated by periods. 

add periods to a decimal string so that the resulting string is a valid ip address.
there may be more than 1 valid ip address corresponding to a string

1.9.2.16811 -> invalid because the 4th chunk is > 255
1.9.2.16.811 -> invalid
1.9.2.168.11 -> valid
1.9.2.1681.1 -> invalid
1.9.21.6.811 -> invalid
1.9.21.68.11 -> valid
1.9.21.681.1 -> invalid
1.9.216.8.11 -> valid
1.9.216.81.1 -> valid

'''

def generateValidIPAddresses(s):
    ipAddresses = generateAllIPAddresses(s)
    return filter(validIPAddress, ipAddresses)

def generateAllIPAddresses(s):
    stringAsArr = [c for c in s]
    res = []
    for x in range(1, len(s) - 2):
        for y in range(x + 1, len(s) - 1):
            for z in range(y + 1, len(s)):
                ipAddr = stringAsArr[:x] + ['.'] + stringAsArr[x:y] + ['.'] + stringAsArr[y:z] + ['.'] + stringAsArr[z:]
                res.append("".join(ipAddr))
    return res

def validIPAddress(s):
    parts = s.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if part == "" or not 0 <= int(part) <= 255:
            return False
    return True

s = '19216811'
s = '255255255255'
s = '1111'
    #  0 1 2 3
    #  1 . 1 . 1 . 1
    #    1    2   3
print(generateValidIPAddresses(s))

def dealsWithZeros(s):
    if len(s) > 3:
        return False
    if len(s) == 1 and s[0] == '0':
        return True
    if s[0] == '0':
        return False
    return True
print(dealsWithZeros('255'))