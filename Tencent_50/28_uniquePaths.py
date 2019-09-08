'''
62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
Note: m and n will be at most 100.

Example 1:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3
Output: 28

Method1:排列组合
因为机器到达右下角，向下几步，向右几步都是固定的，
比如，m=3, n=2，我们只要向下 1 步，向右 2 步就一定能到达终点。
因为一共有m-1个right和n-1个down，所以一共有m+n-2个step要走，其中的m-1个right（或者n-1个down），在这些step中，所以是m+n-2里选m-1个
Runtime: 32 ms, faster than 93.48% of Python3 online submissions for Unique Paths.
Memory Usage: 13.7 MB, less than 5.77% of Python3 online submissions for Unique Paths.
'''
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m+n-2) // math.factorial(m-1) // math.factorial(n-1)
        
'''
Method2: DP
令 dp[i][j] 是到达 i, j 最多路径，因为只能向右下方走，所以到达i，j的上方或者左边就只能往下或者往右走，
即到达上方或者左边的最多路径和就是到达 i, j 最多路径，
我们可以得到动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
注意，对于第一行 dp[0][j]，或者第一列 dp[i][0]，由于都是在边界，所以只能为 1
时间复杂度：O(m*n)
空间复杂度：O(m * n)
Runtime: 32 ms, faster than 93.48% of Python3 online submissions for Unique Paths.
Memory Usage: 13.8 MB, less than 5.77% of Python3 online submissions for Unique Paths.

'''


'''
优化：因为我们每次只需要 dp[i-1][j],dp[i][j-1],所以我们只要记录这两个数
优化1：空间复杂度 O(2n)
Runtime: 36 ms, faster than 75.95% of Python3 online submissions for Unique Paths.
Memory Usage: 13.7 MB, less than 5.77% of Python3 online submissions for Unique Paths.
'''
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]
        return pre[-1]

'''
优化2：空间复杂度 O(n)

'''
import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
