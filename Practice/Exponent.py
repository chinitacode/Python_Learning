
# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0: return 1
        if exponent < 0:
            exponent = -exponent
            if base == 0:
                raise ZeroDivisionError
            base = 1/base 
        if exponent == 1: return base
        if exponent&1:
            return base*self.Power(base*base, exponent>>1)
        else:
            return self.Power(base*base, exponent>>1)

if __name__ == '__main__':
    print(Solution().Power(5,7))
    print(Solution().Power(0,0))
    print(Solution().Power(-5,3))
    print(Solution().Power(5,-3))
    print(Solution().Power(0,-5))
    
    

