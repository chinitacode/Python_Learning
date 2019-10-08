'''
【递归】
- 1.编程实现斐波那契数列求值 f(n)=f(n-1)+f(n-2)
  1.2 解leetcode70.爬楼梯
  1.3 解leetcode198.入室抢劫
- 编程实现求阶乘 n!
- 编程实现一组数据集合的全排列

---------------------------------------
#1.
509. Fibonacci Number [Easy]
---------------------------------------
The Fibonacci numbers,
commonly denoted F(n) form a sequence,
called the Fibonacci sequence,
such that each number is the sum of the two preceding ones,
starting from 0 and 1.
That is,
F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.
Given N, calculate F(N).

Example 1:
Input: 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:
Input: 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:
Input: 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
Note:
0 ≤ N ≤ 30.
[Method 1]: pure recursion (slowest) (Top Dowm)
Time: O(2^n), Space: O(2^n)
Runtime: 1336 ms, faster than 5.07% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.7 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.
'''
class Solution:
    def fib(self, N: int) -> int:
        if N < 0: return
        if N == 0: return 0
        if N == 1: return 1
        return self.fib(N-1) + self.fib(N-2)


'''
[Method 2]: Dynamic Programming(Bottom Up)
Time: O(n), Space: O(n)
Runtime: 32 ms, faster than 91.17% of Python3 online submissions for Fibonacci Number.
Memory Usage: 14 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.
'''
class Solution:
    def fib(self, N: int) -> int:
        if N < 0: return
        dp = {}
        dp[0] = 0
        dp[1] = 1
        for i in range(2, N+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[N]


'''
[Method 3]: Iteration
Time: O(n), Space: O(1)
Runtime: 32 ms, faster than 91.17% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.8 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.
'''
class Solution:
    def fib(self, N: int) -> int:
        curr, nxt = 0, 1
        for i in range(N):
            curr, nxt = nxt, curr + nxt
        return curr


'''
[Method 4]: Matrix Exponentiation
[Intuition]
Use Matrix Exponentiation to get the Fibonacci number from the element at (0, 0) in the resultant matrix.
In order to do this we can rely on the matrix equation for the Fibonacci sequence,
to find the Nth Fibonacci number:
( 1 1  ^ n       ( F(n+1)  F(n)
  1 0 )      =     F(n)    F(n-1) )

[Algorithm]
Check if N is less than or equal to 1. If it is, return N.
Use a recursive function, matrixPower, to calculate the power of a given matrix A.
The power will be N-1, where N is the Nth Fibonacci number.
The matrixPower function will be performed for N/2 of the Fibonacci numbers.
Within matrixPower, call the multiply function to multiply 2 matrices.
Once we finish doing the calculations, return A[0][0] to get the Nth Fibonacci number.

Time complexity : O(logN). By halving the N value in every matrixPower's call to itself,
we are halving the work needed to be done.
Space complexity : O(logN).
The size of the stack in memory is proportionate to the function calls to matrixPower
plus the memory used to account for the matrices which takes up constant space.

Runtime: 32 ms, faster than 91.17% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.8 MB, less than 5.80% of Python3 online submissions for Fibonacci Number.
'''
class Solution:
    def fib(self, N: int) -> int:
        if (N <= 1):
            return N

        A = [[1, 1], [1, 0]]
        self.matrix_power(A, N-1)

        return A[0][0]

    def matrix_power(self, A: list, N: int):
        if (N <= 1):
            return A

        self.matrix_power(A, N//2)
        self.multiply(A, A)
        B = [[1, 1], [1, 0]]

        if (N%2 != 0):
            self.multiply(A, B)

    def multiply(self, A: list, B: list):
        x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
        y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
        z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
        w = A[1][0] * B[0][1] + A[1][1] * B[1][1]

        A[0][0] = x
        A[0][1] = y
        A[1][0] = z
        A[1][1] = w


'''
[Method 5]: Math
Intuition Using the golden ratio, a.k.a Binet's forumula:
φ= (1+sqrt(5))/2	≈ 1.6180339887....
'''
class Solution:
  def fib(self, N):
  	golden_ratio = (1 + 5 ** 0.5) / 2
  	return int((golden_ratio ** N + 1) / 5 ** 0.5)


'''
---------------------------------------
#1.2
70. Climbing Stairs [Easy]
---------------------------------------
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


'''
---------------------------------------
#1.3
198. House Robber [Easy]
---------------------------------------
Recursive Solution: (Top down)
强盗有两个选择： a).抢劫当前房子； b).不抢劫当前房子。
如果选a,则强盗不能抢劫前一个房子，但是可以安全地抢劫前两个房子，
并且获得最大收益为当前房子的价值和抢劫往前数两个房子时的最大收益；
如果选b，则强盗可以获得抢劫前一个房子时的最大收益和接着抢劫挨着的房子。
总结下来，获得的最大收益为以下的最大值：
    1).现在房子的价值+抢劫往前数两个房子的收益
    2).抢劫前一个房子的收益
rob(i) = max( rob(n - 2) + currentHouseValue, rob(n - 1) )
'''
#Time Limit Exceeded
class Solution:
    def rob(self, nums: List[int]) -> int:
        def recur(nums, n):
            if n < 1: return 0
            return max(recur(nums, n-2) + nums[n-1], recur(nums, n-1))
        return recur(nums, len(nums))

'''
Optimized code: Recursion + Memorization (Top down)
Time: O(n); Space: O(n)
Runtime: 36 ms, faster than 80.99% of Python3 online submissions for House Robber.
Memory Usage: 14 MB, less than 9.09% of Python3 online submissions for House Robber.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dict = {}
        def recur(nums, n):
            if n < 1: return 0
            if n not in self.dict:
                self.dict[n] = max(recur(nums, n-1), recur(nums, n-2) + nums[n-1])
            return self.dict[n]
        return recur(nums, len(nums))
