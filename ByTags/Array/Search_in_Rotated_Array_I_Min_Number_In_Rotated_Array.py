'''
旋转数组的最小数字 [Medium]

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

输入一个升序的数组的一个旋转，输出旋转数组的最小元素。

例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。

数组可能包含重复项。

注意：数组内所含元素非负，若数组大小为0，请返回-1。

样例
输入：nums=[2,2,2,0,1]

输出：0
难度：中等
时/空限制：1s / 64MB
总通过数：1782
总尝试数：4234
来源：剑指Offer

[Method 1]: 二分法
因为不论数组是否旋转，两部分都是非递减排列好了的，
所以可以采用二分法解答这个问题，
使得当arr中元素不全为重复的1个元素时（worst case, O(n)）,
其时间复杂度可以降低为O(logn)。

mid = low + (high - low)/2
需要考虑三种情况：
(1)array[mid] > array[high]:
出现这种情况的array类似[3,4,5,6,0,1,2]，此时最小数字一定在mid的右边。
low = mid + 1
(2)array[mid] == array[high]:
出现这种情况的array类似 [1,0,1,1,1] 或者[1,1,1,0,1]，此时最小数字不好判断在mid左边
还是右边,这时只好一个一个试 ，
high = high - 1
(3)array[mid] < array[high]:
出现这种情况的array类似[3,4,5,0,1,2,3]或者[3,0,0,1,2,3,3],此时最小数字一定就是array[mid]
或者在mid的左边。因为右边必然都是递增的。
high = mid

'''
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
