'''
【动态规划】
0-1 背包问题
最小路径和（详细可看 Minimum Path Sum）
编程实现莱文斯坦最短编辑距离
编程实现查找两个字符串的最长公共子序列
编程实现一个数据序列的最长递增子序列





Note:
递归不是动态规划，不能混淆，二者有相通的地方:递归是自顶向下，动归是自底向上。
动归是递归综合备忘录算法以后的反向思维形式。
动态规划算法通常基于一个递推公式及一个或多个初始状态。
当前子问题的解将由上一次子问题的解推出。
使用动态规划来解题只需要多项式时间复杂度， 因此它比回溯法、暴力法等要快许多。
'''

'''
1. 0-1背包问题
假设我们有n件物品，分别编号为0, 2...n-1,每个只有1件。
其中编号为i的物品价值为value[i]，它的重量为weight[i]。
为了简化问题，假定价值和重量都是整数值。
现在，假设我们有一个背包，它能够承载的重量是capacity。
现在，我们希望往包里装这些物品，使得包里装的物品价值最大化，那么我们该如何来选择装的东西呢？

[思路]:
1.首先我们先构建一个表格dp[i][j]，横轴为各个可选择的物品，纵轴为背包的容纳重量（从1到背包的实际最大容纳）。
dp[i][j]表示前i个物品放入容量为j的背包中可以获得的最大价值。
2.状态转移方程为：
dp[i][j] = max{dp[i-1][j], dp[i-1][j-weight[i]] + value[i]}
即，“将前i件物品放入容量为j的背包中”这个子问题，若只考虑第i件物品的策略（放或者不放），
则可转化为一个只牵扯前i-1件物品的问题：
1.若不放当前的第i件物品，则问题转化为“前i-1件物品放入容量为j的背包中”，价值为dp[i-1][j]；
2.若放当前的第i件物品，则问题转化为“先将前i-1件物品放入剩下容量为j-weight[i-1]的背包中，再放入当前第i件物品”，
价值为dp[i-1][j-weight[i]] + value[i]。

[优化空间复杂度]：
以上方法的时间和空间复杂度都为O(n*capacity),其中时间复杂度基本已经不能再优化了，
但空间复杂度却可以优化到O(capacity)。

因为dp[i][j]只和上一层的两个状态有关，所以可以将状态转化为一维数组：
dp[j] = max(dp[j],dp[j-weight[i]] + value[i])；
即要推dp[j],必须保证dp[j]是从dp[j-weight[i]]推出来的。
如果j是顺序递增的，则dp[i][j]是由dp[i][j-weight[i]]推出来的，并非由原来的dp[i-1][j-weight[i]]推导得到的。
E.g.
开始循环前，即背包为空时，dp[0]到最大容量dp[5]的值都为0.
开始循环后，我们需要比较dp[j]（即循环前的值）和dp[j-weight[i]] + value[i]；
因为是顺序循环，j-weight[i] < j, 因此dp[j-weight[i]]会成为前面才刚刚被赋值过得值，
例如当i = 0，
从j=1(至少要让背包容量大于等于物品重量，不然为负没有意义)开始循环，dp[1] = max(dp[1],dp[1-1]+1500) = max(0,1500) = 1500，
（即dp[0][1] = 1500，即背包容量为1时刚好可以放第0件物品，所获得的最大价值为该物品的价值1500.）
然后dp[2] = max(dp[2], dp[2-1] + 1500) = max(0, dp[1] + 1500) = 1500 + 1500 = 3000,
注意！！！
这个时候的dp[j-weight[i]]就成了dp[1],而这个dp[1]是我们刚才才更新的值，是当前的dp[i],并不是由dp[i-1]得到的，
而且此时我们明明只是想把第一个物品（i=0）放进容量为2的背包里，得到的最大价值只是第一个物品的价值，即1500而已，
又怎么可能是3000？所以由此可知0-1背包问题中j不可顺序循环，而是逆序。

https://blog.csdn.net/xiajiawei0206/article/details/19933781

'''
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
    return dp[capacity]


'''
如果改成硬币找零问题：01硬币找零问题（01背包）
给定不同面额的硬币 coins 和总金额 m。每个硬币最多选择一次。
计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

同理，dp[i][j]表示选取当前第i个硬币能凑成总金额为j时最少的硬币个数，
即不拿当前第i个硬币时只用之前的硬币可以凑成j块钱所需最少硬币个数dp[i-1][j]，
与拿当前第i个硬币加上拿之前的硬币凑成j-Coins[i]块钱的硬币数量之和dp[i-1][j-coins[i]] + 1 的最小值。
即写成状态转移方程如下：
dp[i][j] = min(dp[i-1][j], dp[i-1][j-coins[i]] + 1)

同样，我们来优化空间复杂度，依然必须从最大总金额amount开始逆序枚举（枚举到当前硬币i的比值，不然j-coins[i]为负没有意义）。
dp[j] = min(dp[j], dp[j-coins[i]] + 1)
因为这道题是求最少硬币个数，在状态转移方程中用的是min()，所以初始化dp矩阵时给每个值都设为最大值float('inf'),
边界情况为dp[0] = 0, 表示凑出金额为0的最小个数是0个。(但是若本身输入amount为0，则没有硬币组合，返回-1)
最后检查dp[amount], 如果值为'inf', 则说明找不到硬币组合，输出-1，反之才输出相应硬币组合的个数。

[注意]：其实在主循环循环到最后一个硬币时的从amount开始的内循环的第一步就可以结束了，因为我们只需要dp[amount]，
但是接着循环的话可以更新其他amount的硬币组合，毕竟多考虑了一个硬币的情况。

'''
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
