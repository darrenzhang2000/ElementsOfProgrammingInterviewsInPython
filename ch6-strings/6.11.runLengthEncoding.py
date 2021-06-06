'''
aaaabcccaa <-> 4a1b3c2a
implement run length encoding and decoding
'''

def runLengthEncode(s):
    res = []
    i = 0
    while i < len(s):
        # get same char
        j = i + 1
        while j < len(s) and s[i] == s[j]:
            j += 1
        count = j - i
        res.append(str(count) + s[i])
        i = j
    return "".join(res)

def runLengthDecode(s):
    res = []
    i = 0
    while i < len(s):
        # get next num
        j = i + 1
        while j < len(s) and s[j].isdigit():
            j += 1
        num = s[i:j]
        i = j 

        # get next string
        while j < len(s) and s[j].isalpha():
            j += 1
        alpha = s[i:j]
        res.append(int(num) * alpha)
        i = j
    return "".join(res)

def runLengthDecode2(s):
    res = []
    count = 0
    for c in s:
        if c.isdigit():
            count = 10 * count + int(c)
        else:
            res.append(count * c)
            count = 0
    return "".join(res)


print(runLengthDecode2("4a1b3c2a"))
print(runLengthEncode("aaaabcccaa"))