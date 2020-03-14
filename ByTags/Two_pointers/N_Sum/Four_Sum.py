'''
18. 四数之和 [中等]

给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


[Method 1]: 排序+四指针
[Time]: O(n^3)
[Space]: O(1)
注意：不能用if nums[i] > target: break来先一步筛选，因为遇到有负数的情况，负数相加是会变得更小的
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]: continue
                l, r = j+1, len(nums)-1
                while l<r:
                    Sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if Sum > target:
                        r -= 1
                    elif Sum < target:
                        l += 1
                    elif l > j+1 and nums[l] == nums[l-1]:
                        l += 1
                    elif r < len(nums)-1 and nums[r] == nums[r+1]:
                        r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
        return res

'''
[Method 2]: 字典+双指针
先排序，再用两个for循环遍历一遍数组，存储所有可能的two_sum为key,
其可能的索引组合（如果存值的话遇上有重复的情况就不好判断了）为value(以tuple的形式避免重复)；
然后再用两个for循环遍历一遍数组筛选出满足和为target的所有可能组合，一个个地加在set()里避免值重复，
最后把答案list起来
【注意】：在筛选答案的时候为了避免将之前已经加入res的索引组合再加一遍，
可以先判断该组合第一个索引是否在当前j的后面出现。
[Time]: O(nlogn + n^2) = O(n^2)
[Space]:O(2*C(n,2)) = O(n^2) , 即字典的空间开销
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        n, res, two_sums = len(nums), set(), {}
        nums.sort()
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] not in two_sums:
                    two_sums[nums[i] + nums[j]] = [(i,j)]
                else:
                    two_sums[nums[i] + nums[j]].append((i,j))
        for i in range(n-3):
            for j in range(i+1, n-2):
                left = target - nums[i] - nums[j]
                if left in two_sums:
                    for idxes in two_sums[left]:
                        if idxes[0] > j:
                            res.add((nums[i], nums[j], nums[idxes[0]], nums[idxes[1]])) # res是一个set，去重
        return [list(i) for i in res]
