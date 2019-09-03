'''
33. Search in Rotated Sorted Array
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Two-Pointer:

'''
def search(nums, target):
    if len(nums) < 1:
        return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < nums[mid]:
            if nums[left] <= target and target <= nums[mid]:
                right = mid
            else:
                left = mid
        else:
            if nums[mid] <= target and target <= nums[right]:
                left = mid
            else:
                right = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1

#or:
'''
Runtime: 52 ms, faster than 45.84% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.1 MB, less than 6.29% of Python3 online submissions for Search in Rotated Sorted Array.
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:  # base case
            return -1

        l, r = 0, len(nums) - 1

        # input array has no rotation
        # the '=' include the length == 1 array
        if nums[-1] >= nums[0]:
            nums2 = nums
            pIndex = -2
        # input array has been rotated
        else:  # log(n) search the max value
            while l < r:
                m = (l + r) // 2
                if nums[m] > nums[m+1]:
                    break
                elif nums[m] > nums[l]:
                    l = m
                elif nums[m] < nums[l]:
                    r = m
            nums2 = nums[m+1:] + nums[:m+1] # re-order the array
            pIndex = m

        l = 0
        r = len(nums) - 1
        newIndex = -1  # flag to check if item exists
        while l <= r:  # search
            m = (l + r) // 2
            if nums2[m] == target:
                newIndex = m
                break
            elif nums2[m] > target:
                r = m - 1
            elif nums2[m] < target:
                l = m + 1

        if newIndex == (-1): # doen't exist
            return -1

        if pIndex == (-2): # the original array is sorted
            return m

        return (m + pIndex + 1) % len(nums) # add index
