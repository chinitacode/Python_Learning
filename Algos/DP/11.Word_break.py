'''
139. Word Break [Medium]
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

[Analysis]:
wordDict 中的单词没有使用次数的限制，因此这是一个完全背包问题。
求解顺序的完全背包问题时，对物品的迭代应该放在最里层，对背包的迭代放在外层，
只有这样才能让物品按一定顺序放入背包中。

dp[j]表示以j作为结尾的s的子串能否用wordDict里的词来分割。
则对于wordDict里当前第i个word,
需要判断dp[j-len(word)]是否为True, 并且判断s[j-leng: j]是否等于word, 若都符合，则dp[j] = True
E.g.当j = 4，i = 0时，
dp[j - len(wordDict[i])] = dp[0]
我们在这里用dp[0]表示字符串开始前一位，可以看作是空格，空格在哪个单词都存在，所以我们令dp[0] = True
同时s[j-len(wordDict[i]): j] = s[0:4] = 'leet', 刚好等于wordDict[0] = 'leet'，
所以我们让dp[4] = True.
同理，当i = 1时，dp[8 - 4] = dp[4] == True, 并且s[4:8] == 'code',
所以dp[8] = True.

[注意]：
我们不能使dp[j] = (dp[j-len(word)] and s[j-leng: j] == word),
因为对于同一个j里面还有个word的内循环，如对'leet'时满足，dp[j]为True了,
则对下一个单词'code'则不会满足，dp[j]又会回到False，是没有意义的。

[Time]: O(len*n), len为字符串s的长度，n为wordDict元素的个数。
[Space]: O(n)
Runtime: 44 ms, faster than 77.03% of Python3 online submissions for Word Break.
Memory Usage: 14.1 MB, less than 5.55% of Python3 online submissions for Word Break.
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False]*n
        for j in range(1, n+1):
            for word in wordDict:
                leng = len(word)
                if dp[j-leng] and s[j-leng: j] == word:
                    dp[j] = True
        return dp[n]

'''
Else:
'''
#DFS + hashset, O(n^2), O(m), TLE
#n=len(s), m=len(wordDict)
#以s为基础，逐个增加字符个数，并在word Dict中查找
#利用visited[]剪枝，访问过的索引不再访问
#Helper函数的传入参数s不能再使用切片，否则无法与visited[]的索引相对应
#visited[]可以是表示是否访问过的0，1；也可以wordBreak存放访问结果True, False
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wordBreakHelper(s, start, visited):
            if start == len(s):
                return True
            if visited[start] == 0:
                visited[start] = 1
                for end in reversed(range(start + 1, len(s) + 1)):    #逆序更快
                    if s[start : end] in wordSet:
                        if wordBreakHelper(s, end, visited):
                            return True
            return False

        wordSet = set(wordDict)
        visited = [0] * len(s)
        return wordBreakHelper(s, 0, visited)
'''

#DFS, O(n^2), O(1) TLE
#以wordDict为基础，逐个word在s开头查找
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def wordBreakHelper(s, start, visited):
            if start == len(s):
                return True

            if visited[start] == 0:
                visited[start] = 1
                for word in wordDict:
                    if word == s[start : start + len(word)]:
                        if wordBreakHelper(s, start + len(word), visited):
                            return True
            return False

        visited = [0] * len(s)
        return wordBreakHelper(s, 0, visited)

#BFS, O(n^2), O(n)，TLE
#改进1
#利用visited[]剪枝，访问过的索引不再访问
'''
from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        wordSet = set(wordDict)
        visited = [0] * len(s)   #记录每个start索引的访问情况
        dq = deque()
        dq.append(0)    #从index=0处开始
        while dq:
            start = dq.popleft()
            if visited[start] == 0:
                for end in reversed(range(start + 1, len(s) + 1)):  #从长到短试验
                    if s[start : end] in wordSet:
                        dq.append(end)
                        if end == len(s):
                            return True
            visited[start] = 1
        return False
'''
#改进2
#利用hashset剪枝，访问过的索引不再进入队列
#deque与stack的性能相同，deque所需内存更大
'''
from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        wordSet = set(wordDict)
        visited = set()
        dq = deque()
        dq.append(0)    #从index=0处开始
        while dq:
            start = dq.popleft()
            for end in reversed(range(start + 1, len(s) + 1)):  #从长到短试验
                if s[start : end] in wordSet:
                    if end == len(s):
                        return True
                    if end not in visited:
                        dq.append(end)
                        visited.add(end)
        return False
'''
