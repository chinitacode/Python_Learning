'''
98. Validate Binary Search Tree [Medium]

Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

[Method 1]:
> 类型：DFS遍历
> Time Complexity O(n)
> Space Complexity O(h)

错误代码(Buggy Code)：
'''
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if root.left:
            if root.left.val >= root.val or not self.isValidBST(root.left):
                return False
        if root.right:
            if root.right.val <= root.val or not self.isValidBST(root.right):
                return False
        return True

'''
上面代码看起来好像也没什么毛病，但以下这种情况是过不了的

    5
   / \
  1   4
     / \
    3   6
为什么？因为我们每层在当前的root分别做了两件事情：

检查root.left.val是否比当前root.val小并且root.left是不是BST;
检查root.right.val是否比当前root.val大并且root.right是不是BST
大家可以用这个思路过一下上面这个例子，完全没问题。
那么问题来了，Binary Search Tree还有一个定义，就是

左边所有的孩子的大小一定要比root.val小
右边所有的孩子的大小一定要比root.val大
我们错就错在底层的3，比顶层的5，要小。

ok，概念弄懂了，如何解决这个问题呢？我们可以从顶层开始传递一个区间，举个例子。
在顶层5，向下传递的时候，
他向告诉左边一个信息：
左孩子，你和你的孩子，和你孩子的孩子，孩子的...........孩子都不能比我大哟
他向告诉右边一个信息：
右孩子，你和你的孩子，和你孩子的孩子，孩子的...........孩子都不能比我小哟

所以5告诉左边1的信息/区间是：(-infinite, 5)
所以5告诉右边4的信息/区间是：(5 , infinite)

然后我们要做的就是把这些信息带入到我们的代码里，我们把区间的左边取名lower_bound, 右边取名upper_bound
这样才有了LC被复制到烂的标准答案:

'''
class Solution(object):
    def isValidBST(self, root):
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, node, lower_bound, upper_bound):
        if not node: return True
        if node.val >= upper_bound or node.val <= lower_bound:
            return False
        left = self.helper(node.left, lower_bound, node.val)
        right = self.helper(node.right, node.val, upper_bound)
        return left and right

#或者更直观的写法：

def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
    if not root:
        return True
    if root.val <= floor or root.val >= ceiling:
        return False
    # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
    return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)


'''
[Method 2]:根据BST性质进行Inorder操作的暴力解法
利用数组储存inorder过的数，如果出现重复，或者数组不等于sorted(arr)，证明不是Valid Tree
这个解法比较易读，如果对Space Complexity要求不严格，可以通过比对数组里面的数而不是sorted(arr)来达到O(N)时间复杂。
'''
class Solution(object):
    def isValidBST(self, root):
        self.arr = []
        self.inorder(root)
        return self.arr == sorted(self.arr) and len(self.arr) == len(set(self.arr))

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)


'''
O(1) Space解法：
在上面的算法里进行了优化，每次只需要将当前root.val和上次储存的self.last比对即可知道是否满足条件。
然后设立self.flag用于返回。
'''
class Solution(object):
    def isValidBST(self, root):
        self.last = -float('inf')
        self.flag = True
        self.inorder(root)
        return self.flag

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        if self.last >= root.val:
            self.flag = False
        self.last = root.val
        self.inorder(root.right)
