'''
add 1 to number represented by array

input:
[1, 2, 9]

output:
[1, 3, 0]

clarifying questions:
what to do when there is an overflow? expand size of array or reset to 0?

[1, 9, 9, 9]
          1

[1, 9, 9, 0]
       1

[1, 9, 0, 0]
    1

[2, 0, 0, 0]
 1


'''

def plusOne(arr):
    carry = 1
    for i in reversed(range(len(arr))):
        total = arr[i] + carry
        carry = total // 10
        remainder = total % 10
        arr[i] = remainder
        if carry == 0:
            break

    if carry != 0:
        # arr.insert(0, carry)
        arr.append(0)
        arr[0] = 1
    
    return arr

print(plusOne([9, 8, 9, 9]))