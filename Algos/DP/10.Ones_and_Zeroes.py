'''
474. Ones and Zeroes [Medium]
For now, suppose you are a dominator of m 0s and n 1s respectively.
On the other hand, there is an array with strings consisting of only 0s and 1s.
Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s.
Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.

Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s,
which are “10,”0001”,”1”,”0”

Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

[题目大意]：
我们现在从数组中每个字符串都有一些0和1，问给了m个0，n个1，从数组中取出最多的字符串，这些字符串中1和0的出现次数之和不超过m，n.

[Analysis]:
遇到这种求最多或最少的次数的，并且不用求具体的解决方案，一般都是使用DP。

This problem is a typical 0-1 knapsack problem,
we need to pick several strings in provided strings to get the maximum number of strings using limited number 0 and 1.
We can create a three dimensional array, in which dp[i][j][k] means the maximum number of strings
we can get from the first i argument strs using limited j number of '0's and k number of '1's.

For dp[i][j][k], we can get it by fetching the current string i or discarding the current string,
which would result in dp[i][j][k] = dp[i-1][j-numOfZero(strs[i])][i-numOfOnes(strs[i])] and dp[i][j][k] = dp[i-1][j][k];
We only need to treat the larger one in it as the largest number for dp[i][j][k].
we cannot decrease the time complexity, but we can decrease the space complexity from ijk to j*k。

这个DP很明白了，定义一个数组dp[m+1][n+1]，代表m个0, n个1能组成的字符串得最大数目。
遍历每个字符串统计出现的0和1得到zeros和ones，所以有状态转移方程：
dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
即，用i个0和j个1，在数组strs里面，求能组成的字符串的最大数目时有两种情况：
1.不算当前的字符串str，则有dp[i][j]个；
2.要算当前的字符串str,则str之前的字符串只能用i-zeros个0和j-ones个1，所得的字符串个数和为dp[i - zeros][j - ones] + 1。
因此我们比较大小，取最大的值。
其中dp[i - zeros][j - ones]表示如果取了当前的这个字符串，那么之前的字符串用用剩下的0和1时取的最多的数字。
边界条件：dp[0][0],表示用0个0和0个1能凑出的字符串个数为0。
[Time]: O(s*m*n)
[Space]: O(m*n)
Runtime: 2864 ms, faster than 68.16% of Python3 online submissions for Ones and Zeroes.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Ones and Zeroes.
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros, ones = s.count('0'), s.count('1')
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i - zeros][j - ones] + 1, dp[i][j])
        return dp[m][n]
