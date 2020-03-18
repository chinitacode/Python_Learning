'''
169. Majority Element [Easy]
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

[Method 1]: Divide And Conquer
长度为 1 的子数组中唯一的数显然是众数，直接返回即可。
如果回溯后某区间的长度大于 1 ，我们必须将左右子区间的值合并。
如果它们的众数相同，那么显然这一段区间的众数是它们相同的值。
否则，我们需要比较两个众数在整个区间内出现的次数来决定该区间的众数。

[Time]: O(nlogn) 不推荐
[Space]: O(1)
Runtime: 304 ms, faster than 5.52% of Python3 online submissions for Majority Element.
Memory Usage: 14.7 MB, less than 7.14% of Python3 online submissions for Majority Element.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def dnc(lo,hi):
            if lo+1 == hi:
                return nums[lo]
            mid = lo+(hi-lo)//2
            left = dnc(lo,mid)
            right = dnc(mid,hi)
            if left == right:
                return left
            # 否则只能通过它在整个数组中出现的次数来决定选谁 (O(n))
            left_count = sum(1 for i in range(lo,hi) if nums[i] == left)
            right_count = sum(1 for i in range(lo,hi) if nums[i] == right)
            return left if left_count > right_count else right
        return dnc(0,len(nums))
