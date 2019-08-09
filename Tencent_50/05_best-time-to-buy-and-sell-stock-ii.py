'''
122. best-time-to-buy-and-sell-stock-ii

Method 1: Greedy Algorithm, O(n)
Idea：
You can do it on a day-to-day basis.
If buying on day 1 and selling on day 2 is profitable, do it.
If buying on day 2 and selling on day 3 is profitable, do it. And so on.
Yes, you can do both day1-to-day2 and day2-to-day3,
even though there are multiple transactions on day
2. Either think of it as selling first and then buying later on that day,
or think of it as keeping instead of selling+buying.
因为可以当天卖出又买入，所以只要能挣钱就买入卖出即可
'''
def maxProfit(prices):
    if not prices or len(prices) is 1:
        return 0
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            profit += prices[i + 1] - prices[i]
    return profit

# One-liner Solution(Use zip()):
def maxProfit(self, prices):
    return sum(b-a for a,b in zip(prices,prices[1:])if b>a)
    
#Or:
def maxProfit(self, prices):
    return sum(max(b-a,0)for a,b in zip(prices,prices[1:]))

'''
Method 2: 峰值法：先找局部最小，再找局部最大，差值即利润
Two pointers
O(n)
'''
def maxProfit(prices):
    if not prices or len(prices) is 1:
        return 0
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
