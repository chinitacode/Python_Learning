'''
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

[Method 1]: backtracking (TLE)
'''
import unittest
class Solution:
    def threeSum(self, nums):
        result, tmp = [], []
        if len(nums) < 3: return result
        nums.sort()
        def backtrack(result, tmp, nums, pos):
            if len(tmp) == 3 :
                if sum(tmp) == 0 and tmp not in result:
                    result.append(tmp[:])
                return
            else:
                for j in range(pos, len(nums)):
                    tmp.append(nums[j])
                    backtrack(result, tmp, nums, j+1)
                    tmp.pop()
        backtrack(result, tmp, nums, 0)
        return result

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self._f = Solution().threeSum

    def test_less_than_three(self):
        self.assertEqual(self._f([]), [])
        self.assertEqual(self._f([-3,0]), [])

    def test_zeros(self):
        self.assertEqual(self._f([-1,0,1,0,2,0,-1,-4]), [[-1,-1,2],[-1,0,1],[0,0,0]])
        self.assertEqual(self._f([-1,0,1,0,2,-1,-4]), [[-1,-1,2],[-1,0,1]])
        self.assertEqual(self._f([-1,1,0,2,-1,-4]), [[-1,-1,2],[-1,0,1]])

    def test_duplicates(self):
        self.assertEqual(self._f([-1,0,1,0,2,0,0,-1,-4]), [[-1,-1,2],[-1,0,1],[0,0,0]])
        self.assertEqual(self._f([-2,0,0,2,2]),[[-2,0,2]])

if __name__ == '__main__':
    unittest.main()
