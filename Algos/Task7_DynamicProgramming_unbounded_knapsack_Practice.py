'''
518. Coin Change 2 [Medium]

You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.


Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Note:
You can assume that
0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer


[Method 1]: DP:完全背包问题
用dp[i][j]表示用前i个硬币可以凑成j块钱的组合个数。
对于第i个硬币，仍然不用或者用两种情况，以及用的话用几枚硬币。

可得状态转移方程：
dp[i][j] = dp[i-1][j] + dp[i][j-coin] + dp[i][j-2*coin] + dp[i][j-3*coin] + ... + dp[i][j-k*coin], (0 < k < j//coin)

即用前i-1个硬币凑成j块钱的组合，加上用前i-1个硬币凑成j-coin块钱，然后用第i个硬币凑成剩下的coin块钱的组合个数。

[注意！！！]
对于dp[i-1][j-coin]，要考虑硬币面额刚好为当前要凑的面值的情况，即单独那枚硬币就是1种组合，
所以dp[0][0] = 1, 语义是，不考虑任何硬币，凑出总金额为0的组合数为1。

例如硬币coins = [1, 2, 5], amount = 5 时，不考虑面额为5的最后一枚硬币，只考虑前两枚硬币，已经有：
1+1+1+1+1 = 5
1+1+1+2 = 5
1+2+2 = 5
这3种组合，
那么再考虑最后一枚硬币，即 0 + 5 = 5 这1种组合,
也就是dp[1][5] + dp[2][0] = 3 + dp[2][0], 因此dp[2][0] 必须为1， 也就是dp[i][0]都得为1。

因为每个硬币就可以取无数枚，可以看成完全背包问题，因此dp[i][j]不需要从dp[i-1][j]得到，
而是才更新的dp[i][j]，因为可能已经放了几个i物品了，所以我们用的是顺序循环，从当前coin的面额开始循环到总面值，
毕竟如果面值j < coin的话，减出来为负是没有意义的。
所以优化后的一维状态转移方程为：

dp[j] = dp[j] + dp[j-coin]

Time: O(NV), N为硬币个数，V为需要凑的面值。
Space: O(V)
Runtime: 140 ms, faster than 79.18% of Python3 online submissions for Coin Change 2.
Memory Usage: 13.7 MB, less than 16.67% of Python3 online submissions for Coin Change 2.

'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i-coin]
        return dp[amount]


'''
377. Combination Sum IV [Medium]
Given an integer array with all positive numbers and no duplicates,
find the number of possible combinations that add up to a positive integer target.

Example:
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.
Therefore the output is 7.

[Method 1]: DP
[注意！！！]此题不是完全背包，背包问题的状态表示是 f(i,j) 表示前 i 个物体，组成的重量为 j，经过优化变成了一维。
如果此题用完全背包解答，则会将顺序不同的序列如(1, 1, 2)，(1, 2, 1)和(2, 1, 1)算作相同的组合。

我们就以 nums = [1, 2, 3]，target = 4为例。
先分析4有以下几种分解：
4 = 1 + 3， 其中3应该看成用[1, 2, 3]来组成的和为3的组合数：(1,1,1,1),...先略过；
4 = 2 + 2，其中2应该看成用[1, 2, 3]来组成的和为2的组合数：(2,1,1), (2,2), 共2种；
4 = 3 + 1，其中1应该看成用[1, 2, 3]来组成的和为1的组合数：(3, 1), 共1种。
所以4一共有(3的分解种数) + 2 + 1 种分解方式。

再分析3的分解方式：
3 = 1 + 2, 其中2应该看成用[1, 2, 3]来组成的和为2的组合数：(1,1,1), (1,2),共2种；
3 = 2 + 1, 其中1应该看成用[1, 2, 3]来组成的和为1的组合数: (2,1), 共1种；
3 = 3 + 0, 其中0应该看成用[1, 2, 3]来组成的和为0的组合数: (3, ()), 共1种。
所以3一共有 2 + 1 + 1 = 4种。
再回到4的分解可知4一共有 4 + 2 + 1 = 7 种分解方式。

2有：
2 = 1 + 1, 即(1,1), 共1种；
2 = 2 + 0， 即(2,()), 共1种。
因此2一共有2种分解方式。

1：
1 = 1 + 0，即(1,()), 共1种。
所以1一共有1种分解方式。
即4的分解种数 = (4 - 1)的分解种数 + (4 - 2)的分解种数 + (4 - 3)的分解种数，其中1，2，3为各个num。

由此可得：
1.状态：
dp[i] ：对于给定的由正整数组成且不存在重复数字的数组，和为 i 的组合的个数。
2.状态转移方程：
dp[i] = sum{dp[i - num] for num in nums and if i >= num}
并且dp[0] = 1

[注意！！！]内循环必须是循环每个num，因为dp[i]是求的每个num分解方式的和！
Time: O(N*target), N为nums的size；
Space: O(target)
Runtime: 44 ms, faster than 93.67% of Python3 online submissions for Combination Sum IV.
Memory Usage: 14 MB, less than 22.22% of Python3 online submissions for Combination Sum IV.
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]
