'''
78. Subsets [Medium] 类combination提醒，通过pos来添加后面的元素

Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]

Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

[Method 2]: Backtracking
[Time]: O(n*2^n), to generate all subsets and then copy them into output list.
[Space]: O(2**n), to keep all the subsets, since each of n elements could be present or absent.
Runtime: 32 ms, faster than 68.60% of Python3 online submissions for Subsets.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Subsets.
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, tmp, n = [], [], len(nums)
        def backtrack(res, tmp, pos):
            res.append(tmp[:])
            for i in range(pos, n):
                tmp.append(nums[i])
                backtrack(res, tmp, i+1)
                tmp.pop()
        backtrack(res, tmp, 0)
        return res
