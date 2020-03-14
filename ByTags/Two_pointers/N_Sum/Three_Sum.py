'''
15. 三数之和 [中等]
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

[Method 1]: 排序加双（三）指针
[Time]: O(nlogn + n^2) = O(n^2)
[Space]: O(1)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) < 3: return res
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                while i+1 < l < len(nums)-1 and nums[l] == nums[l-1]:
                    l += 1
                if l >= r: break
                Sum = nums[i] + nums[l] + nums[r]
                if Sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif Sum < 0:
                    l += 1
                else:
                    r -= 1
        return res

# 优化：
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3: return result
        #O(nlgn)
        nums.sort()
        #O(n)
        for start in range(len(nums)-2):
            #Pruning
            if nums[start] > 0: break
            #avoid duplicate starting num
            if start > 0 and nums[start] == nums[start-1]: continue
            l, r = start+1, len(nums)-1
            #O(n)
            while l < r:
                Sum = nums[start] + nums[l] + nums[r]
                if Sum == 0:
                    tmp = [nums[start], nums[l], nums[r]]
                    result. append(tmp)
                    #Important! Jumping duplicate second num
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    #Jumping duplicate third num
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif Sum < 0:
                    l += 1
                else:
                    r -= 1
        return result


'''
或者再优化一下，当数组最后两个数之和都小于当前数时，就直接继续遍历下一个数：
Runtime: 912 ms, faster than 63.08% of Python3 online submissions for 3Sum.
Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for 3Sum.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        if n < 3: return res
        nums.sort()
        for i in range(n-2):
            if nums[i] > 0: break
            if (i > 0 and nums[i] == nums[i-1]) or (nums[n-1] + nums[n-2] < -nums[i]) :
                continue
            l, r = i+1, n-1
            while l < r:
                Sum = nums[l] + nums[r]
                if nums[i] + Sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + Sum < 0:
                    l += 1
                else:
                    r -= 1
        return res
