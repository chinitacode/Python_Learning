'''
16. 3Sum Closest
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Method1: Two - pointer
[Analysis]
The way to think about it is since it's 3 sum, there's only going to be 3 numbers.
So to find the combinations of 3 numbers,
he is iterating through the list with the first pointer,
and then trying to find two extra numbers to sum to 0.
Since the list is ordered, the right pointer will always be higher than the middle pointer.
So if the sum is too large, you can move the right pointer back one.
On the other hand, if the sum is too small (below 0), then move the middle pointer up one.
[Note]
1.adding below might improve the solution since sum of positive will be always >0:
if nums[i] > 0:
   break
2.len(nums)-2 is because we need at least 3 numbers to continue.
3.if i > 0 and nums[i] == nums[i-1] is because when i = 0,
it doesn't need to check if it's a duplicate element since it doesn't even have a previous element to compare with.
And nums[i] == nums[i-1] is to prevent checking duplicate again.
4.when there are more duplicates, like if nums = [-2,0,0,2,2],
then when sum is equal to zero, l and r need to be checked duplicate cases as well:
while l < r and nums[l] == nums[l+1]:
    l += 1
while l < r and nums[r] == nums[r-1]:
    r -= 1
l += 1; r -= 1

O(n^2)
Runtime: 1052 ms, faster than 43.22% of Python3 online submissions for 3Sum.
Memory Usage: 17 MB, less than 25.00% of Python3 online submissions for 3Sum.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #O(nlgn)
        nums.sort()
        res = []
        #O(n)
        for i in range(len(nums)-2):
            if nums[i] > 0:
                    break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            #O(n)
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return res


'''
Method2:
Runtime: 248 ms, faster than 99.57% of Python3 online submissions for 3Sum.
Memory Usage: 17.8 MB, less than 10.00% of Python3 online submissions for 3Sum.
'''
from collections import Counter
import bisect

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        sorted_cnt, res = dict(sorted(count.items())), set()
        sorted_klist = list(sorted_cnt)
        # print(sorted_cnt)
        if 0 in sorted_cnt:
            if sorted_cnt[0] >= 3:
                res.add((0, 0, 0))
            sorted_cnt[0] = 1
        right = len(sorted_klist)
        for idx, key in enumerate(sorted_cnt.keys()):
            if sorted_cnt[key] >= 2 and -2 * key in sorted_cnt:
                    res.add((key, key, -2 * key))
            if key < 0:
                twosum = -key
                # can be relaced by left = idx + 1
                left = bisect.bisect_left(sorted_klist, twosum - sorted_klist[-1], lo=idx + 1, hi=right)
                # this cannot be replaced due to the duplicability
                right = bisect.bisect_right(sorted_klist, twosum >> 1, lo=left)

                for sec in sorted_klist[left:right]:
                    other = twosum - sec
                    if other in count and other != sec:
                        res.add((key, other, sec))

        return res
