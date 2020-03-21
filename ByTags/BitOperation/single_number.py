'''
136. Single Number [Easy]

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

[Method 1]:异或
Runtime: 88 ms, faster than 67.17% of Python3 online submissions for Single Number.
Memory Usage: 15.4 MB, less than 6.56% of Python3 online submissions for Single Number.
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:return
        res = 0
        for num in nums:
            res ^= num
        return res

'''
或者用上reduce函数：
'''
from functools import reduce
class Solution:
    def singleNumber(self, nums):
        return reduce(lambda a, b : a ^ b, nums)

'''
[Method 2]: 用set()求和
'''
def singleNumber2(self, nums):
    return 2*sum(set(nums))-sum(nums)

'''
[Method 3]:用字典计数
'''
def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key
