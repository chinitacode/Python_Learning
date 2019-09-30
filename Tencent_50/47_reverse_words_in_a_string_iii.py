'''
557. Reverse Words in a String III [Easy]
Given a string, you need to reverse the order of characters in each word within a sentence
while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.

[Method 1]: 用split(), join() and string slicing
Time: O(n), where nn is the length of the string.
Space: O(n)
Runtime: 36 ms, faster than 90.28% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.5 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return ''
        words = s.split(' ')
        reverse = [word[::-1] for word in words]
        return ' '.join(reverse)


#Or:
        return " ".join([i[::-1] for i in s.split()])

'''
[Method 2]: 手写split()和reverse()
Time: O(n)
Runtime: 116 ms, faster than 6.52% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.4 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s: return ''
        words = self.split(s, ' ')
        rev_words = []
        for word in words:
            rev_words.append(self.reverse(word))

        return ' '.join(rev_words)

    def split(self, s, delimiter):
        ans = []
        word = ''
        for char in s:
            if char == delimiter:
                ans.append(word)
                word = ''
                continue
            word += char
        ans.append(word)
        return ans

    def reverse(self, s):
        s = list(s)
        mid = len(s)//2
        for i in range(mid):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
        return ''.join(s)

'''
[Method 3]: Using Stack
利用stack先进后出的性质，把每一个单词按字符加进stack，
遇到空格时就把stack里的已存单词的字符按顺序一个个Pop到最终要输出的字符串ans里，再加一个空格隔开；
要特别注意的是，输入字符串里的末端是没有空格的，所以我们最后要手动地把存在stack里的最后一个单词按老方法加入ans。
Time: O(n)
Runtime: 124 ms, faster than 5.18% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.1 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        stack, ans = [], ''
        for char in s:
            if char == ' ':
                while stack:
                    ans += stack.pop()
                ans += ' '
                continue
            stack.append(char)
        while stack:
            ans += stack.pop()
        return ans


'''
#也可以手动地给输入字符串末端添加空格，最后输出时切片处理去掉开始的空格：
Runtime: 120 ms, faster than 5.81% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.2 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s + ' '
        stack, ans = [], ''
        for char in s:
            if char == ' ':
                while stack:
                    ans += stack.pop()
                ans += ' '
                continue
            stack.append(char)
        return ans[:-1]
'''
#Or:
Runtime: 120 ms, faster than 5.81% of Python3 online submissions for Reverse Words in a String III.
Memory Usage: 14.1 MB, less than 7.69% of Python3 online submissions for Reverse Words in a String III.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s + " "
        stack, res=[], ""
        for i in s:
            stack.append(i)
            if i == " ":
                while stack:
                    res += stack.pop()
        return res[1:]

'''
还可以用双指针l,r标记单词的首位，遇到空格就把单词反着加进输出字符串并且更新l,r；
但是添加单词的过程中实际上还是用的stack结构，或者再从r循环到l添加，但是这样的话时间复杂度就大大增加了。
'''
