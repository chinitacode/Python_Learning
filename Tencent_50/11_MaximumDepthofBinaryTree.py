'''
104. Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes
along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

# Method 1: Recursion
O(n) time and O(h) space h- height of tree if balanced h = logn
Runtime: 24 ms, faster than 94.04% of Python online submissions for Maximum Depth of Binary Tree.
Memory Usage: 14.6 MB, less than 50.62% of Python online submissions for Maximum Depth of Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right) )

# Or 1-liner:
def maxDepth(self, root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

'''
Method 2: BFS + deque/queue
Time: O(n)   Space: O(n)
Runtime: 24 ms, faster than 94.04% of Python online submissions for Maximum Depth of Binary Tree.
Memory Usage: 14.7 MB, less than 23.46% of Python online submissions for Maximum Depth of Binary Tree.
'''
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # use BFS with iteration
        # BFS + deque
        if not root:
            return 0
        queue = collections.deque([(root, 1)]) # here the 2nd number is level
        while queue:
            curr, val = queue.popleft()
            if curr.left:
                queue.append((curr.left, val+1))
            if curr.right:
                queue.append((curr.right, val+1))
        return val
