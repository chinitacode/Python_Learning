'''
16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).



[Method 1]: Two Pointer
Need to introduce a variable representing the closest sum (named res),
first initiated by a very giant number float('inf')
and the current sum (named Sum) of the current three numbers.
Each time we compare the difference between Sum and target,
and the difference between the previously closest sum res and target,
to decide whether to update the closest sum res.
Return res after the iteration of the first number start is finished (index from 0 to N-3)

[Time]: O(N^2)
[Space]: O(1)
Runtime: 192 ms, faster than 27.21% of Python3 online submissions for 3Sum Closest.
Memory Usage: 13.6 MB, less than 5.41% of Python3 online submissions for 3Sum Closest.
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3: return
        nums.sort()
        res = float('inf')
        for start in range(len(nums)-2):
            l, r = start+1, len(nums)-1
            while l<r:
                tmp = [nums[start], nums[l], nums[r]]
                Sum = sum(tmp)
                if Sum - target == 0: return Sum
                elif Sum - target < 0:
                    l += 1
                else:
                    r -= 1
                if abs(Sum-target) < abs(res-target):
                    res = Sum
        return res

'''
Brute-force: O(N^3)
Brute force solution will be O(N^3).
We end up testing every subset and update the closest sum in every iteration.
'''
