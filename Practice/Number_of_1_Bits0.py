
class Solution:
    def NumberOf1(self, n):
        count = 0
        while n & 0xffffffff != 0:
            count += 1
            n = n & (n - 1)
            print(n)
        return count


##class Solution:
##    def NumberOf1(self, n):
##        # write code here
##        count = 0
##        while n:
##            count += 1
##            print(n)
##            n = n&(n-1)
##        return count

if __name__ == '__main__':
##    print(Solution().NumberOf1(3))
    print(Solution().NumberOf1(-1))
    
