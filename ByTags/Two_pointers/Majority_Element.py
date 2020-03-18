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

[Method 1]: Boyer-Moore Voting Algorithm
不同就cancel，相同就保留，最后剩下的必然是众数。
但是因为我们用的列表，删除操作不方便，所以可以用两个变量，一个candidate初始为nums[0],
一个count初始化为1记录当前遇到的candidate的个数，如果当前遍历到的数字num和candidate相同，
count += 1,否则减1，但当count为0时，也就是说candidate被之前遍历的数字消掉了（像消消乐一样配对消掉了），
那么我们就把num作为新的candidate，把count设置为1，继续遍历下一个元素，直到遍历完后返回最后的candidate即可。
[Time]: O(n)
[Space]: O(1)
Runtime: 176 ms, faster than 74.11% of Python3 online submissions for Majority Element.
Memory Usage: 14.4 MB, less than 26.19% of Python3 online submissions for Majority Element.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return
        count = 1
        candidate = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                count += 1
            elif count == 0:
                candidate = nums[i]
                count += 1
            else:
                count -= 1
        return candidate

# or：
def majorityElement(nums):
    count, cand = 0, 0
    for num in nums:
        if num == cand:
            count += 1
        elif count == 0:
            cand, count = num, 1
        else:
            count -= 1
    return cand
