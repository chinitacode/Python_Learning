'''
桶排序，又叫计数排序。类似于抽屉原理。
可以用于1-n中有元素缺失的情况（重复）。

Best      Average    Worst    Memory    Stable      Method        Note
  n        n          n         k         No       Counting       k为duplicates最大个数（抽屉的最大空间）

1、适用于最大值和最小值之差range比较小的时候，和duplicate很多的情况（节省空间）；

2、找出最小值和最大值，为它们和之间的每一个整数设一个抽屉，
即最小值为第一个最大值为最后一个抽屉，抽屉个数为Max - Min + 1,
每个抽屉记录该属于抽屉元素的个数（即duplicate的个数）；

3、最后用一个for循环按抽屉把数排好；

4、时间复杂度全为O(n), 空间复杂度为O(k), 因为最后是in-place排列的，k抽屉个数，
即最大值和最小值之间的范围range, 当range非常大，比如1和100000之间差太多，则空间开销无法想象。

5、不稳定排序。
'''
def bucket_sort(arr):
    #用一个for循环同时找齐最大最小值比分开用min()和max()省一遍遍历
    Min, Max = arr[0], arr[0]
    # O(n)
    for num in range(1,len(arr)):
        if num < Min:
            Min = num
        elif num > Max:
            Max = num
    #桶的个数
    count = Max - Min + 1
    buckets = [0]*count
    #把元素放进桶里 O(n)
    for num in arr:
        buckets[num-Min] += 1

    pos = 0
    #把桶里元素按顺序取出来排好
    # O(n)，因为总共就只需要把n个元素拿出来放好
    for i in range(count):
        for j in range(buckets[i]):
            arr[pos] = Min + i
            pos += 1


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


[Method 1]: 抽屉原理（把nums作哈希表用）
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
[Method 2]:
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
