'''
111. Minimum Depth of Binary Tree
Runtime: 20 ms, faster than 99.58% of Python online submissions for Minimum Depth of Binary Tree.
Memory Usage: 15 MB, less than 15.38% of Python online submissions for Minimum Depth of Binary Tree.
'''
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        elif not root.right:
            return 1 + self.minDepth(root.left)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
# Or:(slower by 50%)
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1

# Or: add the smaller one of the child depths - except if that's zero, then add the larger one
def minDepth(self, root):
    if not root: return 0
    d = map(self.minDepth, (root.left, root.right))
    return 1 + (min(d) or max(d))

def minDepth(self, root):
    if not root: return 0
    d, D = sorted(map(self.minDepth, (root.left, root.right)))
    return 1 + (d or D)

'''
Iterative solution using queue(层次遍历)
Runtime: 28 ms, faster than 90.80% of Python online submissions for Minimum Depth of Binary Tree.
Memory Usage: 14.6 MB, less than 82.05% of Python online submissions for Minimum Depth of Binary Tree.
'''

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        queue = [(root, 1)]
        while True:
            curr, val = queue.pop(0)
            if not curr.left and not curr.right:
                return val
            if curr.left:
                queue.append((curr.left, val+1))
            if curr.right:
                queue.append((curr.right, val+1))
