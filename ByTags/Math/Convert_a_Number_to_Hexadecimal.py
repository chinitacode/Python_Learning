'''
405. Convert a Number to Hexadecimal [Easy]

Given an integer, write an algorithm to convert it to hexadecimal.
For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero,
it is represented by a single zero character '0';
otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:
Input:
26

Output:
"1a"

Example 2:
Input:
-1

Output:
"ffffffff"

[Note]:
16进制表示方法：0xffffffff = 16**8 = 2**32 = 4294967296

[2的补码方法]：
1.正数的原码、反码、补码均为本身。
2.负数的补码：
  1.其反码 + 1.
  其中求反码有以下方式：
  a.用最大整数 max_int 与 原负数相加（实际上是减去其绝对值），
  比如说8位能表示的最大整数位（11111111）2 = 2**8 - 1 = 255，
  则-1的反码就为(11111111)2 - (1)10 = (11111110)2
  b.把其绝对值逐位与最大整数进行XOR异或操作，因为0^1 = 1, 1^1 = 0, 正好取反。
  2.或直接加上最大整数+1（和为2**8比如说）

但因为在这是用16进制表示，所以最大整数是16**8 = 2**32，或者直接用0xffffffff。
所以num处理为：
    num += 0xffffffff + 1
    或者
    (-num)^0xffffffff
    或者
    num += 2**32

[Method 1]:
[Time]: O(logn)
[Space]: O(1)
Runtime: 16 ms, faster than 72.46% of Python online submissions for Convert a Number to Hexadecimal.
Memory Usage: 11.8 MB, less than 25.00% of Python online submissions for Convert a Number to Hexadecimal.
'''
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        res = ''
        if num < 0:
            num += 0xffffffff + 1
        while num:
            digit = num%16
            res += str(digit) if digit < 10 else (chr(ord('a') + digit - 10))
            num //= 16
        return res[::-1]

'''
[Method 2]:
'''
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num < 0:
            num += 2 ** 32

        stack = []
        s = "0123456789abcdef"

        while num:
            stack.append(s[num % 16])
            num //= 16

        if not stack:
            return "0"

        stack.reverse()
        return "".join(stack)
