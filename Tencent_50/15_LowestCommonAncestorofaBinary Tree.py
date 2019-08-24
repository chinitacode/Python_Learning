'''
236. Lowest Common Ancestor of a Binary Tree[Medium]
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia:
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T
that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

                   3
                /     \
              /         \
             5           1
           /   \        /  \
          6     2      0    8
              /   \
             7     4


Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5,
since a node can be a descendant of itself according to the LCA definition.

Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

*** Watch out: ***
Note that the problem description said that " two given nodes in the tree."
So the parameters p and q are node references in the tree.
Use ''if (root == p) instead of if(root.val == p.val)''
与题235求二叉搜索树的LCR不同，这道题的题设是普通的二叉树，
因此找一个node时（先找root）如果左边找不到，则还需往右边找。

#Method1: Recursion: Divide and Conquer + DFS（Preorder Traversal）
Time:O(n)   Space:O(n)
Runtime: 64 ms, faster than 75.63% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 24 MB, less than 82.35% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
[分析]
    1.最低公共祖先的定义是，在一个二叉树中，我们能找到的最靠近叶子的节点，该节点同时是p和q的祖先节点。
    注意，如果p或者q本身也可以作为自己的祖先。

    2.这个题里面lowestCommonAncestor(root, p, q)函数的作用是判断p和q在root树中最低的公共祖先是什么，返回值是公共祖先。
    如果当前节点等于其中的p和q某一个节点，那么找到了节点（即找到了其中一个），返回该节点，否则在左右子树分别寻找。

    3.左右子树两个返回的是什么呢？按照该递归函数的定义，即找到了左子树和右子树里p和q的公共祖先，注意祖先可以是节点自己。
    然后根据左右侧找到的节点做进一步的判断。

    4.left返回的是左子树里找到的p、q的公共祖先（即p和q中的其中一个节点）
    因为p或者q本身也可以作为自己的祖先，找到了则返回自己。
    right返回值同理。

    5.如果left and right，则p和q必定分别分部在左右子树，不然必有一个子树为空！

    6.如果left and right，说明分别找到了p和q，那么LCA就是当前节点。
    否则就在不为空的那个结果就是所求。
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None: return None
        # If looking for me, return myself: 分治到底部的base case：
        #只要p或q之一在root里存在，就返回root(因题意'p and q are different and both values will exist in the binary tree.')
        if root == p or root == q:
            return root

        left =  self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right: return root
        if left: return left
        if right: return right
