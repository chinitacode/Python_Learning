'''
90. Subsets II [Medium]

Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, tmp, n = [], [], len(nums)
        nums.sort()
        def backtrack(res, tmp, pos):
            res.append(tmp[:])
            for i in range(pos, n):
                if i != pos and nums[i] == nums[i-1]: continue
                tmp.append(nums[i])
                backtrack(res, tmp, i+1)
                tmp.pop()
        backtrack(res, tmp, 0)
        return res
