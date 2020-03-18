'''
229. Majority Element II [Medium]

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

[Note]: 注意，因为是找出现次数超过1/3的数，整个数组中最多只能有两个。

[Method 1]: Boyer Moore Voting Algorithm
因为最多有两个数，所以我们设置两个candidate,即candidate1和candidate2，和count1,count2,
如果等于当前任意一个candidate，就把该count加1，如果当前有一个count等于0，
那就更新candidate为当前数并且count设置为1。但是如果当前num不等于任一candidate，
就把两个count都减1，返回最后出现次数大于1/3size的candidate的列表。

[Time]: O(n*4 + 2n) = O(n)
[Space]: O(1)
Runtime: 124 ms, faster than 60.74% of Python3 online submissions for Majority Element II.
Memory Usage: 14.1 MB, less than 17.65% of Python3 online submissions for Majority Element II.
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1,count1,cand2,count2 = None,0,None,0
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1,count1 = num, 1
            elif count2 == 0:
                cand2,count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        size = len(nums)
        return [cand for cand in (cand1,cand2) if cand is not None and nums.count(cand) > (size//3)]
