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
final dp:   [-2, 1, -2, 4,  3, 5, 6,  1, 5]
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
#Or：
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

'''
[Method 3]: Divide and Conquer
1) Divide the given array in two halves
2) Return the maximum of following three
….a) Maximum subarray sum in left half (Make a recursive call)
….b) Maximum subarray sum in right half (Make a recursive call)
….c) Maximum subarray sum such that the subarray crosses the midpoint

The lines 2.a and 2.b are simple recursive calls.
How to find maximum subarray sum such that the subarray crosses the midpoint?
We can easily find the crossing sum in linear time.
The idea is simple, find the maximum sum starting from mid point and ending at some point on left of mid,
then find the maximum sum starting from mid + 1 and ending with sum point on right of mid + 1.
Finally, combine the two and return.

Time: O(nlgn)
maxSubArraySum() is a recursive method and time complexity can be expressed as following recurrence relation.
T(n) = 2T(n/2) + Θ(n)
The above recurrence is similar to Merge Sort and can be solved either using Recurrence Tree method or Master method.
It falls in case II of Master Method and solution of the recurrence is Θ(nLogn).

Runtime: 176 ms, faster than 5.22% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.4 MB, less than 5.69% of Python3 online submissions for Maximum Subarray.
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return
        r = len(nums) - 1
        return self.maxSubArraySum(nums, 0, r)

    def maxCrossingSum(self, nums, l, mid, r):
        left_sum = float('-infinity')
        cur_sum = 0
        for i in range(mid, l-1, -1):
            cur_sum += nums[i]
            left_sum = max(left_sum,cur_sum)

        right_sum = float('-infinity')
        cur_sum = 0
        for j in range(mid+1, r+1):
            cur_sum += nums[j]
            right_sum = max(right_sum,cur_sum)

        return left_sum + right_sum

    def maxSubArraySum(self, nums, l, r):
        if l == r:
            return nums[l]
        mid = l + (r - l)//2
        return max(self.maxSubArraySum(nums, l, mid),self.maxSubArraySum(nums, mid+1, r),self.maxCrossingSum(nums,l,mid,r))
