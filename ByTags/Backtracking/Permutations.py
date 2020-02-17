'''
46. Permutations [Medium]
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]

Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]


[Method 1]: Backtracking
[Time]: O(N!)
[Time]: O(N!)
Runtime: 40 ms, faster than 58.87% of Python3 online submissions for Permutations.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Permutations.
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, tmp = [], []
        def backtrack(res, tmp, pos, nums):
            if not nums:
                res.append(tmp[:])
                return
            for i in range(len(nums)): # 每次递归nums长度都会变化，所以不能用先计算好了的n
                tmp.append(nums[i])
                backtrack(res, tmp, i + 1, nums[:i] + nums[i+1:])
                tmp.pop()
        backtrack(res, tmp, 0, nums)
        return res
'''
[Method 2]: Iteration
[Time]: O(N*2*N!) == O(N)
[Space]: O(N!)
Runtime: 28 ms, faster than 99.28% of Python3 online submissions for Permutations.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Permutations.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        #iterate through the element in nums, each time insert one element:
        for n in nums:
            #create an empty list to store the temporary element permutated
            tmp = []
            # insert the new number based on the previous element permutated
            for e in res:
                for i in range(len(e) + 1):
                    #insert n at the position of i of element e by creating a
                    # new element and append it to tmp
                    tmp.append(e[:i] + [n] + e[i:])
            # update res
            res = tmp
        return res
