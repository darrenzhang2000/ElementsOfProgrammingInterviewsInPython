'''
buy and sell stock twice

input:
[12,11,13,9,12,8,14,13,15]

output:
10

'''

def buy_sell_stock_once(arr, start, end): # O(n) time O(1) space
    if len(arr) <= 1:
        return 0
    maxProfit = 0
    minPrev = arr[start]
    for i in range(start + 1, end):
        maxProfit = max(maxProfit, arr[i] - minPrev)
        minPrev = min(minPrev, arr[i])
    return maxProfit

def buy_sell_stock_twice(arr): # O(n^2) time O(1) space
    maxProfit = 0
    for i in range(1, len(arr) - 1):
        leftProfit = buy_sell_stock_once(arr, 0, i)
        rightProfit = buy_sell_stock_once(arr, i, len(arr))
        maxProfit = max(maxProfit, leftProfit + rightProfit)
    return maxProfit

# arr = [12,11,13,9,12,8,14,13,15]
# print(buy_sell_stock_twice(arr))
# arr = [0,10,0,0, 100]
# print(buy_sell_stock_twice(arr))

'''

[12,11,13,9,12, 8, 14,13,15]
[12,11,11,9, 9, 8, 8, 8, 8]
[15,15,15,15,15,15,15,15,15]
  0  0  2 2  3  3  6  6  7
  7  7  7 7  7  7  2  2  0
'''


def buy_sell_stock_twice2(arr): # O(n) time O(n) space
    if not arr:
        return 0

    minArr = [arr[0]] * len(arr) 
    for i in range(1, len(arr)):
        minArr[i] = min(minArr[i - 1], arr[i])

    maxArr = [arr[len(arr) - 1]] * len(arr)
    for i in range(len(arr) - 2, -1, -1):
        maxArr[i] = max(maxArr[i + 1], arr[i])

    profit = 0
    for i in range(len(arr) - 1):
        trans1 = max(arr[i] - minArr[i], 0)
        trans2 = max(maxArr[i + 1] - arr[i + 1], 0)
        profit = max(profit, trans1 + trans2)
    
    return profit

# arr = [12,11,13,9,12,8,14,13,15]
# print(buy_sell_stock_twice2(arr))
# arr = [0,10,0,0, 100]
# print(buy_sell_stock_twice2(arr))