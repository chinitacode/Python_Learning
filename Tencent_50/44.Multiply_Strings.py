'''
43. Multiply Strings [Medium]
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

[Method 1]:
This is the standard manual multiplication algorithm.
We use two nested for loops, working backward from the end of each input number.
We pre-allocate our result and accumulate our partial result in there.
One special case to note is when our carry requires us to write to our sum string outside of our for loop.
At the end, we trim any leading zeros, or return 0 if we computed nothing but zeros.

Time: O(n1*n2); Space: O(n1+n2)
Runtime: 176 ms, faster than 25.88% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.8 MB, less than 7.14% of Python3 online submissions for Multiply Strings.
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0]* (len(num1) + len(num2))
        for i, e1 in enumerate(reversed(num1)):
            for j, e2 in enumerate(reversed(num2)):
                res[i+j] += int(e1) * int(e2)
                res[i+j+1] += res[i+j]//10
                res[i+j] %= 10

        while len(res) > 1 and res[-1] == 0: res.pop()
        return ''.join( map(str,res[::-1]) )



'''
#or:
Runtime: 256 ms, faster than 9.84% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.8 MB, less than 7.14% of Python3 online submissions for Multiply Strings.
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i, d1 in enumerate(num1[::-1]):
            for j, d2 in enumerate(num2[::-1]):
                res += int(d1)*(10**i) * int(d2)*(10**j)
        return str(res)


'''
[Method 2]: add 0 considering the position of digit in numbers each time when multiplying
Runtime: 140 ms, faster than 48.32% of Python3 online submissions for Multiply Strings.
Memory Usage: 13.8 MB, less than 7.14% of Python3 online submissions for Multiply Strings.
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        #position of the current digit in num2
        c2 = 1

        for n1 in num1[::-1]:
            #position of the current digit in num1
            c1 = 1
            for n2 in num2[::-1]:
                res += int(n1) * int(n2) * c1 * c2
                c1 = c1* 10
            c2 *= 10

        return str(res)
