'''
【递归】
通过LeetCode上【70. 爬楼梯】学习（建议）
'''







'''

70. Climbing Stairs
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
'''

'''
Method1: (Top-Down)Recursion using fibonacci without memoization
Time: O(2^n)
Time Limit Exceeded
Note: 之所以会TLE，是因为递归的时候出现了很多次重复的运算。
这种重复计算随着input的增大，会出现的越来越多，时间复杂度也会将以指数的级别上升。
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

'''
# OPTIMIZE: (Top-Down) Recursion + memoization by hash table(global variable)
Time: O(n)
Runtime: 4 ms, faster than 99.78% of Python online submissions for Climbing Stairs.
Memory Usage: 11.9 MB, less than 17.19% of Python online submissions for Climbing Stairs.'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.dic = {0:1, 1:1, 2:2}
        def helper(n):
            if n not in self.dic:
                # 每次递归时只有helper(n-1)是O(n)，
                # 因为前者已经把后者helper(n-2)存入哈希表，所以后者只是O(1)
                self.dic[n] = helper(n-1) + helper(n-2)
            return self.dic[n]
        return helper(n)


'''
Metho2: (Bottom-up) iteration use O(1) space
Time: O(n) Space:O(1)
Runtime: 8 ms, faster than 97.54% of Python online submissions for Climbing Stairs.
Memory Usage: 11.6 MB, less than 100.00% of Python online submissions for Climbing Stairs.
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        curr, next = 1, 1
        for i in range(n):
            curr, next = next, curr + next
        return curr

'''
Method2: (Bottom-up) iteration use list for memoization
Time: O(n) Space:O(n)
Runtime: 8 ms, faster than 97.54% of Python online submissions for Climbing Stairs.
Memory Usage: 11.7 MB, less than 46.88% of Python online submissions for Climbing Stairs.
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0] * (n+1)
        res[0], res[1] = 1, 1
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[-1]

'''
Method3: (Top-Down) Dynamic Programming
Runtime: 4 ms, faster than 99.78% of Python online submissions for Climbing Stairs.
Memory Usage: 11.8 MB, less than 35.94% of Python online submissions for Climbing Stairs.
[思路]
根据TLE的代码进行优化，如果能够将之前的计算好了的结果存起来，之后如果遇到重复计算直接调用结果，
会从之前的指数时间复杂度，变成O(N)的时间复杂度。
[实现]
开辟一个长度为N的数组，将其中的值全部赋值成-1，用-1是因为这一类问题一般都会要你求多少种可能，
在现实生活中，基本不会要你去求负数种可能，所以这里-1可以成为一个很好的递归条件/出口。
然后只要我们的数组任然满足arr[n] == -1，说明我们在n层的数没有被更新，
即就是我们还在向下递归或者等待返回值的过程中，所以我们继续递归直到n-1和n-2的值返回上来。
这里注意我们递归的底层，也就是arr[0]和arr[1]，分别对应n==1和n==2时，即arr[0], arr[1] = 1, 2
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        res = [-1 for i in range(n)]
        res[0], res[1] = 1, 2
        return self.dp(n-1, res)

    def dp(self, n, res):
        if res[n] == -1:
            res[n] = self.dp(n - 1, res) + self.dp(n - 2, res)
        return res[n]
