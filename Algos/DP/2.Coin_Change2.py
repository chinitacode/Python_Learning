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
dp[i][j] = dp[i-1][j] + dp[i][j-coin]

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
衍生：Lintcode 562. 背包问题 IV
给出 n 个物品, 以及一个数组, nums[i]代表第i个物品的大小,
保证大小均为正数并且没有重复, 正整数 target 表示背包的大小, 找到能填满背包的方案数。
每一个物品可以使用无数次。

样例
样例1
输入: nums = [2,3,6,7] 和 target = 7
输出: 2

解释:
方案有:
[7]
[2, 2, 3]

样例2
输入: nums = [2,3,4,5] 和 target = 7
输出: 2

解释:
方案有:
[2, 5]
[3, 4]

衍生：【2017美团】【背包】拼凑硬币
给你六种面额 1、5、10、20、50、100 元的纸币，假设每种币值的数量都足够多，
编写程序求组成N元（N为0~10000的非负整数）的不同组合的个数。
https://blog.csdn.net/majichen95/article/details/89365919
'''
