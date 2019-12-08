'''
704. Binary Search [Easy]

Given a sorted (in ascending order) integer array nums of n elements and a target value,
write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].

[Method 1]:
关键是左右bound都要推进，否则会陷入死循环.
这里的二分搜索要注意一下，考虑当lo==hi时也就是说数组只有一个元素时，
也是要比对看是否等于target的，所以while循环的条件式while lo <= hi,
而且每次lo和hi的更新都要mid+1和mid-1,
不然因为while循环break条件里的等号，会容易陷入死循环跳不出来。
Runtime: 268 ms, faster than 83.84% of Python3 online submissions for Binary Search.
Memory Usage: 14 MB, less than 100.00% of Python3 online submissions for Binary Search.
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi = 0, len(nums)-1
        #lo == hi表明只有一个元素，只需要验证这个元素是否等于target
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

'''
[Method 2]用自带的bisect模块
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        subtract 1 as the bisect call "returns an insertion point which comes
        after (to the right of) any existing entries of x in a."
        '''
        if not matrix or not matrix[0]: return False
        i = bisect.bisect([row[0] for row in matrix], target) - 1
        j = bisect.bisect(matrix[i], target) - 1
        return matrix[i][j] == target
