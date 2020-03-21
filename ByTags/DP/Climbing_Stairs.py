'''
---------------------------------------------
70.Climbing Stairs [Easy]

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
---------------------------------------------
[Method 1]: DP (Bottom Up)

[Time]: O(n)
[Space]: O(n)
Runtime: 28 ms, faster than 57.46% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return n
        dp = [0]*(n+1)
        dp[1],dp[2] = 1, 2
        for j in range(3,n+1):
            dp[j] = dp[j-2] + dp[j-1]
        return dp[n]

'''
爬楼梯变形：给定n, 求将n分解为1,3,4相加的总方案数（顺序matters）
  或理解为：仍然是爬楼梯，一次可以爬1步，3步或者4步
[分析]
关键还是找到公式dp[i] = dp[i-1] + dp[i-3] + dp[i-4]，
其实可以想成第一步是1有多少种选择，加上第一步是3的选择数，再加第一步是4的可能组合。
'''
def climb_stairs(n):
    dp = [1, 1, 2, 4] # base cases
    if n > 4:
        dp += [0]*(n-4)
    for i in range(4, n):
        dp[i] = dp[i-1] + dp[i-3] + dp[i-4]
    return dp[n-1]


'''
[Method 3]: 迭代，其实就是fibonacci数列。
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        curr, nxt = 1, 2
        for i in range(1, n):
            curr, nxt = nxt, curr + nxt
        return curr
