'''
93. Restore IP Addresses [Medium]

Given a string containing only digits,
restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]


[Method 1]: Recursion + dfs
[Time]: C(11,3)
[Space]: O(1)，由于这个问题限制在有效 IP 段内，树最多 4 层，保存的结果集也是有限个。
Runtime: 28 ms, faster than 86.85% of Python3 online submissions for Restore IP Addresses.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Restore IP Addresses.
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        # part为0表示已经处理了0部分，即最开始
        self.dfs(s, 0, "", res)
        return res

    # part stands for the number of parts already dealed
    def dfs(self, s, part, path_string, res):
        if part == 4:
            if not s:
                res.append(path_string[:-1])  # [:-1]是为了去掉最后一次递归多加的'.'
            return
        for num_digit in range(1,4): # 每部分都有至少1个至多3个数字
            if num_digit <= len(s):
                if num_digit == 1: # 该部分只取1个数字
                    self.dfs(s[num_digit:], part+1, path_string + s[:num_digit] + '.', res)
                elif num_digit == 2 and s[0] != '0':
                    self.dfs(s[num_digit:], part+1, path_string + s[:num_digit] + '.', res)
                elif num_digit == 3 and s[0] != '0' and int(s[:num_digit]) < 256:
                    self.dfs(s[num_digit:], part+1, path_string + s[:num_digit] + '.', res)


'''
[Method 3]: Brute Force
'''
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n, res = len(s), []
        for a in range(1,4):
            for b in range(a+1,a+4):
                for c in range(b+1,b+4):
                    if 0 < n-c < 4:
                        tmp = (s[:a], s[a:b], s[b:c], s[c:])
                        if all(int(x) < 256 and str(int(x)) == x for x in tmp):
                            res.append(".".join(tmp))
        return res

# or one-liner:
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [".".join((s[:a],s[a:b],s[b:c],s[c:])) \
                for a in range(1,4) for b in range(a+1,a+4) for c in range(b+1,b+4) \
                if 0 < len(s)-c < 4 and all(int(x) < 256 and str(int(x)) == x \
                for x in (s[:a],s[a:b],s[b:c],s[c:]))]



'''
[Method 4]: Regex
'''
from re import match
vre = [r'[0-9]', r'[1-9][0-9]', r'1[0-9][0-9]|2[0-4][0-9]|25[0-5]']

class Solution(object):
    def restoreIpAddresses(self, s):
        possible = lambda s: (match(regx, s).group() for regx in vre if match(regx, s))
        def helper(s, depth):
            if not depth:
                return [] if s else [[]]
            return [[p]+r for p in possible(s)
                          for r in helper(s[len(p):], depth-1)]
        return map('.'.join, helper(s, 4))
