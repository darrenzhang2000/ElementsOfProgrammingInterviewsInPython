'''
maximize profit by buying and selling block

input:
[310,315,275,295,260,270,290,230,255,250]

brute force: O(n^2) time, O(1) space

keep track of the minimum at each point and find max that way
[310,315,275,295,260,270,290,230,255,250]
[310,310,275,275,260,260,260,230,230,230]
'''

def buy_sell_stock_once(arr):
    maxProfit = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            maxProfit = max(maxProfit, arr[j] - arr[i])
    return maxProfit

# arr = [310,315,275,295,260,270,290,230,255,250]
# print(buy_sell_stock_once(arr))

def buy_sell_stock_once2(arr):
    if len(arr) <= 1:
        return 0
    maxProfit = 0
    minPrev = arr[0]
    for i in range(1, len(arr)):
        maxProfit = max(maxProfit, arr[i] - minPrev)
        minPrev = min(minPrev, arr[i])
    return maxProfit

arr = [310,315,275,295,260,270,290,230,255,250]
print(buy_sell_stock_once2(arr))