'''
1. Two Sum [Easy]
Given an array of integers,
return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].


[注意]：
输入:
[3,2,4]
6
输出
[0,0]
预期结果
[1,2]

[Method 1]: dictionary
注意，数组可能存在重复元素，如nums = [3,3,9]，但是字典只会记录一个相同的元素作为key，
并且其value为最后出现元素的值（不断地更新），所以当target = 6时，
因为我们最后遍历数组时是从第一个3开始遍历的，这个时候如果3存在于字典中，
那么其索引必然是另外一个3（后面的元素）的索引。
但是为了避免Nums = [1,3,9], target = 6时出现的3 == 6-3的情况，所以我们必须要在返回前判断两个索引是否相同。
[Time]: O(2n) == O(n)
[Space]: O(n)
Runtime: 44 ms, faster than 92.55% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 11.16% of Python3 online submissions for Two Sum.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if (target - num) in d and i != d[target - num]:
                return [i, d[target - num]]
        return []

'''
[优化版]：
因为前者需要遍历两次数组，可以看是否可以只遍历一次：
Runtime: 40 ms, faster than 97.99% of Python3 online submissions for Two Sum.
Memory Usage: 14 MB, less than 65.35% of Python3 online submissions for Two Sum.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wanted = {}
        for i, num in enumerate(nums):
            if num in wanted: # 判断num是否是为了凑齐target而被需要的另一个数
                return [wanted[num], i]
            wanted[target - num] = i
        return []
