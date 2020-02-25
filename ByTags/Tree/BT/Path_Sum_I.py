'''
112. Path Sum [Easy]

Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.



112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，
这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。
示例:

给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。


[注意]：
1.路径必须从根节点到叶节点
2.有可能有负数，所以不存在当当前和大于22就可以放弃的情况

[Method 1]: 递归
[时间复杂度]：我们访问每个节点一次，时间复杂度为 O(N)，其中 N 是节点个数。
[空间复杂度]：最坏情况下，整棵树是非平衡的，例如每个节点都只有一个孩子，
递归会调用 N 次（树的高度），因此栈的空间开销是 O(N)。
但在最好情况下，树是完全平衡的，高度只有log(N)，因此在这种情况下空间复杂度只有 O(log(N)) 。

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, Sum: int) -> bool:
        if not root: return False
        # 判断是否是叶节点并且是否叶节点满足条件
        if not root.left and not root.right and root.val == Sum:
            return True
        Sum -= root.val
        return self.hasPathSum(root.left, Sum) or self.hasPathSum(root.right, Sum)


'''
[Method 2]: 迭代(前序遍历)
[时间复杂度]：和递归方法相同是 O(N)。
[空间复杂度]：当树不平衡的最坏情况下是 O(N)O(N) 。在最好情况（树是平衡的）下是 O(logN)。

'''
class Solution:
    def hasPathSum(self, root: TreeNode, Sum: int) -> bool:
        if not root: return False
        stack = [(root, Sum)]
        while stack:
            node, curSum = stack.pop()
            if not node.left and not node.right and node.val == curSum:
                return True
            if node.right:
                stack.append((node.right, curSum - node.val))
            if node.left:
                stack.append((node.left, curSum - node.val))
        return False
