'''
53. Maximum Subarray [Easy]
Given an integer array nums, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.


Method1: DP with O(n) time and O(n) space
Runtime: 72 ms, faster than 92.61% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.6 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.

dp[i]表示以a[i]为结束的子序列的最大和
前面的a[i-1]结束的某个子序列已经取得最大和,如果和是正的,那么继续累加下去才有意义,
否则应该停止累积,从下1个元素重新计算子序列.

step 0 : dp[0] = nums[0]
step i : dp[i] = dp[i-1] + nums[i] if dp[i-1] > 0 else nums[i]

e.g.
input nums: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
final dp:   [-2, 1, -2, 4, 3, 5, 6, 1, 5]
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums.copy()
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)

'''
Method2: 记录每个元素是否包含前一元素的当前最大值curSum,和整个数组里面的最大值maxSum,
最终返回maxSum
O(n) time and O(1) Space
Runtime: 76 ms, faster than 76.85% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14 MB, less than 12.20% of Python3 online submissions for Maximum Subarray.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        curSum = maxSum = nums[0]
        for num in nums[1:]:
            curSum = max(num, num + curSum)
            maxSum = max(maxSum, curSum)
        return maxSum


'''
Runtime: 72 ms, faster than 92.57% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.4 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
'''
class Solution:
    def maxSubArray(self, n):
        m = t = float('-Infinity')
        for i in n:
            if t + i < i:
                t = i
            else:
                t = t + i
            if m < t:
                m = t
        return m
