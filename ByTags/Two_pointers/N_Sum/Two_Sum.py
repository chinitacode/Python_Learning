'''
1. 两数之和 [简单]
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，
并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

[Method 1] 字典（空间换时间）
[Time]: O(N)
[Space]: O(N)
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            if target-num in visited:
                return [visited[target-num], i]
            visited[num] = i
        return []


'''
[Method 2]: Two-Pointer
双指针用法只能用于数组是排好序的或者数组未排序但是只要求返回和为target的数值而非索引，
因为排好序后索引就乱了，就算是先用一个字典记录其value:index，遇到有duplicates的情况，
字典中的同一个value只会记录下它最新的index，当2nums = target的时候就会出错。
'''
# 如果只要求返回满足和为target的两个num：
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        if not nums or nums [0] > target: return []
        i, j = 0, len(nums)-1
        while nums[j] > target:
            j -= 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return []


# 如果要求返回索引，数组未排序但是无duplicates:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {num:i for i, num in enumerate(nums)}
        nums.sort()
        if not nums or nums [0] > target: return []
        i, j = 0, len(nums)-1
        while nums[j] > target:
            j -= 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [dic[nums[i]], dic[nums[j]]]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return []
