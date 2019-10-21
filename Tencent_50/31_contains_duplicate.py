'''
217. Contains Duplicate [easy]
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

[method1] hashmap
O(n)
Runtime: 136 ms, faster than 93.10% of Python3 online submissions for Contains Duplicate.
Memory Usage: 21 MB, less than 7.55% of Python3 online submissions for Contains Duplicate.
'''
from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = Counter(nums)
        return len(dic) != len(nums)

'''
[method2]using set

'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(set(nums)) < len(nums) else False
