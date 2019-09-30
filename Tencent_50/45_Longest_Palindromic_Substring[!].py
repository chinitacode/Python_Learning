'''
5. Longest Palindromic Substring [Medium]

Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"

[Method 1]: Brute Force, from middle to outside
Time: O(n^2), worst case: 'aaaaaaa'; Space: O(n)
Runtime: 976 ms, faster than 68.71% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.7 MB, less than 22.69% of Python3 online submissions for Longest Palindromic Substring.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for i in range(len(s)):
            #while the palindrome string has odd length:
            tmp = self.palindrome_at(s, i, i)
            if len(tmp) > len(longest):
                longest = tmp

            #even cases like 'abba':
            tmp = self.palindrome_at(s, i, i+1)
            if len(tmp) > len(longest):
                longest = tmp
        return longest
    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def palindrome_at(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
'''
#或者用max()
Runtime: 952 ms, faster than 74.18% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 13.6 MB, less than 23.53% of Python3 online submissions for Longest Palindromic Substring.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for i in range(len(s)):
            #while the palindrome string has odd length:
            longest = max(self.palindrome_at(s, i, i), self.palindrome_at(s, i, i+1), longest, key = len)
        return longest

    def palindrome_at(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


'''
[Method 2]: DP
解决这类 “最优子结构” 问题，可以考虑使用 “动态规划”：

1、定义 “状态”；
2、找到 “状态转移方程”。


1、定义 “状态”，这里 “状态”数组是二维数组。
dp[l][r] 表示子串 s[l, r]（包括区间左右端点）是否构成回文串，是一个二维布尔型数组。
即如果子串 s[l, r] 是回文串，那么 dp[l][r] = true。

2、找到 “状态转移方程”。
首先，我们很清楚一个事实：

1、当子串只包含 1 个字符，它一定是回文子串；

2、当子串包含 2 个以上字符的时候：如果 s[l, r] 是一个回文串，例如 “abccba”，
那么这个回文串两边各往里面收缩一个字符（如果可以的话）的子串 s[l + 1, r - 1] 也一定是回文串，
即：如果 dp[l][r] == true 成立，一定有 dp[l + 1][r - 1] = true 成立。

根据这一点，我们可以知道，给出一个子串 s[l, r] ，如果 s[l] != s[r]，那么这个子串就一定不是回文串。
如果 s[l] == s[r] 成立，就接着判断 s[l + 1] 与 s[r - 1]，这很像中心扩散法的逆方法。

事实上，当 s[l] == s[r] 成立的时候，dp[l][r] 的值由 dp[l + 1][r - l] 决定，
这一点也不难思考：当左右边界字符串相等的时候，整个字符串是否是回文就完全由“原字符串去掉左右边界”的子串是否回文决定。
但是这里还需要再多考虑一点点：“原字符串去掉左右边界”的子串的边界情况。

1、当原字符串的元素个数为 3 个的时候，如果左右边界相等，那么去掉它们以后，只剩下 1 个字符，它一定是回文串，故原字符串也一定是回文串；

2、当原字符串的元素个数为 2 个的时候，如果左右边界相等，那么去掉它们以后，只剩下 0 个字符，显然原字符串也一定是回文串。

把上面两点归纳一下，只要 s[l + 1, r - 1] 至少包含两个元素，就有必要继续做判断，否则直接根据左右边界是否相等就能得到原字符串的回文性。
而“s[l + 1, r - 1] 至少包含两个元素”等价于 l + 1 < r - 1，整理得 l - r < -2，或者 r - l > 2。

综上，如果一个字符串的左右边界相等，以下二者之一成立即可：
1、去掉左右边界以后的字符串不构成区间，即“ s[l + 1, r - 1] 至少包含两个元素”的反面，即 l - r >= -2，或者 r - l <= 2；
2、去掉左右边界以后的字符串是回文串，具体说，它的回文性决定了原字符串的回文性。

于是整理成“状态转移方程”：

dp[l][r] = (s[l] == s[r] and (l - r >= -2 or dp[l + 1][r - 1]))
或者
dp[l][r] = (s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]))
编码实现细节：因为要构成子串 l 一定小于等于 r ，我们只关心 “状态”数组“上三角”的那部分取值。

Time: O(n^2), Space: O(n^2)
Runtime: 2584 ms, faster than 42.59% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 21.6 MB, less than 9.25% of Python3 online submissions for Longest Palindromic Substring.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        longest = s[0]
        dp = [[0] * len(s) for i in range(len(s))]
        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, len(s)):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]):
                    dp[l][r] = 1
                    if r-l+1 > len(longest):
                        longest = s[l:r+1]
        return longest


'''
[Method 3]: ***** Manacher Algorithm *****
Based on this article: https://segmentfault.com/a/1190000003914228#articleHeader5
Time: O(n), Space: O(n)
Runtime: 92 ms, faster than 95.35% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14 MB, less than 22.69% of Python3 online submissions for Longest Palindromic Substring.
'''
class Solution:
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        #C is the index of the center of the current palindrome;
        #R is the index of the end position of the current palindrome;
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to j = C - (i-C),which is i´ centered at C
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
