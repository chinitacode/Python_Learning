'''
16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).



Two Pointer Solution: O(N^2)

1.We can use the two pointer method to reduce complexity to O(N^2).
We begin by sorting the array.

2.Now we use three indices i,j and k.
We iterate i from 0 to N (actually till N-2 is fine).
We initialize j to i+1 and k to N-1.

3.Now we compute curr_sum = nums[i]+nums[j]+nums[k].
If this equals target, we have the closest sum.

4.Otherwise update closest_sum using the rule abs(curr_sum-target) < abs(closest_sum-target).

5.Now what if curr_sum is less than target.
Should we test (nums[i]+nums[j]+nums[k-1]), (nums[i]+nums[j]+nums[k-2]), (nums[i]+nums[j]+nums[k-3]) ?
The answer is NO. All of these triplets will be less than curr_sum.
And curr_sum is less than target - so there is no point testing these triplets.
We must move forward by advancing j to j + 1 in the hope to get a larger triplet.
This is the main intuition in this problem.

6.You can visualize (6) by thinking all possible triplet sums sorted and arranged on a number line.
When you find a curr_sum less than target, you increase curr_sum by increasing j.
When you find a curr_sum less more than target, you reduce curr_sum by reducing k
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = 2**31-1
        for i in range(len(nums)):
            j,k = i+1, len(nums)-1
            while j<k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == target:
                    return curr_sum
                if abs(curr_sum-target) < abs(closest_sum-target):
                    closest_sum = curr_sum
                if curr_sum < target:
                    j = j+1
                else:
                    k = k-1
        return closest_sum

#Or:
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i+1, len(num) - 1
            while j < k:
                sum = num[i] + num[j] + num[k]
                if sum == target:
                    return sum

                if abs(sum - target) < abs(result - target):
                    result = sum

                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1

        return result

'''
Brute-force: O(N^3)
Brute force solution will be O(N^3).
We end up testing every subset and update the closest sum in every iteration.
'''
