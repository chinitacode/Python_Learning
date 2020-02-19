# -*- coding:utf-8 -*-

import unittest

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if target is None or not array or not array[0]: return False
        rows = len(array)
        cols = len(array[0])
        i, j = rows - 1, 0
        while i >= 0 and j < cols:
            if array[i][j] == target:
                return True
            if array[i][j] < target:
                j += 1
            else:
                i -= 1
        return False

class TestFind(unittest.TestCase):
    def test_empty(self):
        s = Solution()
        arr = [[1,2,3,5],[2,3,4,6],[3,5,7,11]]
        self.assertEqual(s.Find(None, arr),False)
        self.assertEqual(s.Find(3, []),False)
        self.assertEqual(s.Find(7, [[]]),False)

    
    def test_t(self):
        s = Solution()
        arr = [[1,2,3,5],[2,3,4,6],[3,5,7,11]]
        self.assertEqual(s.Find(4, arr),True)
        self.assertEqual(s.Find(8, arr),False)
        self.assertEqual(s.Find(13, arr),False)
        arr2 = [[1,2,3,5],[6,7,8,20],[9,11,17,21]]
        self.assertEqual(s.Find(20, arr2),True)
        self.assertEqual(s.Find(4, arr2),False)
        self.assertEqual(s.Find(15, arr2),False)

if __name__ == '__main__':
    unittest.main()
