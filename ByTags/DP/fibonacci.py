'''
509. Fibonacci Number [Easy]

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

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

[Method]: Top-Down Recursion using Memoization(hashmap)
[Time]: O(n). Each number, starting at 2 up to and including N,
is visited, computed and then stored for O(1) access later on.
[Space]: O(n)
Runtime: 28 ms, faster than 85.08% of Python3 online submissions for Fibonacci Number.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Fibonacci Number.
'''
import unittest

class Solution(object):

    def Fibonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            raise ValueError('n shouldn\'t be negative.')
        if n < 2:
            return n
        self.cache = {0:0,1:1}
        return self.helper(n)

    def helper(self, n):
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.helper(n-2) + self.helper(n-1)
        return self.cache[n]


class TestFib(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_value(self):
        self.assertRaises(ValueError, self.sol.Fibonacci,-2)
        self.assertEqual(self.sol.Fibonacci(0), 0)
        self.assertEqual(self.sol.Fibonacci(1), 1)

    def test_n(self):
        self.assertEqual(self.sol.Fibonacci(5), 5)
        self.assertEqual(self.sol.Fibonacci(4), 3)
        self.assertEqual(self.sol.Fibonacci(30), 832040)

if __name__ == '__main__':
    unittest.main()



'''
[Method 2]:

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
