'''
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

Example 1:
Given the following tree [3,9,20,null,null,15,7]:
    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

Brute Froce Method: Recursive, O(nlgn)
Runtime: 52 ms, faster than 39.13% of Python online submissions for Balanced Binary Tree.
Memory Usage: 17.3 MB, less than 15.63% of Python online submissions for Balanced Binary Tree.
'''
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        def maxx(node):
            if node is None: return 0
            return 1 + max(maxx(node.left), maxx(node.right))
        #O(n)
        if abs(maxx(root.left) - maxx(root.right)) > 1: return False
        #O(lgn)
        return self.isBalanced(root.left) and self.isBalanced(root.right)

'''
Recursive method with global variable
其实我们在处理完get_height这个高度的时候，我们完全可以在检查每个节点高度并且返回的同时，
记录左右差是否已经超过1，只要有一个节点超过1，那么直接返回False即可，
因此我们只需要在外围设立一个全球变量记录True和False，在调用get_height的时候，内置代码里加入对左右高度的判定即可
O(n)
'''
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.isBalanced = True
        self.getHeight(root)
        return self.isBalanced


    def getHeight(self, root):
        if not root: return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left - right) > 1:
            self.isBalanced = False
        return max(left, right) + 1


'''
Method3: '-1'
O(N)
最后Leetcode上有一种-1的方法，其实就是上面这种方法的一种延伸。
如果左右两边出现了高度差高于1的情况，直接返回-1，这个-1怎么来的？因为高度不可能为负数，-1其实就是一种True/False的表达。
那么在实现上，我们只要对get_height每次返回前做一个判定即可
'''
class Solution(object):
    def isBalanced(self, root):
        height = self.get_height(root)
        return height != -1


    def get_height(self, root):
        if not root: return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if left == -1 or right == -1 : return -1
        if abs(left - right) > 1:  return -1
        return max(left, right) + 1

#Or:
class Solution(object):
    def isBalanced(self, root):

        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1

'''
Iterative, based on postorder traversal:
'''
class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True
