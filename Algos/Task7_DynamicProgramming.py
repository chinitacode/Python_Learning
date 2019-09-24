'''
【动态规划】
0-1 背包问题
最小路径和（详细可看 Minimum Path Sum）
编程实现莱文斯坦最短编辑距离
编程实现查找两个字符串的最长公共子序列
编程实现一个数据序列的最长递增子序列

[Practice]
1.1维DP问题：
    53. Maximum Subarray [Easy]
    70.Climbing Stairs [Easy]
        爬楼梯变形：给定n,找到不同将n写成1,3,4相加的问题（顺序matters）
                或：仍然是爬楼梯，一次可以爬1步，3步或者4步



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



'''
53. Maximum Subarray [Easy]
Method1: DP with O(n) time and O(n) space

dp[i]表示以a[i]为结束的子序列的最大和
前面的a[i-1]结束的某个子序列已经取得最大和,如果和是正的,那么继续累加下去才有意义,
否则应该停止累积,从下1个元素重新计算子序列.

step 0 : dp[0] = nums[0]
step i : dp[i] = dp[i-1] + nums[i] if dp[i-1] > 0 else nums[i]

e.g.
input nums: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
final dp:   [-2, 1, -2, 4,  3, 5, 6,  1, 5]
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums.copy()
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)



'''
70.Climbing Stairs [Easy]
DP (Bottom Up)
Time: O(n), Space: O(n)
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return n
        dp = [0]*n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

'''
爬楼梯变形：给定n,找到不同将n写成1,3,4相加的问题（顺序matters）
  或理解为：仍然是爬楼梯，一次可以爬1步，3步或者4步
[分析]
关键还是找到公式dp[i] = dp[i-1] + dp[i-3] + dp[i-4]，
其实可以想成第一步是1有多少种选择，加上第一步是3的选择数，再加第一步是4的可能组合。
'''
def climb_stairs(n):
    dp = [1, 1, 2, 4]
    if n > 4:
        dp += [0]*(n-4)
    for i in range(4, n):
        dp[i] = dp[i-1] + dp[i-3] + dp[i-4]
    return dp[n-1]
