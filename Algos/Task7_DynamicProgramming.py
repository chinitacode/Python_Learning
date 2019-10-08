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
# n个物体的重量(w[0]无用)
weight = [1, 4, 3, 1]
# n个物体的价值(p[0]无用)
value = [1500, 3000, 2000, 2000]
# 计算n的个数
n = len(weight) - 1
# 背包的载重量
capacity = 5
# 装入背包的物体的索引
x = []

def bag_dynamic(weight, value, capacity, x):
    n = len(weight)
    weight.insert(0, 0)
    value.insert(0, 0)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if j >= weight[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
            else:
                dp[i][j] = dp[i - 1][j]
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] > dp[i - 1][j]:
            x.append(i)
            j = j - weight[i]

    return dp[n][capacity]
