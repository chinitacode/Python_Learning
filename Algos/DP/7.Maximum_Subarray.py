'''
---------------------------------------------
53. Maximum Subarray [Easy]
---------------------------------------------
Method1: DP with O(n) time and O(n) space

dp[i]表示以a[i]为结束的子序列的最大和
前面的a[i-1]结束的某个子序列已经取得最大和,如果和是正的,那么继续累加下去才有意义,
否则应该停止累积,从下1个元素重新计算子序列.

step 0 : dp[0] = nums[0]
step i : dp[i] = dp[i-1] + nums[i] if dp[i-1] > 0 else nums[i]

e.g.
input nums: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
final dp:   [-2, 1, -2, 4,  3, 5, 6,  1, 5]
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums.copy()
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
        return max(dp)
