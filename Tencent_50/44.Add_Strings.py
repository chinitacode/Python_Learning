'''
415. Add Strings [Easy]
Given two non-negative integers num1 and num2 represented as string,
return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

[Method 1]: 先从最低位相加，若长度不同，再把高位补足
Runtime: 56 ms, faster than 37.28% of Python3 online submissions for Add Strings.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Add Strings.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        Sum = 0
        carry = 1
        for (d1,d2) in zip(num1[::-1], num2[::-1]):
            Sum += (int(d1) + int(d2))*carry
            carry *= 10

        if len(num1) > len(num2):
            carry = 10**len(num2)
            for d1 in num1[len(num1)-len(num2)-1::-1]:
                Sum += int(d1)*carry
                carry *= 10

        elif len(num1) < len(num2):
            carry = 10**len(num1)
            for d2 in num2[len(num2)-len(num1)-1::-1]:
                Sum += int(d2)*carry
                carry *= 10
        return str(Sum)

'''
[Method 2]: 把短的字符串高位补足0
Time: O(max(n1,n2))
Runtime: 56 ms, faster than 37.28% of Python3 online submissions for Add Strings.
Memory Usage: 14 MB, less than 5.55% of Python3 online submissions for Add Strings.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num2 = '0'*(len(num1) - len(num2)) + num2
        else:
            num1 = '0'*(len(num2) - len(num1)) + num1
        Sum = 0
        carry = 1
        for (d1,d2) in zip(num1[::-1], num2[::-1]):
            Sum += (int(d1) + int(d2))*carry
            carry *= 10
        return str(Sum)

'''
[Method 3]: 把短的字符串高位补足0，按位把字符串加在前面
Runtime: 44 ms, faster than 83.09% of Python3 online submissions for Add Strings.
Memory Usage: 13.9 MB, less than 5.55% of Python3 online submissions for Add Strings.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num2 = '0'*(len(num1) - len(num2)) + num2
        else:
            num1 = '0'*(len(num2) - len(num1)) + num1
        Sum = ''
        carry = 0
        for (d1,d2) in zip(num1[::-1], num2[::-1]):
            d = (int(d1) + int(d2) + carry)
            carry = d//10
            Sum = str(d%10) + Sum
        if carry > 0:
            Sum = str(carry) + Sum
        return Sum

'''
[Method 4]:按照ord('0') = 48来转换成integer，相加后再取str()
O(n1 + n2) = O(n)
Runtime: 60 ms, faster than 23.88% of Python3 online submissions for Add Strings.
Memory Usage: 13.8 MB, less than 5.55% of Python3 online submissions for Add Strings.
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 = n1*10 + ord(num1[i])-48
        for i in range(len(num2)):
            n2 = n2*10 + ord(num2[i])-48
        return str(n1+n2)
