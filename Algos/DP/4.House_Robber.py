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
