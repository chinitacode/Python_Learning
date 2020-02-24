'''
面试题26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false

示例 2：
输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000

[前序遍历+递归]
首先要遍历A找出与B根节点一样值的节点R，即找到入口
然后递归判断树A中以R为根节点的子树是否包含和B一样的结构
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        res = False
        if A and B:
            if A.val == B.val:
                res = self.isSubTree(A, B)
            if not res:
                res = self.isSubStructure(A.left, B)
            if not res:
                res = self.isSubStructure(A.right, B)
        return res

    def isSubTree(self, A, B):
        if not B: return True
        if not A or A.val != B.val: return False
        return self.isSubTree(A.left, B.left) and self.isSubTree(A.right, B.right)
