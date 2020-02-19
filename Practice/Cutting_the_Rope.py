class Solution(object):
    def maxProductAfterCutting(self,length):
        """
        :type length: int
        :rtype: int
        """
        if length < 4:
            return length-1
        timesOf3 = length//3
        if length - 3*timesOf3 == 1: #最后余4的情况，最好拆成2*2>3*1
            timesOf3 -= 1
        timesOf2 = (length - 3*timesOf3)//2
        return 3**timesOf3*2**timesOf2

        
if __name__ == '__main__':
    print(Solution().maxProductAfterCutting(8))
        
