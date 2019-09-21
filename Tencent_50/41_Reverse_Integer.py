'''
7. Reverse Integer [Easy]
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

[Note]:
Assume we are dealing with an environment
which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem,
assume that your function returns 0 when the reversed integer overflows.

[注意]: 如以下示例边际case，input为31位并未溢出，但是output则为34位溢出了，因此返回的是0。
[Input]:
1534236469
[Output]:
9646324351

而题目说的‘Given a 32-bit signed integer’，意思是给出的x一定是在32位里的带符号整数，
所以我们只需要检查输出的数字有没有溢出就可以了。

[Method 1.1]: str + Two-pointer
Time: O(lgn/2) = O(lgn)，lgn是因为最多循环n的位数（相当于每次除以10）
Runtime: 32 ms, faster than 96.18% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Reverse Integer.
'''
class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(x)
        if len(str_num) < 2: return x
        string_list = list(str_num)
        i, j = 1 if string_list[0] == ('-' or '+') else 0, len(string_list) - 1
        while i < j:
            string_list[i], string_list[j] = string_list[j], string_list[i]
            i += 1
            j -= 1
        n = int(''.join(string_list))
        return n if (-2**31) < n < (2**31 - 1) else 0

'''
[Method 1.2]: str + bit_length + abs() + cmp()

Because in Python we have:
>>> False - True
-1
>>> True - True
0
>>> False - False
0
>>> True - False
1

==> ((x > 0) - (x < 0)) return -1 if x < 0; return 0 if x == 0; return 1 if x > 0

Runtime: 36 ms, faster than 84.41% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.7 MB, less than 5.26% of Python3 online submissions for Reverse Integer.
'''
class Solution:
    def bit_length(self, n):
        s = bin(n)
        s = s.lstrip('-0b')
        return len(s)

    def reverse(self, x: int) -> int:
        n = ((x > 0) - (x < 0)) * int(str(abs(x))[::-1])
        return n if self.bit_length(n) < 32 else 0

'''
[Method 3]
翻转整数，那就在x%10后赋给新的值rev，每次遍历前新的值先乘以10，再加上取余后的数。
每次遍历后x都除以10，如果这个rev比32位最大整数还要大，或者比最小的还要小，则返回0。
否则遍历结束后，返回rev即可。
Time: O(lgn), Space: O(1)
Runtime: 36 ms, faster than 84.41% of Python3 online submissions for Reverse Integer.
Memory Usage: 14 MB, less than 5.26% of Python3 online submissions for Reverse Integer.
'''
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            rev = rev*10 + x%10
            x //= 10
        rev *= sign
        return rev if -2**31 < rev < 2**31 - 1 else 0
