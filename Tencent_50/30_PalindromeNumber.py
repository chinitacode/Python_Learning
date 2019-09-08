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

Method1:
Runtime: 88 ms, faster than 21.05% of Python3 online submissions for Palindrome Number.
Memory Usage: 14 MB, less than 6.50% of Python3 online submissions for Palindrome Number.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        ranger = 1
        while x // ranger >= 10:
            ranger *= 10

        while x:
            left = x // ranger
            right = x % 10
            if left != right:
                return False
            
            x = (x % ranger) // 10
            ranger //= 100

        return True
        
'''
Method2: Fastest

'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
        
        
'''
Method3
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0 or (x%10==0 and x!=0)):return False
        rev=0
        while(x>rev):
            rev=rev*10
            rev+=x%10
            x=x//10
        if(rev==x or rev//10==x):
            return True
        else:
            return False
