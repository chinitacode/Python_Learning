'''
【重要】二叉树的下一个节点 [Medium]

给定一棵二叉树的其中一个节点，请找出中序遍历序列的下一个节点。

注意：

如果给定的节点是中序遍历序列的最后一个，则返回空节点;
二叉树一定不为空，且给定的节点一定不是空节点；
样例

E.G.1：假定二叉树是：[2, 1, 3, null, null, null, null]， 给出的是值等于2的节点。

则应返回值等于3的节点。

该二叉树的结构如下，2的后继节点是3。
  2
 / \
1   3



E.G.2

  2
 / \
1   3
   /  \
  4    9

2的后继节点时4
中序遍历为：[1,2,4,3,9]


E.G.3
       5
     /
    /
   /
  2
 / \
1   3
   /  \
  4    9

9的后继节点为5
中序遍历为：[1,2,4,3,9,5]


因为对于中序遍历：
1、有右子树的，那么下个结点就是右子树最左边的点，
2、没有右子树的，也可以分成两类：
a)是父节点左孩子 ，那么父节点就是下一个节点，如E.G.2中的1，4
b)是父节点的右孩子，但是可能是某上层节点（如根节点）的左子树，所以必须找找他的父节点的父节点的父节点...
直到当前结点是其上层节点的左孩子，如E.G.3的9.
如果没有那么他就是尾节点，如E.G.2中9。

时间复杂度分析
不论往上找还是往下找，总共遍历的节点数都不大于树的高度。
所以时间复杂度是 O(h)，其中 h 是树的高度。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.father = None
class Solution(object):
    def inorderSuccessor(self, q):
        """
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not q: return None
        if q.right:
            node = q.right
            while node.left:
                node = node.left
            return node
        else:
            while q.father:
                if q == q.father.left:
                    return q.father
                q = q.father
            return None
