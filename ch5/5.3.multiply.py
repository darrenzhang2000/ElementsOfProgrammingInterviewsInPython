'''
multiple two numbers represented by arrays. useful in cryptography when dealing with large numbers
overflow prevents soln by converting numbers to ints

[1, 2, 3]
[4, 5, 6]


product(arr1, arr2, place)

place = 0
 1  1
[1, 2, 3]
[4, 5, 6]
 7  3  8

place = 1
     1  1
    [1, 2, 3]
    [4, 5, 6]
     6  1  5  0


place = 2
    1
[1, 2, 3]
[4, 5, 6]
 4  9  2 0 0 



'''


'''
first implement helper add before multiply

add
7  3  8
6  1  5
4  9  2


12345+891=13236
 
  11
54321 +  # flip arr1
198   =  # flip arr2
63231    # add them
         # flip back
'''

def add(arr1, arr2):
    reversedArr1 = list(reversed(arr1))
    reversedArr2 = list(reversed(arr2))
    resSum = []
    carry = 0
    for i in range(max(len(arr1), len(arr2))):
        digit1 = reversedArr1[i] if i < len(reversedArr1) else 0
        digit2 = reversedArr2[i] if i < len(reversedArr2) else 0
        remainder = (carry + digit1 + digit2) % 10
        carry = (carry + digit1 + digit2) // 10
        resSum.append(remainder)
    if carry != 0:
        resSum.append(carry)
    return list(reversed(resSum))

# arr1 = list(map(int, str(12345)))
# arr2 = list(map(int, str(891)))
# print(add(arr1, arr2))
    
def multiply(arr1, arr2):
    negative = arr1[0] * arr2[0] < 0
    arr1[0] = abs(arr1[0])
    arr2[0] = abs(arr2[0])
    product = []
    for place in range(len(arr2)):
        product = add(product, multiplyPlace(arr1, arr2, place))
    if negative:
        product[0] *= -1
    return product

def multiplyPlace(arr1, arr2, place):
    resSum = [0 for _ in range(place)]
    idx = len(arr2) - 1 - place
    digit = arr2[idx]
    carry = 0
    for i in reversed(range(len(arr1))):
        remainder = (arr1[i] * digit + carry) % 10
        resSum.append(remainder)
        carry = (arr1[i] * digit + carry) // 10
    if carry != 0:
        resSum.append(carry)
    return list(reversed(resSum))

def intToArray(n):
    negative = n < 0
    absN = list(map(int, str(abs(n))))
    if negative:
        absN[0] *= -1
    return absN

# arr1 = intToArray(123)
# arr2 = intToArray(456)
# print(multiply(arr1, arr2))
# arr1 = intToArray(8)
# arr2 = intToArray(-9)
# print(multiply(arr1, arr2))

'''
EPI soln

[9, 9]
[9, 9]

[0, 0, 8, 1]
i = 1
j = 0
res[3] = 81
res[2] = 8
res[3] = 1

'''

def multiply2(arr1, arr2):
    sign = -1 if (arr1[0] < 0) ^ (arr2[0] < 0) else 0
    arr1[0], arr2[0] = abs(arr1[0]), abs(arr2[0])
    product = [0] * (len(arr1) + len(arr2))
    for i in reversed(range(len(arr1))):
        for j in reversed(range(len(arr2))):
            product[i + j + 1] += arr1[i] * arr2[j]
            product[i + j] += product[i + j + 1] // 10
            product[i + j + 1] %= 10

    idxFirstNonZero = next((i for i, x in enumerate(product) if x != 0))
    product = product[idxFirstNonZero:] or [0]
    return [sign * product[0]] + product[1:]
         

arr1 = intToArray(123)
arr2 = intToArray(456)
print(multiply2(arr1, arr2))
arr1 = intToArray(8)
arr2 = intToArray(-9)
print(multiply2(arr1, arr2))
