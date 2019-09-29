'''
9. Palindrome Number
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?

[Method 1]: 用数学的方法先比较最外层的digits，然后处理x使之去掉已经比较了的digits，继续比较。
Time: O(lgn); Space: O(1)
Runtime: 88 ms, faster than 21.05% of Python3 online submissions for Palindrome Number.
Memory Usage: 14 MB, less than 6.50% of Python3 online submissions for Palindrome Number.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        #找出x的位数，如121,则ranger=100
        ranger = 1
        while x // ranger >= 10:
            ranger *= 10

        while x:
            left = x // ranger
            right = x % 10
            if left != right:
                return False

            #比较完最外面两个digit后，处理x
            x = (x % ranger) // 10
            ranger //= 100

        return True

'''
[Method 2]: Reverse 所有digits：把x reverse处理后与原x比较，若相等则return True。
Time: O(lgn); Space: O(1)
Runtime: 84 ms, faster than 28.09% of Python3 online submissions for Palindrome Number.
Memory Usage: 14 MB, less than 6.50% of Python3 online submissions for Palindrome Number.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        num, rev = x, 0
        while num > 0:
            rev *= 10
            rev += num%10
            num //= 10
        return rev == x

'''
[Method 3]: Reverse Half of the digits.
To avoid the overflow issue of the reverted number, (No worries in Python)
what if we only revert half of the int number?
As the reverse of the last half of the palindrome
should be the same as the first half of the number,
if the number is a palindrome.

[Note]:
1.首先需要处理以0结尾的数字如1210,因为根据（while x > rev）循环条件，
half reversed后的数字为012，即12，而剩下的x位12，则相等会返回True。
2.奇数位数字如121，half reversed后的数字为21，而x为1，因此需要把rev除掉10后再比较。

Time: O(log(lgn)), 每次x都会除以10，并且之比较一半的位数，所以再除以2；
Space: O(1)
Runtime: 76 ms, faster than 48.54% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.1 MB, less than 6.50% of Python3 online submissions for Palindrome Number.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x != 0): return False
        rev = 0
        while x > rev:
            rev *= 10
            rev += x%10
            x //= 10
        return rev == x or rev//10 == x


'''
[Method 3]: Fastest: Converting Integer to String
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
