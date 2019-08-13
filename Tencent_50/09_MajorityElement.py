'''
169. Majority Element
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

# Method 1: Dictionary. O(n)
key in dict: O(1)
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
                if count[num] > n // 2:
                    return num
            else:
                count[num] = 1

# Method 2: # two pass + dictionary
def majorityElement1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for num in nums:
        if dic[num] > len(nums)//2:
            return num


# Method 3, O(nlgn)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]


# TLE
def majorityElement3(nums):
    for i in xrange(len(nums)):
        count = 0
        for j in xrange(len(nums)):
            if nums[j] == nums[i]:
                count += 1
        if count > len(nums)//2:
            return nums[i]

# Bit manipulation
def majorityElement5(nums):
    bit = [0]*32
    for num in nums:
        for j in xrange(32):
            bit[j] += num >> j & 1
    res = 0
    for i, val in enumerate(bit):
        if val > len(nums)//2:
            # if the 31th bit if 1,
            # it means it's a negative number
            if i == 31:
                res = -((1<<31)-res)
            else:
                res |= 1 << i
    return res

# Or shorter:
def majorityElement(nums):
    return (sum((sum(n>>i&1 for n in nums) > len(nums)/2) << i
                for i in range(32)) + 2**31) % 2**32 - 2**31


# Divide and Conquer
def majorityElement6(self, nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    a = self.majorityElement(nums[:len(nums)//2])
    b = self.majorityElement(nums[len(nums)//2:])
    if a == b:
        return a
    return [b, a][nums.count(a) > len(nums)//2]

#Boyer-Moore
# the idea here is if a pair of elements from the
# list is not the same, then delete both, the last
# remaining element is the majority number
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
