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
