'''
226. Invert Binary Tree [Easy]
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew),
but you can’t invert a binary tree on a whiteboard so f*** off.


[Method 1]: Recursion
反转一颗空树结果还是一颗空树。
对于一颗根为 root ，左子树为 left， 右子树为 right 的树来说，
它的反转树是一颗根为 root，左子树为 right 的反转树，右子树为 left 的反转树的树。
[Time]: O(n), 既然树中的每个节点都只被访问一次，其中 n 是树中节点的个数。
在反转之前，不论怎样我们至少都得访问每个节点至少一次，因此这个问题无法做地比 O(n) 更好了。
[Space]: 在最坏情况下栈内需要存放 O(h) 个方法调用，其中 h 是树的高度。
Runtime: 16 ms, faster than 73.91% of Python online submissions for Invert Binary Tree.
Memory Usage: 12 MB, less than 7.50% of Python online submissions for Invert Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root or (not root.left and not root.right): return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


'''
#Or:
Runtime: 20 ms, faster than 41.08% of Python online submissions for Invert Binary Tree.
Memory Usage: 11.8 MB, less than 37.50% of Python online submissions for Invert Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


'''
[Method 2]: Iteration + stack
我们需要交换树中所有节点的左孩子和右孩子。
因此可以创一个栈来存储所有左孩子和右孩子还没有被交换过的节点。
开始的时候，只有根节点在这个栈里面。
只要这个队列不空，就一直从栈中出队节点，然后互换这个节点的左右孩子节点，
接着再把孩子节点入栈，对于其中的空节点不需要加入栈。
最终栈一定会空，这时候所有节点的孩子节点都被互换过了，直接返回最初的根节点就可以了。
E.g.
     4                 4               4
   /   \             /   \           /   \
  2     7      =>   7     2     =>  7     2
 / \   / \         / \   / \       / \   / \
1   3 6   9       6   9 1   3     9   6 3   1

[Time]: O(n), 既然树中的每个节点都只被访问一次，其中 n 是树中节点的个数。
[Space]: O(n)， 即使在最坏的情况下，也就是队列里包含了树中所有的节点。
对于一棵完整二叉树来说，叶子节点那一层拥有⌈n/2] = O(n) 个节点。
Runtime: 16 ms, faster than 73.91% of Python online submissions for Invert Binary Tree.
Memory Usage: 11.9 MB, less than 7.50% of Python online submissions for Invert Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root
