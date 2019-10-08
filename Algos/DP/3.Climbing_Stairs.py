'''
---------------------------------------------
70.Climbing Stairs [Easy]
---------------------------------------------
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


'''
