'''
77. Combinations [Medium]
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

[Method 1]: Backtracking
Runtime: 560 ms, faster than 71.00% of Python online submissions for Combinations.
Memory Usage: 13.3 MB, less than 61.54% of Python online submissions for Combinations.
'''
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res, tmp = [], []
        def backtrack(res, tmp, pos, k):
            if k == 0:
                res.append(tmp[:])
                return
            for i in range(pos, n+1):
                tmp.append(i)
                backtrack(res, tmp, i+1, k-1)
                tmp.pop()
        backtrack(res, tmp, 1, k)
        return res
