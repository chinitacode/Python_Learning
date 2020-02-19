# Unbounded Knapsack Problem
def knapsack2(weight, value, capacity):
    '''

    >>> knapsack2([], [], 10)
    0
    >>> knapsack2([3], [10], 0)
    0
    >>> knapsack2([4], [15], 4)
    15
    >>> knapsack2([4], [15], 10)
    30
    >>> knapsack2([4], [15], 3)
    0
    >>> weight = [1, 50]
    >>> value = [1, 30]
    >>> capacity = 100
    >>> knapsack2(weight, value, capacity)
    100
    >>> weight = [1, 3, 4, 5]
    >>> value = [10, 40, 50, 70]
    >>> capacity = 8
    >>> knapsack2(weight, value, capacity)
    110
    
    '''
    n = len(weight)
    if n < 1 or capacity < 1: return 0
    dp = [0]*(capacity + 1)
    for i in range(n):
        for j in range(weight[i], capacity+1):
            dp[j] = max(dp[j], dp[j - weight[i]]+value[i])
    #print(dp)
    return dp[capacity]


#完全硬币找零问题
def coinChange2(coins, amount):
    '''
    >>> coinChange2([2], 1)
    -1
    >>> coins = [2, 3, 5]
    >>> coinChange2(coins, 10)
    2
    >>> coinChange2(coins, 11)
    3
    >>> coinChange2(coins, 0)
    0
    >>> coinChange2([1, 2, 5], 10)
    2
    >>> coinChange2([1, 2, 5], 11)
    3
    '''
    
    if len(coins) < 1: return -1
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j-coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1
