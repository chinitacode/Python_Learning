'''
450. Delete Node in a BST

Invert Binary Tree（翻转二叉树）

104.Maximum Depth of Binary Tree（二叉树的最大深度）

Validate Binary Search Tree（验证二叉查找树）[作为可选]

Path Sum（路径总和）


'''

'''
450. Delete Node in a BST
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

1.Recursion:
Runtime: 56 ms, faster than 56.24% of Python online submissions for Delete Node in a BST.
Memory Usage: 19.9 MB, less than 26.67% of Python online submissions for Delete Node in a BST.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                root = root.right
            elif root.right is None:
                root = root.left
            else:
                root.val = self.get_max(root.left)
                root.left = self.deleteNode(root.left, root.val)
        return root
    def get_max(self, root):
        if root is None:
            return None
        while root.right is not None:
            root = root.right
        return root.val

'''
2.Iteration: Code1
Runtime: 52 ms, faster than 80.43% of Python online submissions for Delete Node in a BST.
Memory Usage: 19.8 MB, less than 93.33% of Python online submissions for Delete Node in a BST.
'''
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        node = root
        if not node:
            return None
        if (not node.left and not node.right) and key == node.val:
            return None
        #record the parent node as prev
        prev = node
        while node:
            if key < node.val:
                prev = node
                node = node.left
            elif key > node.val:
                prev = node
                node = node.right
            else:
                if node.left is None:
                    #check in which side node is of its parent node prev
                    if node.val == prev.val:
                        return node.right
                    if node.val > prev.val:
                        prev.right = node.right
                    else:
                        prev.left = node.right
                elif node.right is None:
                    #check in which side node is of its parent node prev
                    if node.val == prev.val:
                        return node.left
                    if node.val > prev.val:
                        prev.right = node.left
                    else:
                        prev.left = node.left
                else:
                    #first find the max value node in its left Tree
                    #replace the val of node with the maxx value
                    #delete the maxx node
                    branch = node.left
                    prev = node
                    while branch.right:
                        prev = branch
                        branch = branch.right
                    maxx = branch.val
                    #check in which side the maxx node(branch) is of the node
                    #the maxx node might have left children
                    if maxx > prev.val:
                        prev.right = branch.left
                    else:
                        prev.left = branch.left
                    node.val = maxx
                return root
        #Perhaps root does not have a node with val equal to key
        return root
'''
2.Iteration: Code1
Runtime: 48 ms, faster than 92.65% of Python online submissions for Delete Node in a BST.
Memory Usage: 19.8 MB, less than 86.67% of Python online submissions for Delete Node in a BST.
先找到要remove的节点(这里还需要它的父节点)，在去移除，根据以下三种情况：
1.no child
2.one child
3.two child
1，就直接利用当前要移除的节点 (cur) 的父节点来移除即可。同时在第一种情况下需要判断是不是root节点就是需要的移除的节点，如果是的话，直接返回None
2，判断当前要移除的节点 (cur) 是父节点的左节点还是右节点来进行移除，同时判断是当前节点是存在左节点还是右节点(在第二种情况里面是只存在其中之一的)，这里面也要判断cur等于root的话就直接返回其中的左节点或右节点，这里可以优化代码为 cur.right or cur.left
3，这里就无须判断当前移除的节点 (cur) 是否是 root节点了，同时利用之前的提示说道需要找到inorder successor，其实就是一直找左节点，直到为空为止。但是这里具体来说就是找到当前这个
cur.right的最左节点 (temp) 以及其上一个节点 (temp_father)如果最后迭代完了，这个temp依旧是cur.right，那么就先交换temp和cur的值，然后让cur.right = temp.right,，如果temp不是cur.right，就说明有temp_father 存在了，得利用temp_father 来进行删除，这里也需要先进行temp和cur节点的值交换，交换之后，temp_father.left不是直接等于None的(去除交换值之后的temp节点)，因为这个temp虽然没有left节点，但是是有right节点的，所以应该令temp_father.left = temp.right。这里代码结构还可以优化一下，因为不管怎么样都要交换temp和cur节点的值，所以在判断temp!=cur.right之前就可以进行交换了，而不是要写两遍交换语句。
'''
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root:
            cur = root
            while 1:
                if cur.val>key:
                    father = cur
                    if cur.left:
                        cur = cur.left
                    else:
                        break
                elif cur.val<key:
                    father = cur
                    if cur.right:
                        cur = cur.right
                    else:
                        break
                else:
                    if not cur.right and not cur.left:
                        if cur==root:
                            return None
                        if cur.val>father.val:
                            father.right = None
                        else:
                            father.left = None
                        # 这里如何remove这个无子节点的node
                        break
                    elif not cur.right or not cur.left:
                        if cur==root:
                            return cur.right if cur.right else cur.left
                        if cur.val>father.val:
                            father.right = cur.right if cur.right else cur.left
                        else:
                            father.left = cur.right if cur.right else cur.left
                        # 这里又如何替换为子节点的呢？嘛呀，怎么这么难啊！
                        break
                    else:
                        # find its inorder_successor or predecessor
                        temp = cur.right
                        while temp.left:
                            temp_father = temp
                            temp = temp.left
                        #这样就找到了用来交换的点，接下来是如何交换呢？
                        if temp!=cur.right:
                            temp.val,cur.val = cur.val,temp.val
                            temp_father.left = temp.right
                        else:
                            temp.val,cur.val = cur.val,temp.val
                            cur.right = temp.right
                        break
            return root
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

'''
110. Balanced Binary Tree
Brute Froce: Recursive, O(nlgn)
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
