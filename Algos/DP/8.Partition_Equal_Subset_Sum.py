'''
416. Partition Equal Subset Sum [Medium]
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

[Method 1]: DP
问题可以看做一个背包大小为Sum//2的0-1背包问题。

dp[i][j]表示用前i个num可以凑齐j的组合方式个数：
dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i]]

可以优化空间复杂度为一维数列（逆序）：
dp[j] = dp[j] + dp[j-nums[i]]

使dp[0] = 1,即刚好当前num就可以凑齐j的组合个数为1；
最后返回True如果dp[Sum//2]不为0，且为2的倍数，也就是说有2的整数倍种方式凑齐Sum//2。

[Time]: O(N + N*Sum//2) = O(N*Sum//2), N为nums的元素个数，Sum为nums的元素之和。
[Space]: O(Sum//2)
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
[Method 2] Brute Force:
一样的先找出nums和的一半，使之为target;循环每个num，将可能的和存在s这个set里（初始化为{0}）,
只要有等于target的和，就返回True.

[Note]: set()之间相加用'|'操作，比如说{0} |= {1} = {0, 1}
Time: 最坏O(2^n)，因为in操作需要2^n + 2^(n-1) + ... + 2^0,并且set操作又要2^(n-1) + ... + 2^0。
Space: O(1)
Runtime: 216 ms, faster than 69.75% of Python3 online submissions for Partition Equal Subset Sum.
Memory Usage: 14.6 MB, less than 13.64% of Python3 online submissions for Partition Equal Subset Sum.
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) %2 == 0:
            target = sum(nums) // 2
            s = {0}
            for n in nums:
                s |= {n+x for x in s}
                if target in s:
                    return True
        return False


'''
[Method 3]: DFS
'''
