'''
15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

[Method 1]: backtracking (TLE)
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result, tmp = [], []
        if len(nums) < 3: return result
        nums.sort()
        def backtrack(result, tmp, nums, pos):
            if len(tmp) == 3 :
                if sum(tmp) == 0 and tmp not in result:
                    result.append(tmp[:])
                return
            else:
                for j in range(pos, len(nums)):
                    tmp.append(nums[j])
                    backtrack(result, tmp, nums, j+1)
                    tmp.pop()
        backtrack(result, tmp, nums, 0)
        return result



'''
[Method 2]: Two - pointer
[Analysis]
The way to think about it is since it's 3 sum, there are only going to be 3 numbers.
The main idea is to iterate every number in nums.
We use the number as a target to find two other numbers which make total zero.
For those two other numbers, we move pointers, l and r, to try them.
That way, we need to sort the numbers.
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

[Time]: O(n^2)
[Space]: O(1)
Runtime: 736 ms, faster than 85.82% of Python3 online submissions for 3Sum.
Memory Usage: 17 MB, less than 25.71% of Python3 online submissions for 3Sum.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3: return result
        #O(nlgn)
        nums.sort()
        #O(n)
        for start in range(len(nums)-2):
            #Pruning
            if nums[start] > 0: break
            #avoid duplicate starting num
            if start > 0 and nums[start] == nums[start-1]: continue
            l, r = start+1, len(nums)-1
            #O(n)
            while l < r:
                Sum = nums[start] + nums[l] + nums[r]
                if Sum == 0:
                    tmp = [nums[start], nums[l], nums[r]]
                    result. append(tmp)
                    #Important! Jumping duplicate second num
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    #Jumping duplicate third num
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif Sum < 0:
                    l += 1
                else:
                    r -= 1
        return result

'''
或者再优化一下，当数组最后两个数之和都小于当前数时，就直接继续遍历下一个数：
Runtime: 912 ms, faster than 63.08% of Python3 online submissions for 3Sum.
Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for 3Sum.
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        if n < 3: return res
        nums.sort()
        for i in range(n-2):
            if nums[i] > 0: break
            if (i > 0 and nums[i] == nums[i-1]) or (nums[n-1] + nums[n-2] < -nums[i]) :
                continue
            l, r = i+1, n-1
            while l < r:
                Sum = nums[l] + nums[r]
                if nums[i] + Sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + Sum < 0:
                    l += 1
                else:
                    r -= 1
        return res

'''
[Method 3]: Preprocessing nums using Counter + bisect
[bisect module methods]:
1. bisect(list, num, beg, end) :
- This function returns the position in the sorted list,
where the number passed in argument can be placed so as to maintain the resultant list in sorted order.
If the element is already present in the list,
the right most position where element has to be inserted is returned.
This function takes 4 arguments, list which has to be worked with,
number to insert, starting position in list to consider,
ending position which has to be considered.

2. bisect_left(list, num, beg, end) :
- This function returns the position in the sorted list,
where the number passed in argument can be placed so as to maintain the resultant list in sorted order.
If the element is already present in the list, the left most position where element has to be inserted is returned.
This function takes 4 arguments, list which has to be worked with,
number to insert, starting position in list to consider,
ending position which has to be considered.

3. bisect_right(list, num, beg, end) :
- This function works similar to the “bisect()” and mentioned above.


[Time]: O(n*n)
[Space]: O(n)
Runtime: 248 ms, faster than 99.57% of Python3 online submissions for 3Sum.
Memory Usage: 17.8 MB, less than 10.00% of Python3 online submissions for 3Sum.
'''
from collections import Counter
import bisect

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #a Counter object of a dictionary in which keys are the nums and values are its occurrence
        count = Counter(nums)
        #sort the counter object by its keys and save it as dictionary named sorted_cnt
        sorted_cnt, res = dict(sorted(count.items())), set()
        #a list of the nums without duplicates
        sorted_klist = list(sorted_cnt)
        #Three zeros can be used in one sum, discard the extra zeros leaving only 1,
        #because we can't form a sum with only two zeros
        # if len(nums) < 3 or sorted_klist[0] > 0 or sorted_klist[-1] < 0: return res
        if 0 in sorted_cnt:
            if sorted_cnt[0] >= 3:
                res.add((0, 0, 0))
            sorted_cnt[0] = 1
        right = len(sorted_klist)
        for idx, key in enumerate(sorted_cnt.keys()):
            if sorted_cnt[key] >= 2 and -2 * key in sorted_cnt:
                    res.add((key, key, -2 * key))
            #Problem of Two_Sum
            if key < 0:
                twosum = -key
                # finding the floor and ceiling of the left two numbers to slice nums
                # can be relaced by left = idx + 1
                left = bisect.bisect_left(sorted_klist, twosum - sorted_klist[-1], lo=idx + 1, hi=right)
                # Pruning:
                # the 'first'(sec) number only need to iterate from the start to 1 plus the index of of the mid number,
                # else the sum will be greater than 2*mid, which is twosum
                right = bisect.bisect_right(sorted_klist, twosum >> 1, lo=left)
                for sec in sorted_klist[left:right]:
                    other = twosum - sec
                    # avoid repetition because 2 duplicate nums will be checked first within the outer for loop
                    if other != sec and other in count:
                        res.add((key, other, sec))
        return res
