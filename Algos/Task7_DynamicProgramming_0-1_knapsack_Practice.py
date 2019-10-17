
'''
416. Partition Equal Subset Sum [Medium]

问题可以看做一个背包大小为Sum//2的0-1背包问题。

dp[i][j]表示用前i个num可以凑齐j的组合方式个数：
dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i]]

可以优化空间复杂度为一维数列（逆序）：
dp[j] = dp[j] + dp[j-nums[i]]

使dp[0] = 1,即刚好当前num就可以凑齐j的组合个数为1；
最后返回True如果dp[Sum//2]不为0，且为2的倍数，也就是说有2的整数倍种方式凑齐Sum//2。

Time: O(N + N*Sum//2) = O(N*Sum//2), N为nums的元素个数，Sum为nums的元素之和。
Space: O(Sum//2)
Runtime: 1040 ms, faster than 35.83% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 14.1 MB, less than 13.64% of Python3 online submissions for Partition Equal Subset Sum.
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        Sum = sum(nums)
        if Sum % 2: return False
        cap = Sum // 2
        dp = [0] * (cap + 1)
        dp[0] = 1
        for num in nums:
            for j in range(cap, num -1, -1):
                dp[j] = dp[j] + dp[j-num]
        return True if (dp[cap] != 0 and dp[cap]%2 == 0) else False


'''
494. Target Sum [Medium]

'''
