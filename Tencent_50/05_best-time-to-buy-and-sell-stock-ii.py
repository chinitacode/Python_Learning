'''
122. best-time-to-buy-and-sell-stock-ii

Method 1: Greedy Algorithm
O(n)
因为可以当天卖出又买入，所以只要能挣钱就买入卖出即可
'''

def maxProfit(prices):
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]
    return profit

'''
Method 2: 峰值法：先找局部最小，再找局部最大，差值即利润
Two pointers
O(n)
'''
def maxProfit(prices):
    profit = 0
    i = 0
    while i < len(prices):
        while i < len(prices) - 1 and prices[i+1] <= prices[i]:
            i += 1
        j = i + 1
        while j < len(prices) - 1 and prices[j+1] > prices[j]:
            j += 1
        profit += prices[j] - prices[i] if j < len(prices) else 0
        i = j + 1
    return profit
