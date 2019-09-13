'''
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


[analysis]
The key is to find out the minimal value of the array and the maximal value that comes after the minimal value
O(n)
Runtime: 64 ms, faster than 98.38% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14.9 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0
        for i in range(len(prices)):
            #update the minimal value 
            if prices[i] < minprice:
                minprice = prices[i]
            #update maxprofit with prices come after minprice
            if prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice      
        return maxprofit

#or more concise code:
def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
