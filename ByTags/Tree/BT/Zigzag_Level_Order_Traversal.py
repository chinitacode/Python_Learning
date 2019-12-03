'''
103. Binary Tree Zigzag Level Order Traversal [Medium]

Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

[Method 1]:
还是按照BFS层次遍历从左到右地遍历每一层的节点，只不过是偶数层的(把根节点记作第一层)时，
逆序地把节点加入到表示该层的list里面（可以通过insert(0,val)）。
因为输出时每层都会改变方向，所以我们只需要维持一个odd标志来判断奇偶，通过与(-1)相乘来看是否是偶数层。
[Time]: O(n), n为所有节点
[Space]: O(n)
Runtime: 16 ms, faster than 87.45% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
Memory Usage: 12.2 MB, less than 14.28% of Python online submissions for Binary Tree Zigzag Level Order Traversal.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return
        level = [root]
        res = []
        odd = 1
        while level:
            nxt_level = []
            nodes = []
            for node in level:
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)
                # if level number is odd
                if odd > 0:
                    nodes.append(node.val)
                else:
                    nodes.insert(0,node.val)
            level = nxt_level
            res.append(nodes)
            odd *= (-1)
        return res
