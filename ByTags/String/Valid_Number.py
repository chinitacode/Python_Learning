'''
65. Valid Number [Hard]
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.
However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

【剑指offer版】
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

注意:

小数可以没有整数部分，例如.123等于0.123；
小数点后面可以没有数字，例如233.等于233.0；
小数点前面和后面可以有数字，例如233.666;
当e或E前面没有数字时，整个字符串不能表示数字，例如.e1、e1；
当e或E后面没有整数时，整个字符串不能表示数字，例如12e、12e+5.4;

[Method 1]: 拆分法
可以写成 A[.[B]][e/EC], 即有整数存在时，和无整数存在时的 .B[e/EC]。
A为数值整数部分（可以有正负号的整数），B为紧跟着小数点的为数值的小数部分（无正负号的整数），
C为紧跟着e/E为数值的指数部分（可以有正负号的整数）。
整体的逻辑为：
1.因为[e/EC]可存在可不存在，影响最小，所以一开始我们就可以先搞定C：
  如果e/E存在则C为isInteger()扫描后的返回值，不然就为True（所有的返回我们都带上and C）
2.如果存在小数点：
  (1)如果A不存在则B必须存在：
     如果B不存在：return False
     否则return B and C
  (2)如果B存在：
     return A and B and C
  否则return A and C
 3.如果不存在小数点：
   return A and C

[Time]: O(n)
[Space]: O(1)
Runtime: 32 ms, faster than 67.66% of Python3 online submissions for Valid Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Number.
'''
import unittest

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s: return False
        dot_pos = s.find(".")
        e, E = s.find("e"), s.find("E")
        e_pos =  e if e != -1 else E
        if e_pos != -1 and e_pos < dot_pos: return False # e/E后不能有小数
        C = self.isInteger(s, e_pos+1, len(s)-1) if e_pos != -1 else True
        if dot_pos != -1:
            B = self.isUnsignedInteger(s, dot_pos+1, e_pos-1 if (e_pos != -1) else (len(s)-1))
            if dot_pos == 0 or (dot_pos == 1 and s[0] in ("+", "-")): # 如果A不存在，B必须存在
                if dot_pos == len(s)-1 or dot_pos + 1 == e_pos: return False # 如果B不存在
                return B and C
            A = self.isInteger(s, 0, dot_pos-1)
            if not(dot_pos == len(s)-1 or dot_pos + 1 == e_pos): # 如果B存在
                return A and B and C
            return A and C
        A = self.isInteger(s, 0, e_pos-1 if (e_pos != -1) else (len(s)-1))
        return A and C

    def isInteger(self, s, i, j):
        if 0 <= i < len(s) and 0 <= j < len(s):
            if s[i] in ("+", "-"):
                i += 1
            return self.isUnsignedInteger(s, i, j)
        return False

    def isUnsignedInteger(self, s, i, j):
        if i > j: return False # 不能为空
        if 0 <= i < len(s) and 0 <= j < len(s):
            for index in range(i, j+1):
                if not s[index].isdigit():
                    return False
            return True
        return False

'''
[Method 1.2] 逻辑判断法：
Use 3 flags
We use three flags: met_dot, met_e, met_digit, mark if we have met ., e
or any digit so far. First we strip the string,
then go through each char and make sure:

If char == + or char == -, then prev char (if there is) must be e
. cannot appear twice or after e
e cannot appear twice, and there must be at least one digit before and after e
All other non-digit char is invalid

Runtime: 28 ms, faster than 86.73% of Python3 online submissions for Valid Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Number.
'''
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in ['+', '-']:
                if i > 0 and s[i-1] != 'e':
                    return False
            elif char == '.':
                if met_dot or met_e: return False
                met_dot = True
            elif char == 'e':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False # e后必须接，所以这时重置met_digit为False,以免e为最后一个char
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit

'''
[Method 2]: 正则表达式
按照法一的思路，可得正则表达式：
^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$

Runtime: 28 ms, faster than 86.73% of Python3 online submissions for Valid Number.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Valid Number.
'''
import re
class Solution:
    p = re.compile(r'^[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?$')
    def isNumber(self, s: str) -> bool:
        return bool(self.p.match(s.strip()))


'''
[Method 3]: DFA(deterministic finite automaton, 确定性有限自动机)
Runtime: 28 ms, faster than 86.73% of Python3 online submissions for Valid Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Valid Number.
Next challenges:
'''
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define DFA state transition tables
        states = [{},
                 # State (1) - initial state (scan ahead thru blanks)
                 {'blank': 1, 'sign': 2, 'digit':3, '.':4},
                 # State (2) - found sign (expect digit/dot)
                 {'digit':3, '.':4},
                 # State (3) - digit consumer (loop until non-digit)
                 {'digit':3, '.':5, 'e':6, 'blank':9},
                 # State (4) - found dot (only a digit is valid)
                 {'digit':5},
                 # State (5) - after dot (expect digits, e, or end of valid input)
                 {'digit':5, 'e':6, 'blank':9},
                 # State (6) - found 'e' (only a sign or digit valid)
                 {'sign':7, 'digit':8},
                 # State (7) - sign after 'e' (only digit)
                 {'digit':8},
                 # State (8) - digit after 'e' (expect digits or end of valid input)
                 {'digit':8, 'blank':9},
                 # State (9) - Terminal state (fail if non-blank found)
                 {'blank':9}]
        currentState = 1
        for c in s:
            # If char c is of a known class set it to the class name
            if c in '0123456789':
                c = 'digit'
            elif c in ' \t\n':
                c = 'blank'
            elif c in '+-':
                c = 'sign'
            # If char/class is not in our state transition table it is invalid input
            if c not in states[currentState]:
                return False
            # State transition
            currentState = states[currentState][c]
        # The only valid terminal states are end on digit, after dot, digit after e, or white space after valid input
        if currentState not in [3,5,8,9]:
            return False
        return True

'''
[Method 4]: 投机法（不可取）

'''
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except :
            return False

'''
Unittest
'''
class TestIsNumeric(unittest.TestCase):
    def setUp(self):
        self._f = Solution().isNumber

    def test_float(self):
        self.assertEqual(self._f("."), False)
        self.assertEqual(self._f("+."), False)
        self.assertEqual(self._f("233.666"), True)
        self.assertEqual(self._f(".123"), True)
        self.assertEqual(self._f("+.123"), True)
        self.assertEqual(self._f("233."), True)

    def test_sign(self):
        self.assertEqual(self._f("+233.666"), True)
        self.assertEqual(self._f("-233.666"), True)
        self.assertEqual(self._f("+-233.666"), False)
        self.assertEqual(self._f("+233.-666"), False)

    def test_e(self):
        self.assertEqual(self._f("e1"), False)
        self.assertEqual(self._f(".e1"), False)
        self.assertEqual(self._f(".12e1"), True)
        self.assertEqual(self._f("12e+3"), True)
        self.assertEqual(self._f("3e-8"), True)
        self.assertEqual(self._f("1.2e+3"), True)
        self.assertEqual(self._f("1.2e+-3"), False)
        self.assertEqual(self._f("12e"), False)
        self.assertEqual(self._f("12e+5.4"), False)

    def test_E(self):
        self.assertEqual(self._f("E1"), False)
        self.assertEqual(self._f("+E1"), False)
        self.assertEqual(self._f(".E1"), False)
        self.assertEqual(self._f(".12E1"), True)
        self.assertEqual(self._f("12E+3"), True)
        self.assertEqual(self._f("3E-8"), True)
        self.assertEqual(self._f("1.2E+3"), True)
        self.assertEqual(self._f("1.2E+-3"), False)
        self.assertEqual(self._f("12E"), False)
        self.assertEqual(self._f("12E+5.4"), False)

    def test_space(self):
        self.assertEqual(self._f(" 1"), True)
        self.assertEqual(self._f("1 "), True)
        self.assertEqual(self._f("1 2"), False)
        self.assertEqual(self._f(" -90e3   "), True)

if __name__ == '__main__':
    unittest.main()
