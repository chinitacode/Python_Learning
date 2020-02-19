# -*- coding:utf-8 -*-
import unittest

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return None
        if rotateArray[0] < rotateArray[-1]:
            return rotateArray[0]
        lo, hi = 0, len(rotateArray)-1
        while lo < hi:
            mid = lo + (hi-lo)//2
            if rotateArray[mid] > rotateArray[hi]: #min肯定在右边
                lo = mid + 1
            elif rotateArray[mid] == rotateArray[hi]: #2种情况，前面重复或者后面重复
                #如[1,1,1,0,1]和[1,0,1,1,1]，无法区分在左还是在右，只能1个个地试
                hi -= 1 #因为都是非递减
            else:
                hi = mid
        return rotateArray[lo]
            
                
                


        
class TestSol(unittest.TestCase):
    def setUp(self):
        self.f = Solution().minNumberInRotateArray

    def test_value(self):
        self.assertEqual(self.f([]), None)
        self.assertEqual(self.f([3]),3)

    def test_non_rotated(self):
        self.assertEqual(self.f([3,3,4,5]),3)
        self.assertEqual(self.f([3,3,3,3]),3)

    def test_rotated(self):
        self.assertEqual(self.f([2,2,3,3,1,2]),1)
        self.assertEqual(self.f([3,4,5,1,2]),1)

if __name__ == '__main__':
    unittest.main()
