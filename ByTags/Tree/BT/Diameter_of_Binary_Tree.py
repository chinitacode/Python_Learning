'''
543. Diameter of Binary Tree [Easy]
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

[Method 1]: Recursion
实际上有可能并不包含根节点，所以还是需要通过设置一个全局变量来记录最大路径长度，
每次递归都要通过比较来更新这个全局变量，最终返回它。
时间复杂度：O(N)，每个节点只访问一次。
空间复杂度：O(N)，深度优先搜索的栈开销。
Runtime: 48 ms, faster than 71.95% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 14.4 MB, less than 100.00% of Python3 online submissions for Diameter of Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #全局变量，记录最长路径的节点个数
        self.Max = 1
        if not root or (not root.left and not root.right): return 0
        self.max_depth(root)
        #减1是因为返回的值是按edge计算的
        return self.Max - 1
    #返回的是该节点的最大深度，按路径中的节点个数算
    def max_depth(self, root):
        if not root:
            return 0
        L = self.max_depth(root.left)
        R = self.max_depth(root.right)
        self.Max = max(self.Max,L+R+1)
        return 1 + max(L,R)

#Or:
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
