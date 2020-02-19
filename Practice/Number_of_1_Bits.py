class Solution(object):
    def NumberOf1(self,n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            n = ((-n)^(2**32-1))+1
        count = 0
        while n:
            if n&1:
                count += 1
            n >>= 1
        return count

if __name__ == '__main__':
    print(Solution().NumberOf1(4294967294))
    print(Solution().NumberOf1(9))
    print(Solution().NumberOf1(-2))
            
        
