'''
448. Find All Numbers Disappeared in an Array [Easy]
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array),
some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime?
You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]

[Method 1]: 先set()再 一一比对
修改了input array
[Time]: O(nlgn)
[Space]: O(1)
Runtime: 428 ms, faster than 47.66% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 23.6 MB, less than 7.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = sorted(list(set(nums)))
        count, offset, res = n - len(nums), 0, []
        i = 1
        for num in nums:
            if count == 0: break
            if i + offset != num:
                for _ in range(num-i-offset):
                    res.append(i+offset)
                    count -= 1
                    offset += 1
            i += 1
        i += offset
        while count != 0:
            res.append(i)
            count -= 1
            i += 1
        return res

#Or:
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        marked = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in marked]

'''
[Method 2]: 抽屉原理（把nums作哈希表用）
把每个数看作是它们在假设是从从 1 到 N 排好序的数列Nums里的位置（index），
并把其（位置）对应的数字标记为负数。
所以最终为正的位置就是未被标记的，即该位置为空，缺少相应的数字 index+1,
最后把它加入输出数组即可。
[Time]: O(n)
[Space]: O(1)
Runtime: 432 ms, faster than 42.92% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 21.5 MB, less than 17.86% of Python3 online submissions for Find All Numbers Disappeared in an Array.
'''
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            index = abs(num) - 1
            nums[index] = - abs(nums[index])
        return [index + 1 for index in range(n) if nums[index] > 0]

'''
[Method 3]:
Iterate the array and add N to the existing number at the position implied by every element.
This means that positions implied by the numbers present in the array
will be strictly more than N (smallest number is 1 and 1+N > N).
Therefore. in the second iteration,
we simply need to report the numbers less than equal to N to return the missing numbers..
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        for i in range(len(nums)):
            nums[(nums[i]%N)-1] += N
        return [i+1 for i in range(len(nums)) if nums[i]<=N]



'''
若将题目要求改为数组中每个元素出现的可能次数是 n 次,
求出数组中出现此次为偶数（奇数）次的元素（出现 0 次也算偶数次）。
'''
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 将所有正数作为数组下标，置对应数组值为相反数。那么，仍为正数的位置即为出现偶数次(未出现是0次，也是偶数次)数字。
        # 举个例子：
        # 原始数组：[1, 1, 1, 1, 2, 3, 4, 5]
        # 重置后为：[1, -1, -1, -1, -2, 3, 4, 5]
        # 结论：[1,3,4,5] 分别对应的index为[1,6,7,8]（消失的数字）
        for num in nums:
            index = abs(num) - 1
            # 保持nums[index]为相反数,唯一和上面的解法不同点就是这里，好好体会
            nums[index] = -nums[index]
        #偶数次
        return [i + 1 for i, num in enumerate(nums) if num > 0]
        #奇数次
        return [i + 1 for i, num in enumerate(nums) if num < 0]
