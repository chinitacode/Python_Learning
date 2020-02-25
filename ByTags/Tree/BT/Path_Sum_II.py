'''
113. 路径总和 II [中等]

给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

[Method 1]: 迭代（前序遍历）
[时间复杂度]：和递归方法相同是 O(N)。
[空间复杂度]：当树不平衡的最坏情况下是 O(N*N)。在最好情况（树是平衡的）下是 O(logN)。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, Sum: int) -> List[List[int]]:
        if not root: return []
        res, tmp = [], [root.val]
        stack = [(root, Sum-root.val, tmp)]  # 把路径也加入stack，这样不同路径间就不会影响了
        while stack:
            node, curSum, tmp = stack.pop()
            if not node.left and not node.right:
                if curSum == 0:
                    res.append(tmp[:])
            if node.right:
                stack.append((node.right, curSum-node.right.val, tmp+[node.right.val]))
            if node.left:
                stack.append((node.left, curSum-node.left.val, tmp+[node.left.val]))
        return res

'''
[Method 2]: 递归+dfs
注意： 深度优先搜索不需要手动回溯，
因为我们这里仍然是必须从根节点到叶节点，而且有可能有负数节点存在，所以也不需要剪枝。
'''
class Solution:
    def pathSum(self, root: TreeNode, Sum: int) -> List[List[int]]:
        if not root: return []
        res, tmp = [], []
        def dfs(node, tmp, curSum):
            if not node.left and not node.right and curSum == 0:
                res.append(tmp)
            if node.left:
                dfs(node.left, tmp + [node.left.val], curSum-node.left.val)
            if node.right:
                dfs(node.right, tmp + [node.right.val], curSum-node.right.val)
        dfs(root, tmp+[root.val], Sum-root.val)
        return res
