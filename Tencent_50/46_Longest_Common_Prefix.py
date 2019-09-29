'''
14. Longest Common Prefix [Easy]

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

[Method 1]: 取input list里最后一个字符串作为比较的reference，
从其第一位字符开始，比较剩下list里每个字符串相应的位数，只要出现问题（位数不够）或者结果不相等，
就立刻返回prefix字符串。
Time: O(m(n-1)), m为input list里最后一个字符串的长度，n为input list里元素个数；
Space: O(1)
Runtime: 40 ms, faster than 72.36% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.7 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1: return ''
        prefix = ''
        refer = strs[-1]
        strs.pop()
        i = 0
        for char in refer:
            for word in strs:
                if i > len(word) - 1 or char != word[i]: return prefix
            prefix += char
            i += 1
        return prefix


'''
[Optimization]: 选取input list里面长度最短的字符串作为比较的参照，然后对每个字符串相应位数进行比较。
Time: O(m + mn), m为最短字符串长度，n为字符串个数；
Space: O(1)
Runtime: 36 ms, faster than 91.36% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.7 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1: return ''
        prefix = ''
        refer = min(strs, key = len)
        for i, char in enumerate(refer):
            for word in strs:
                if char != word[i]: return prefix
            prefix += char
        return prefix


'''
[Method 2]: Divide and Conquer
Time: O(mn),最坏情况下，我们有n个长度为m的相同字符串,每两个字符串都需要比较；
如果input是9个字符串，那么实际上会进行8次比较，每次比较都会比较m个字符（最坏）。
Space: O(mn)
Runtime: 44 ms, faster than 40.31% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.6 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        if len(strs) == 1: return strs[0]
        if len(strs) == 2:
            prefix = ''
            for (s1,s2) in zip(strs[0],strs[1]):
                if s1 != s2: return prefix
                prefix += s1
            return prefix
        left = self.longestCommonPrefix(strs[:len(strs)//2])
        right = self.longestCommonPrefix(strs[len(strs)//2:])
        return self.longestCommonPrefix([left, right])

#或者不用slicing:
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        def comparetwo(a,b):
            result = ''
            for m,n in zip(a,b):
                if m == n:
                    result += m
                else:
                    return result
            return result
        def divide(start,end):
            mid = int((start + end)/2)
            if mid == start and mid == end:
                return strs[mid]
            elif mid == start and mid != end:
                return comparetwo(strs[start],strs[end])
            else:
                a = divide(start,mid)
                b = divide(mid+1,end)
                return comparetwo(a,b)

        return divide(0,len(strs)-1)

'''
[Method 3] Python zip() and set()
【第一行】每次都取各个字符串的同一列字符，放进 set，set 中不会储存重复元素，所以长度为1代表各个字符都是相同的，此时 == 会让它变成 True
【第二行】index 搜索第一个 0 的位置，0 与 False 在值上是等价的，相当于搜索第一个 False 的位置也就是公共前缀的长度

Time: O(m(nm)), set()需要O(m),m为input list里字符串个数，zip()则需要O（mn），n为最短字符串的长度。
[Note]: 关于zip()的时间复杂度：
1.可以将它看作一个循环，向zip添加一个参数将在每次迭代中添加O(1)，
或者在所有n迭代中添加O(n)。(假设最小参数的大小为n)

例如，对于zip(X1,X2,...,Xm)，您正在做O(mn)的工作，
但是m是常量，所以它是O(n)。(再次假设参数的最小大小为n)

2.zip(*args)的运行时间为O(len(args) * min(len(a) for a in args)。
如果没有对参数(例如，列表的数量(len(args))是常量)的特定假设，就不能将其归结为O(n))。

如果列表的长度都相同，那么可以使用单个长度n来代替最小长度的计算，
并使用m来表示列表的数量，并将其写成O(m * n)。
如果列表的数量不变，那么m的因数是一个常量，可以删除，只留下O(n)。
Runtime: 36 ms, faster than 91.30% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 13.9 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = [len(set(chars)) == 1 for chars in zip(*strs)] + [0]
        return strs[0][:res.index(0)] if strs else ''
'''
把代码展开相当于：
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res


'''
[Method 4]:
按字典排序数组，比较第一个，和最后一个单词，有多少前缀相同。
如['flower', 'flow', 'flight']，按字典序排序后变成了['flight', 'flow', 'flower']，
列表首位和末位为差别最大的两个字符串，只需要比较这两个即可。
Time: O(nlogn + m)
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        strs.sort()
        a = strs[0]
        b = strs[-1]
        prefix = ''
        for (c1,c2) in zip(a,b):
            if c1 != c2: break
            prefix += c1
        return prefix

#或者不用zip（）
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        s.sort()
        n = len(s)
        a = s[0]
        b = s[n-1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res
