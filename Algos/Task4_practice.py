'''

1. Two Sum (Easy)

Reverse String （反转字符串）

Reverse Words in a String（翻转字符串里的单词）

String to Integer (atoi)（字符串转换整数 (atoi)）[作为可选]

'''
#1. Two Sum (Easy)
# using hash O(N)
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return map[num[i]], i + 1

        return -1, -1

"""
This way the number of iterations is the smallest because all wanted numbers are stored in a memory.
"""
# Or:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

#Or:
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
