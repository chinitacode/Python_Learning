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
假设我们有n件物品，分别编号为1, 2...n。
其中编号为i的物品价值为value[i]，它的重量为weight[i]。
为了简化问题，假定价值和重量都是整数值。
现在，假设我们有一个背包，它能够承载的重量是capacity。
现在，我们希望往包里装这些物品，使得包里装的物品价值最大化，那么我们该如何来选择装的东西呢？

[思路]
1.首先我们先构建一个表格dp[i][j]，横轴为背包的容纳重量（从1到背包的实际最大容纳），纵轴为各个可选择的物品。
而表格中的每个单元格表示的是使用i与前的物品、且保证总重量不大于j情况下背包能容纳物品的最大价值。
2.尝试填充完毕后，我们可以得到一个结论：
在i行j列的最大值可以说是（i-1行[即不取i物品]j列的值) 和 (i物品的价值 + i-1行j-i物品价值列的值[即取了i物品的价值])，
写成状态转移方程即为：`dp[i][j] = max{dp[i-1][j], dp[i-1][j-value[i]] + value[i]}

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
