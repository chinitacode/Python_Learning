'''
47. Permutations II [Medium]

Given a collection of numbers that might contain duplicates,
return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

[Method 1]: Backtracking
可以像Subsets II一样，在遍历元素的时候通过判断是否与上一个元素相同来去重，
但是因为nums并未排好序，有可能会遇到如[3,3,0,3]这种情况，所以我们需要先排列nums。
Runtime: 52 ms, faster than 81.81% of Python3 online submissions for Permutations II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Permutations II.
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, tmp, n = [], [], len(nums)
        nums.sort()
        def backtrack(res, tmp, nums):
            if not nums:
                res.append(tmp[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                backtrack(res, tmp, nums[:i] + nums[i+1:])
                tmp.pop()
        backtrack(res, tmp, nums)
        return res

'''
[Method 2]: Iteration(不需要排序)
Runtime: 44 ms, faster than 98.26% of Python3 online submissions for Permutations II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Permutations II.
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            tmp = []
            for e in res:
                for i in range(len(e)+1):
                    tmp.append(e[:i] + [num] + e[i:])
                    if i < len(e) and num == e[i] : break # 直接break来遍历下一个e，因为前面已经有了的那个num已经与剩下的元素全排列过了
            res = tmp
        return res
