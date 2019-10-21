'''
238. Product of Array Except Self[Medium]
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).
Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)


[Method 1]: sequential and reversed traversal
Intuition: current_product = product_left * product_right
E.g.
Input:  [1,2,3,4]
Output: [24,12,8,6]
product[2] = product_left * product_right = 1 * (3*4) = 12
So we initialize the result array by all 1,
and in the sequential traversal of nums,
we multiply it by its left product,
and update the left product of the next num by multiplying the current num itself;
and in the reversed traversal,
we multiply it by its right product,
and update the right product of the next num by multiplying the current num itself.
[Time]: O(n)
[Space]: O(1)  (here the output array does not count as extra space)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res, l, r = [1]*len(nums), 1, 1
        for i, j in zip(range(len(nums)), range(len(nums)-1, -1, -1)):
            res[i], l = res[i]*l, l*nums[i]
            res[j], r = res[j]*r, r*nums[j]
        return res
