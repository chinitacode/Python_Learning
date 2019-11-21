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
