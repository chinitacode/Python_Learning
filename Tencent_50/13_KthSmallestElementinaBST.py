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
Method 1: Stack + Iteration
Code1:
Using deque, setting its maximum length to k.
# O(n) time, O(k) space
Runtime: 36 ms, faster than 91.60% of Python online submissions for Kth Smallest Element in a BST.
Memory Usage: 19.9 MB, less than 6.52% of Python online submissions for Kth Smallest Element in a BST.
## keep only k elements in stac, if full while appending,
## stack will implement popleft automatically
## the val of the last element in stac is wanted
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
Code2:
Use Stack
O(n) time, O(n) space
Runtime: 32 ms, faster than 97.17% of Python online submissions for Kth Smallest Element in a BST.
Memory Usage: 19.7 MB, less than 39.13% of Python online submissions for Kth Smallest Element in a BST.
'''
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

'''
Method2: DFS recursive, stop early when meet kth

Code1:
'''
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.res = None
        self.dfs_recur(root)
        return self.res
    def dfs_recur(self, node):
        if node is None:
            return
        self.dfs_recur(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.dfs_recur(node.right)
'''
Code2
Runtime: 40 ms, faster than 79.17% of Python online submissions for Kth Smallest Element in a BST.
Memory Usage: 19.7 MB, less than 32.61% of Python online submissions for Kth Smallest Element in a BST.
'''
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = [k]
        self.dfs_recur(root, res)
        return res[1]
    def dfs_recur(self, node, res):
        if len(res) > 1:
            return
        if node.left:
            self.dfs_recur(node.left, res)
        res[0] -= 1
        if res[0] == 0:
            res.append(node.val)
            return
        if node.right:
            self.dfs_recur(node.right, res)

'''
Method3: Generator
Time: O(k), Space: O(1)
Code1
Runtime: 44 ms, faster than 61.80% of Python online submissions for Kth Smallest Element in a BST.
Memory Usage: 19.6 MB, less than 56.52% of Python online submissions for Kth Smallest Element in a BST.
'''
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        for val in self.inorder(root):
            if k == 1:
                return val
            else:
                k -= 1

    def inorder(self, root):
        if root is not None:
            for val in self.inorder(root.left):
                yield val
            yield root.val
            for val in self.inorder(root.right):
                yield val

'''
Code2
Runtime: 44 ms, faster than 61.80% of Python online submissions for Kth Smallest Element in a BST.
Memory Usage: 19.7 MB, less than 41.30% of Python online submissions for Kth Smallest Element in a BST.
'''
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(node):
            if node:
                for val in inorder(node.left):
                    yield val
                yield node.val
                for val in inorder(node.right):
                    yield val
        return next(itertools.islice(inorder(root), k-1, k))



'''
Method4: Binary Search + Recursion
### We only need to traverse all nodes if it's NOT a BST.
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
