'''
25. 剪绳子

给你一根长度为 n 绳子，请把绳子剪成 m 段（m、n 都是整数，2≤n≤58 并且 m≥2）。

每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]k[1] … k[m] 可能的最大乘积是多少？

例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到最大的乘积18。

样例
输入：8
输出：18

[Method 1]:
设置一个数组dp[n+1]，dp[ i ]存储绳子长度为i 时的最大乘积。
依题意，绳子至少被剪一次，所以绳子长度最小为2。
外层for循环从绳长为i=2的情况开始依次计算，直到计算到绳长为n的情况。

内层for循环：当绳长为i时，由于已知至少剪一刀，
我们索性假设第一刀剪在长度为j的位置(即第一段绳子长度为j)。
剩下的那段长度为( i - j )的绳子就变成了“可剪可不剪”。
那究竟是“不剪了”得到的乘积大呢，还是“继续剪余下的这段”得到乘积更大？
我们不知道，所以需要两种情况都计算一下进行比较。
其中，“不剪了”得到的乘积是j * ( i - j )，“继续剪”得到的乘积是j * dp[ i - j ]。
取其中的较大值，就是“第一剪在j位置”能得到的最大乘积。
而第一剪的所有可能位置是1,2,…,i-1。依次计算所有可能情况，取最大值即为dp[ i ]的值。

由上述过程可知，只有先依次计算出dp[2],dp[3],....的值，才能得到dp[n]的值。此为动态规划。

[Time]: O(n^2)
[Space]: O(n)
'''
class Solution(object):
    def maxProductAfterCutting(self,length):
        """
        :type length: int
        :rtype: int
        """
        dp = [0]*(length+1)
        dp[1] = 1
        for i in range(2,length+1):
            for j in range(1,i):
                dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
        return dp[length]

if __name__ == '__main__':
    print(Solution().maxProductAfterCutting(8)) #18



'''
[Method 2]: 贪婪算法
首先把一个正整数 N 拆分成若干正整数只有有限种拆法，所以存在最大乘积。
假设 N = n1+n2+…+nk，并且 n1×n2×…×nk 是最大乘积。

显然1不会出现在其中；
如果对于某个 i 有 ni≥5，那么把 ni 拆分成 3+(ni−3)3+(ni−3)，我们有 3(ni−3)=3ni−9>ni3(ni−3)=3ni−9>ni；
如果 ni=4ni=4，拆成 2+2乘积不变，也就是说当绳子长度为4的时候其实没有必要剪，只是题目要求至少要剪一刀；
如果有三个以上的2，那么 3×3>2×2×2，所以替换成3乘积更大；
综上，选用尽量多的3，直到剩下2或者4时，用2。

[Time]: O(1)
[Space]: O(1)
'''
class Solution(object):
    def maxProductAfterCutting(self,length):
        """
        :type length: int
        :rtype: int
        """
        if length < 4:
            return length-1
        timesOf3 = length//3
        if length - 3*timesOf3 == 1: #最后余4的情况，最好拆成2*2>3*1
            timesOf3 -= 1
        timesOf2 = (length - 3*timesOf3)//2
        return 3**timesOf3*2**timesOf2


if __name__ == '__main__':
    print(Solution().maxProductAfterCutting(8))
