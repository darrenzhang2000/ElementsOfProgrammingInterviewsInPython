def buy_and_sell_stock_twice_constant_space(prices):
    min_prices, max_profits = [float('inf')] * 2, [0] * 2
    for price in prices:
        for i in reversed(range(2)):
            max_profits[i] = max(max_profits[i], price - min_prices[i])
            min_prices[i] = min(min_prices[i],
                                price - (0 if i == 0 else max_profits[i - 1]))
            print(price, i, max_profits[i], min_prices[i])
    return max_profits[-1]

arr = [12,11,13,9,12,8,14,13,15]
print(buy_and_sell_stock_twice_constant_space(arr))

# 1.10 variant - compute inverse permutation
# 1.11 variants, 1.12
# all of them ... 
# is valid sudoku pythonic soln
# code spiral ordering fancy soln
# need to implement 5.19 matrix rotation!!!