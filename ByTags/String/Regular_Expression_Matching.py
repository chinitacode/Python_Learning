'''
10. Regular Expression Matching [Hard]

Given an input string (s) and a pattern (p),
implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'.
Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false


[Method 1]: Recursion
Intuition

If there were no Kleene stars (the * wildcard character for regular expressions),
the problem would be easier
 - we simply check from left to right if each character of the text matches the pattern.

When a star is present, we may need to check many different suffixes of the text
and see if they match the rest of the pattern.
A recursive solution is a straightforward way to represent this relationship.

If a star is present in the pattern, it will be in the second position pattern[1].
Then, we may ignore this part of the pattern, or delete a matching character in the text.
If we have a match on the remaining strings after any of these operations,
then the initial inputs matched.

Runtime: 1532 ms, faster than 5.78% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Regular Expression Matching.
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        if '*' not in p:
            return self.match(s, p)
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s,p[2:]) or first_match and self.isMatch(s[1:],p)
        return first_match and self.isMatch(s[1:],p[1:])

    def match(self, s, p):
            if not p: return not s
            first_match = bool(s) and p[0] in {s[0], '.'}
            return first_match and self.match(s[1:], p[1:])


'''
[Method 2]: Recursion + dictionary (dp)
[Time]: O(len(s)*len(p))
[Space]: O(len(s)*len(p))
Runtime: 64 ms, faster than 37.08% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Regular Expression Matching.
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.memo = dict()
        def dp(i, j):
            if (i,j) in self.memo:
                return self.memo[(i, j)]
            if j == len(p): return i == len(s)
            first_match = i < len(s) and p[j] in {s[i], '.'}
            if j <= len(p)-2 and p[j+1] == '*':
                ans = dp(i, j+2) or (first_match and dp(i+1, j))
            else:
                ans = first_match and dp(i+1, j+1)
            self.memo[(i,j)] = ans
            return ans
        return dp(0,0)

'''
[Method 3]: DP
[Time]: O(len(s)*len(p))
[Space]: O(len(s)*len(p))
Runtime: 96 ms, faster than 29.08% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Regular Expression Matching.
'''
class Solution(object):
    def isMatch(self, text, pattern):
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], '.'}
                if j+1 < len(pattern) and pattern[j+1] == '*':
                    dp[i][j] = dp[i][j+2] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]

'''
One-line cheatsheet:
'''
import re
class Solution:
    def isMatch(self, s, p):
        return s in re.findall(p, s)
# or:
class Solution:
    def isMatch(self, s, p):
        return bool(re.match(r"%s" %p, s)) and re.match(r"%s" %p, s).group() == s
