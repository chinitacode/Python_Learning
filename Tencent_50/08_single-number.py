'''
136. Single Number
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

A number XOR itself will get result 0. And a number XOR 0 will get itself.
For example,
>>> 1 ^ 1
0
>>> 0 ^ 2
2

In this way, if we XOR numbers with each other: two identical numbers XOR to 0,
the standard will be the single number finally.
known that A XOR A = 0 and the XOR operator is commutative,
the solution will be very straightforward.
'''
#Version 1
def singleNumber(self, nums):
    res = 0
    for num in nums:
        res ^= num
    return res

#Version 2
from functools import reduce

class Solution:
    def singleNumber(self, nums):
        return reduce(lambda a, b : a ^ b, nums)

#Version 3
def singleNumber(self, nums):
    return reduce(operator.xor, nums)

'''
Other methods:
'''
def singleNumber1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0)+1
    for key, val in dic.items():
        if val == 1:
            return key

def singleNumber2(self, nums):
    return 2*sum(set(nums))-sum(nums)
