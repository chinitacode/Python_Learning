'''
617. Merge Two Binary Trees [Easy]
Given two binary trees and imagine that when you put one of them to cover the other,
some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree.
The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of new tree.

给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
否则不为 NULL 的节点将直接作为新二叉树的节点。



Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:

Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the root nodes of both trees.


[Method 1]: Recursion
[Time]: O(m), a total of m nodes need to be traversed.
Here, m represents the minimum number of nodes from the two given trees.
[Space]: O(m). The depth of the recursion tree can go upto m in the case of a skewed tree.
In average case, depth will be O(logm).
Runtime: 88 ms, faster than 67.38% of Python3 online submissions for Merge Two Binary Trees.
Memory Usage: 14.7 MB, less than 5.72% of Python3 online submissions for Merge Two Binary Trees.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2: return t2 or t1
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root

'''
#Or:
[Space]: O(m)
'''
def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees2(t1.left, t2.left)
        t1.right = self.mergeTrees2(t1.right, t2.right)
        return t1

'''
[Method 2]: Iteration + Stack (dfs)
如果两树相应位置都不为None, 则一起入栈。
[Time]: O(m)，worst case为当两树都平衡时，则要traverse一个树的所有节点m；
[Space]: O(m/2)，worst case为当两树都平衡时，stack最多储存left或者right上的节点总数。
Runtime: 92 ms, faster than 39.02% of Python3 online submissions for Merge Two Binary Trees.
Memory Usage: 14.2 MB, less than 20.00% of Python3 online submissions for Merge Two Binary Trees.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 or not t2: return t2 or t1
        stack1, stack2 = [t1], [t2]
        while stack1: #入栈是两个栈一起入
            node1, node2 = stack1.pop(), stack2.pop()
            node1.val += node2.val
            if node1.left and node2.left:
                stack1.append(node1.left)
                stack2.append(node2.left)
            elif node2.left: #若t1左树为空，则把t2左树全部移过来
                node1.left = node2.left
            if node1.right and node2.right:
                stack1.append(node1.right)
                stack2.append(node2.right)
            elif node2.right:
                node1.right = node2.right
        return t1
