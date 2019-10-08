'''
[Practice]
1.1维DP问题：
    53. Maximum Subarray [Easy]
    70.Climbing Stairs [Easy]
        爬楼梯变形：给定n,找到不同将n写成1,3,4相加的问题（顺序matters）
                或：仍然是爬楼梯，一次可以爬1步，3步或者4步
    198. House Robber
    213. House Robber II
    337. House Robber III
'''



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



'''
---------------------------------------------
70.Climbing Stairs [Easy]
---------------------------------------------
DP (Bottom Up)
Time: O(n), Space: O(n)
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return n
        dp = [0]*n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]

'''
爬楼梯变形：给定n,找到不同将n写成1,3,4相加的问题（顺序matters）
  或理解为：仍然是爬楼梯，一次可以爬1步，3步或者4步
[分析]
关键还是找到公式dp[i] = dp[i-1] + dp[i-3] + dp[i-4]，
其实可以想成第一步是1有多少种选择，加上第一步是3的选择数，再加第一步是4的可能组合。
'''
def climb_stairs(n):
    dp = [1, 1, 2, 4]
    if n > 4:
        dp += [0]*(n-4)
    for i in range(4, n):
        dp[i] = dp[i-1] + dp[i-3] + dp[i-4]
    return dp[n-1]


'''
---------------------------------------------
198. House Robber [Easy]
---------------------------------------------
[Analysis] DP
注意并不一定是严格地每每隔着1个房子抢劫，每次抢劫时要考虑目前能得到的最大利益，如：
Input:          [2,1,1,2]
Output:     4 = 2 + 2
Explication: dp = [2,1,3,4]


Input:              [8,3,5,7,6,9,2,8,3,5]
Output: 37 = 8 + 7 + 9 + 8 + 5
Explication: dp =   [8,3,13,15,19,24,21,32,27,37]

Time: O(n), Space:O(n)
Runtime: 40 ms, faster than 49.03% of Python3 online submissions for House Robber.
Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions for House Robber.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1:
            return nums[0]
        dp = nums
        for i in range(2, len(nums)):
            dp[i] += max(dp[i-2], dp[i-3] if i >= 3 else 0)
        return max(dp[-1], dp[-2])


'''
[Optimization]
no和yes分别表示当前不抢和抢。
Time: O(n); Space: O(1)
Runtime: 32 ms, faster than 95.56% of Python3 online submissions for House Robber.
Memory Usage: 13.9 MB, less than 9.09% of Python3 online submissions for House Robber.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        no, yes = 0, 0
        for i in nums:
            #如果当前不抢，则最大利益为之前不抢和抢的最大值；
            #如果当前抢，则最大利益为当前房子的利益加上之前不抢的利益
            no, yes = max(no, yes), no + i
        #最后看最后的房子能抢还是不能抢
        return max(no, yes)

'''
Recursive Solution: (Top down)
强盗有两个选择： a).抢劫当前房子； b).不抢劫当前房子。
如果选a,则强盗不能抢劫前一个房子，但是可以安全地抢劫前两个房子，
并且获得最大收益为当前房子的价值和抢劫往前数两个房子时的最大收益；
如果选b，则强盗可以获得抢劫前一个房子时的最大收益和接着抢劫挨着的房子。
总结下来，获得的最大收益为以下的最大值：
    1).现在房子的价值+抢劫往前数两个房子的收益
    2).抢劫前一个房子的收益
rob(i) = max( rob(n - 2) + currentHouseValue, rob(n - 1) )
'''
#Time Limit Exceeded
class Solution:
    def rob(self, nums: List[int]) -> int:
        def recur(nums, n):
            if n < 1: return 0
            return max(recur(nums, n-2) + nums[n-1], recur(nums, n-1))
        return recur(nums, len(nums))

'''
Optimized code: Recursion + Memorization (Top down)
Time: O(n); Space: O(n)
Runtime: 36 ms, faster than 80.99% of Python3 online submissions for House Robber.
Memory Usage: 14 MB, less than 9.09% of Python3 online submissions for House Robber.
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.dict = {}
        def recur(nums, n):
            if n < 1: return 0
            if n not in self.dict:
                self.dict[n] = max(recur(nums, n-1), recur(nums, n-2) + nums[n-1])
            return self.dict[n]
        return recur(nums, len(nums))

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

'''
---------------------------------------------
337. House Robber III
---------------------------------------------
'''
