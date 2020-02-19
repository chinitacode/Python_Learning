#0-1 背包问题
def knapsack1(weight, value, capacity):
    '''

    >>> knapsack1([], [], 10)
    0
    >>> knapsack1([3], [10], 0)
    0
    >>> knapsack1([4], [15], 4)
    15
    >>> knapsack1([4], [15], 10)
    15
    >>> knapsack1([4], [15], 3)
    0
    >>> weight = [1, 2, 3, 8, 7, 4]
    >>> value = [20, 5, 10, 40, 15, 25]
    >>> capacity = 10
    >>> knapsack1(weight, value, capacity)
    60
    >>> weight = [10, 20, 30]
    >>> value = [60, 100, 120]
    >>> capacity = 50
    >>> knapsack1(weight, value, capacity)
    220

    '''

    #winpty python -m doctest knapsack_problem_0_1.py
    n = len(weight)
    if n < 1 or capacity < 1: return 0
    dp = [0]*(capacity + 1)
    for item in range(n):
        for j in range(capacity, weight[item]-1, -1):
            dp[j] = max(dp[j], dp[j - weight[item]] + value[item])
    #print(dp)
    return dp[capacity]


#0-1 硬币找零问题
def coinChange1(coins, amount):
    '''
    >>> coinChange1([2], 1)
    -1
    >>> coins = [2, 3, 5]
    >>> coinChange1(coins, 10)
    3
    >>> coinChange1(coins, 11)
    -1
    >>> coinChange1(coins, 0)
    -1
    >>> coins = [2, 1, 2, 3, 5]
    >>> coinChange1(coins, 10)
    3
    >>> coinChange1(coins, 11)
    4
    >>> coinChange1(coins, 5)
    1
    >>> coinChange1(coins, 6)
    2
    '''
    
    n = len(coins)
    if n < 1 or amount < 1: return -1
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(amount, coin-1, -1):
            dp[j] = min(dp[j], dp[j-coin] + 1)
    print(dp)
    return dp[amount] if dp[amount] != float('inf') else -1



