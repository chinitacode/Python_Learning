'''
124. Binary Tree Maximum Path Sum [Hard]
Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes
from some starting node to any node in the tree along the parent-child connections.
The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]
       1
      / \
     2   3
Output: 6



Example 2:
Input: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7
Output: 42



Example 3:
Input: [-1,-2,-3]
       1
      / \
     2   3
Output: -1
因为至少需要包含1个节点，所以这里只是舍弃为负的叶节点。


[Method 1]:Divide and Conquer + DFS Method with Helper Function updating a "global" maximum
对于二叉树      a
              / \
             b   c

根据题意，最大路径和可能出现在：
         左子树中:b-a
         右子树中:a-c
         包含根节点与左右子树: b-a-c

我们的思路是递归从bottom向top来return的过程中,记录左子树和右子树中路径更大的那个max(l,r),
并向父节点提供当前节点和子树组成的最大值。

递归设计：
返回值：(root.val) + max(l, r) 即此节点与左右子树最大值之和，较差的解直接被舍弃，不会再被用到。
需要注意的是，若计算的当前支路 l 或 r 的结果 <= 0，意味着对根节点有负贡献，不会在任何情况选这条路（父节点中止），因此返回0剪枝。
递归终止条件：越过叶子节点，返回0；
记录最大值：当前节点最大值 = root.val + l + r。
最终返回所有路径中的全局最大值即可。

[Time]: O(N);
[Space]: O(log(N)) = height of the binary tree
Runtime: 92 ms, faster than 26.42% of Python online submissions for Binary Tree Maximum Path Sum.
Memory Usage: 24.8 MB, less than 67.50% of Python online submissions for Binary Tree Maximum Path Sum.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')
        def max_gain(node):
            if not node: return 0
            l, r = max_gain(node.left), max_gain(node.right)
            # if we take node as the root node of the maximum sum path:
            price_newpath = l + node.val + r
            # update the global variable
            self.max_sum = max(self.max_sum, price_newpath)
            # return the max path sum of including node, if the path sum is negative then give it up
            return max(node.val + max(l,r), 0)
        max_gain(root)
        return self.max_sum
