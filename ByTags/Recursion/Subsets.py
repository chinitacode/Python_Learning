'''
78. Subsets [Medium]

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

[Method 1]: recursion
[Time]: O(2^n), to generate all subsets and then copy them into output list.
[Space]: O(2**n)
Runtime: 28 ms, faster than 88.51% of Python3 online submissions for Subsets.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Subsets.

For a given number, it could be present or absent (i.e. binary choice) in a subset solution.
As as result, for NN numbers, we would have in total 2**n choices (solutions).
[注意]：
在遍历res里的元素时，因为我们一直在给res加东西，所以res是一直变化的，那么就会陷入死循环，
所以我们只能遍历res的深拷贝res[:]!
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums: # O(n)
            for e in res[:]: # O(2**n)
                res.append(e + [num])
        return res
