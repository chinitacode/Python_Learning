'''
---------------------------------------------
213. House Robber II [Medium]
---------------------------------------------
因为抢劫了第一个房子就不能抢劫最后一个房子，
所以问题变成了：f(1,n) = max(f(1, n-1), f(2,n))

[Method 1] 2 DP,
dp1为从第一个房子抢劫到到第n-1个房子，略掉最后一个房子；
dp2为从第二个房子抢劫到最后一个房子。
Time: O(n) 实际上用时2n; Space: O(n) 实际上用2n的空间。
Runtime: 40 ms, faster than 52.48% of Python3 online submissions for House Robber II.
Memory Usage: 13.9 MB, less than 5.56% of Python3 online submissions for House Robber II.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        dp1 = nums.copy()
        dp2 = nums.copy()
        dp1.pop()
        dp2[0] = 0
        for i in range(2, len(dp1)):
            dp1[i] += max(dp1[i-2], dp1[i-3] if i >= 3 else 0)
        max_without_last = max(dp1[-1],dp1[-2] if len(dp1) > 1 else 0)

        for i in range(2,len(dp2)):
            dp2[i] += max(dp2[i-2], dp2[i-3] if i >= 3 else 0)
        max_with_last = max(dp2[-1],dp2[-2])
        return max(max_without_last, max_with_last)

'''
Optimized code:
Time: O(n) 实际上用时2n; Space: O(n) 实际上用2n的空间。
Runtime: 32 ms, faster than 95.82% of Python3 online submissions for House Robber II.
Memory Usage: 13.6 MB, less than 5.56% of Python3 online submissions for House Robber II.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]

        def robRange(nums, start, end):
            dp = nums[start:end]
            for i in range(2, len(dp)):
                dp[i] += max(dp[i-2], dp[i-3] if i >= 3 else 0)
            return max(dp[-1],dp[-2] if start + 1 < end else 0)
        #f(1,n) = max(f(1, n-1), f(2,n))
        return max(robRange(nums,0,len(nums)-1), robRange(nums,1,len(nums)))


'''
Optimizing space:
Time: O(n), Space: O(1)
Runtime: 32 ms, faster than 95.82% of Python3 online submissions for House Robber II.
Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for House Robber II.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        def robRange(nums, start, end):
            yes, no = nums[start], 0
            for i in range(start+1,end):
                yes, no = no + nums[i], max(yes, no)
            return max(yes, no)
        return max(robRange(nums,0,len(nums)-1), robRange(nums,1,len(nums)))


'''
#Shorter code:
Runtime: 36 ms, faster than 82.97% of Python3 online submissions for House Robber II.
Memory Usage: 13.8 MB, less than 5.56% of Python3 online submissions for House Robber II.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(nums):
            yes, no = 0, 0
            for i in nums:
                yes, no = no + i, max(yes, no)
            return max(yes, no)
        # False equals 0 and True equals 1
        return max(robRange(nums[len(nums) != 1:]), robRange(nums[:-1]))
