# -*- coding:utf-8 -*-
import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin: return None
        def helper(lo = 0, hi = len(tin)-1):
            #停止递归的条件
            if lo > hi:
                return None
            nonlocal root_idx
            root_val = pre[root_idx]
            root = TreeNode(root_val)
            idx = idx_map[root_val]
            #split tree
            root_idx += 1
            root.left = helper(lo,idx-1)
            root.right = helper(idx + 1, hi)
            return root

        root_idx = 0
        # O(n)
        idx_map = {val:idx for idx,val in enumerate(tin)}
        return helper()
    
    
    
class TestTree(unittest.TestCase):
    
    def test_empty(self):
        pre = [3,9,20,15,7]
        ino = [9,3,15,20,7]
        sol = Solution()
        r = sol.reConstructBinaryTree(pre,[])
        self.assertEqual(r,None)
        r = sol.reConstructBinaryTree([],[ino])
        self.assertEqual(r,None)

    def test_true(self):
        pre = [3,9,20,15,7]
        ino = [9,3,15,20,7]
        sol = Solution()
        r = sol.reConstructBinaryTree(pre,ino)
        self.assertEqual(r.val,3)
        self.assertEqual(r.left.val,9)
        self.assertEqual(r.right.right.val,7)
        


        
if __name__ == '__main__':
    unittest.main()
