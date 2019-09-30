'''
70. Climbing Stairs [Easy]
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
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

[Method 1]: Recursion + Memorization using global attribute as dictionary (Top down)
Time: O(n), Space: O(n)
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dic = {1:1, 2:2}
        def helper(n):
            if n not in self.dic:
                self.dic[n] = helper(n-1) + helper(n-2)
            return self.dic[n]
        return helper(n)

'''
[Method 2]: DP (Bottom Up)
Time: O(n), Space: O(n)
Runtime: 32 ms, faster than 89.40% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.8 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.
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
[Method 3]: Iteration piggybacking on Fibonacci Number
Time: O(n), Space: O(1)
Runtime: 32 ms, faster than 89.40% of Python3 online submissions for Climbing Stairs.
Memory Usage: 13.9 MB, less than 5.97% of Python3 online submissions for Climbing Stairs.
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        curr, nxt = 1, 2
        for i in range(1, n):
            curr, nxt = nxt, curr + nxt
        return curr
