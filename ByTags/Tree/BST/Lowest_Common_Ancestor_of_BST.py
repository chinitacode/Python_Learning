'''
235. Lowest Common Ancestor of a Binary Search Tree [Easy]
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node
 in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.


【注意！！！】题目没有说p.val一定小于q.val!


[Method 1]: Recursion
分析可得，只要p和q分立在root两端，或者p和q中其中有一个为root，LCA就为root；
反之，则根据其位置选择一边的子树进行递归。
[Time]: O(logn)，因为将problem size减半了。
[Space]: O(logn),递归树高度
Runtime: 72 ms, faster than 96.82% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or not p or not q: return None
        if p.val < root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

#Or(if p is not necessarily less than  q):
    def lowestCommonAncestor(self, root, p, q):
        if not root or not p or not q:
            return None
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

#Or One-liner version code:
def lowestCommonAncestor(self, root, p, q):
    return root if (root.val - p.val) * (root.val - q.val) < 1 else \
           self.lowestCommonAncestor((root.left, root.right)[p.val > root.val], p, q)

'''
[Method 2]: Iteration
[Time]: O(logn)
[Space]: O(1)
Runtime: 76 ms, faster than 91.14% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root

#Or:
def lowestCommonAncestor(self, root, p, q):
    while root:
        if max(p.val, q.val) < root.val:
            root = root.left
        elif min(p.val, q.val) > root.val:
            root = root.right
        else:
            return root
    return None
