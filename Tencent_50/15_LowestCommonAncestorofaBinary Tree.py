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

***   ***  ***  *** Watch out: ***  ***  ***  ***  ***
Note that the problem description said that " two given nodes in the tree."
So the parameters p and q are node references in the tree.
Use ''if (root == p) instead of if(root.val == p.val)''
与题235求二叉搜索树的LCR不同，这道题的题设是普通的二叉树，
因此找一个node时（先找root）如果左边找不到，则还需往右边找。
***  ***  ***  ***  ***  ***  ***  ***  ***  ***  ***

--------------------
Recursion solutionn: Divide and Conquer + DFS（Preorder Traversal）
--------------------
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

'''
--------------------
Iterative solution: stack + dictionary + helper method
--------------------
use stack to traverse(pre-order) and dictionary to store the parent node of
each node(until target node found) in the helper method

[Time] _dfs: 先序遍历找节点：O(n)  +  输出包含节点到root的路径O(h) ==> O(n)
[Space] O(n)的字典，O(h)的stack ==> O(n)
lowestCommonAncestor: 2个dfs + 1个while loop：2*(O() + O(h)) + O(h) ==> O(n)

Runtime: 64 ms, faster than 75.64% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 20.2 MB, less than 86.27% of Python online submissions for Lowest Common Ancestor of a Binary Tree.

[注意]
1.p、q必定存在于root并且不等
2.以下code还可以优化，因为在找p和q的时候各自递归了一次，若p和q同在一边，就重复做功了
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        #此时p和q全部为从目标节点的root的路径list
        p = self._dfs(root, p)
        q = self._dfs(root, q)
        answer = root
        #通过循环去掉p和q里重复的节点，p最后一个去重的节点就是所求的LCA
        #O(h)
        while p and q and p[-1] is q.pop():
            answer = p.pop()
        return answer

    #先序遍历找节点：O(n)  +  输出包含节点到root的路径O(h) ==> O(n)
    def _dfs(self, root, n):
        #初始化空字典，因为root无parent
        parents = dict()
        #用stack做后序遍历
        stack = [root]
        while stack:
            #先判断root是否为该节点，再把其左右子树压入栈等待检查
            node = stack.pop()
            if node is None:
                continue
            #找到了该节点就break，这时在它之上的node的parent都已经加入了字典
            if node is n:
                break
            #先压右子树入栈，因为pop时后出（先进后出）
            stack.append(node.right)
            #后压左子树入栈（LIFO）
            stack.append(node.left)
            #把才压入栈的节点的parent全部加入字典（哈希表）
            parents[node.left] = node
            parents[node.right] = node
        #初始化时answer[-1]都为目标节点
        answer = [n]
        #把从该节点到root整条路径上的节点从bottom到up地加入answer
        while answer[-1] != root:
            answer.append(parents[answer[-1]])
        return answer

'''
-----------
优化版代码：
-----------
先把p和q的parent加入字典，再用一个list来存储p的路径节点，判断q节点是否在p路径中，
通过循环让q往上（parent）更新，最终相交的节点就是所求的LCA。
[Time] O(n)    [Space]O(n)

Runtime: 52 ms, faster than 98.72% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 19.4 MB, less than 100.00% of Python online submissions for Lowest Common Ancestor of a Binary Tree.
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        parent = {root: None}
        # O(n)
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
        ancestors = []
        # O(h)
        while p:
            ancestors.append(p)
            p = parent[p]
        # O(h)
        while q not in ancestors:
            q = parent[q]
        return q
