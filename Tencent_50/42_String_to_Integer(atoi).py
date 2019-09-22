'''
8. String to Integer (atoi) [Medium]

Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
 and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which
could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
If the numerical value is out of the range of representable values,
INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.


[Method 1] 手写slice条件 + try/except block
Time: O(n); Space: O(n)
Runtime: 36 ms, faster than 92.53% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 14 MB, less than 5.95% of Python3 online submissions for String to Integer (atoi).
'''
import sys
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if not str: return 0
        maxint = sys.maxsize
        minint = -sys.maxsize - 1
        str = str.split()[0]
        i = 1 if (str[0] == '-' or str[0] == '+') else 0
        while i < len(str):
            try:
                int(str[i])
                i += 1
            except:
                break
        try:
            num = int(str[:i])
            if minint < num < maxint:
                return num
            elif num < 0:
                return minint
            else:
                return maxint
        except:
            return 0

#[Note]: Leetcode 不识别sys模块，因此有：
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str: return 0
        maxint = 2147483647
        minint = -2147483648
        str = str.split()[0]
        i = 1 if (str[0] == '-' or str[0] == '+') else 0
        while i < len(str):
            try:
                int(str[i])
                i += 1
            except:
                break
        try:
            num = int(str[:i])
            if minint < num < maxint:
                return num
            elif num < 0:
                return minint
            else:
                return maxint
        except:
            return 0


#Or:用.isdigit()
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str: return 0
        maxint = 2147483647
        minint = -2147483648
        str = str.split()[0]
        i = 1 if (str[0] == '-' or str[0] == '+') else 0
        while i < len(str):
            if str[i].isdigit():
                i += 1
            else:
                break
        try:
            num = int(str[:i])
            if minint < num < maxint:
                return num
            elif num < 0:
                return minint
            else:
                return maxint
        except:
            return 0


'''
[Method 2]: regexp
注：就因为这道题这个解法专门花了一下午回顾了regexp...
Runtime: 40 ms, faster than 75.24% of Python3 online submissions for String to Integer (atoi).
Memory Usage: 13.8 MB, less than 5.95% of Python3 online submissions for String to Integer (atoi).
'''
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if not str: return 0
        maxint = 2147483647
        minint = -2147483648
        #？表示optional，出现0或1次
        exp = r'[-+]?\d+'
        #match()只从开头找
        str = re.match(exp, str)
        if str:
            num = int(str.group())
            if num > maxint:
                return maxint
            elif num < minint:
                return minint
            else:
                return num
        return 0
