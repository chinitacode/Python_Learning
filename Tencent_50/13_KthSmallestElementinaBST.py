'''
230. Kth Smallest Element in a BST [Medium]
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
Note: You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3

二叉查找树（Binary Search Tree），也称为二叉搜索树、有序二叉树（ordered binary tree）
或排序二叉树（sorted binary tree），是指一棵空树或者具有下列性质的二叉树：

1.若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
2.若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
3.任意节点的左、右子树也分别为二叉查找树；
4.没有键值相等的节点。
'''

'''
Method 1: Using a deque, setting its maximum length to k.
O(n) time, O(k) space
# keep only k elements in stac, if full while appending,
# stack will implement popleft automatically
# the val of the last element in stac is wanted
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        import collections
        stac = collections.deque(maxlen=k)
        while True:
            while root:
                stac.append(root)
                root = root.left
            root = stac.pop()
            if k == 1:
                return root.val
            k -= 1
            root = root.right

'''
### We only need to traverse all nodes if it's NOT a BST.
Recursion
Runtime: 52 ms, faster than 27.51% of Python online submissions for Kth Smallest Element in a BST.
Memory Usage: 19.8 MB, less than 6.52% of Python online submissions for Kth Smallest Element in a BST.
'''
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def sort_tree(root):
            if root:
                left = sort_tree(root.left)
                right = sort_tree(root.right)
                return left + [root.val] + right
            return []
        sorted_tree = sort_tree(root)
        return sorted_tree[k - 1]
