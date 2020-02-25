'''
437. 路径总和 III [简单]
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11

[Method 1]: 迭代（前序遍历）
利用栈对二叉树进行遍历，用一个额外的数组curSums保存当前所有以已遍历节点开头的路径的节点和，
判断每个保存节点和的数组里有多少个和sum相等的数，加到输出结果res即可。
[Time]: O(N*N)
[Space]: O(N*N)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, Sum: int) -> int:
        if not root: return 0
        res = 0
        stack = [(root, [root.val])]
        while stack:
            node, curSums = stack.pop()
            res += curSums.count(Sum)
            curSums += [0]
            if node.right:
                stack.append((node.right, [cur_sum + node.right.val for cur_sum in curSums]))
            if node.left:
                stack.append((node.left, [cur_sum + node.left.val for cur_sum in curSums]))
        return res

'''
[Method 2]：递归


'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, Sum: int) -> int:
        if not root: return 0
        return self.find_path(root, Sum) + \
            self.pathSum(root.left, Sum) + self.pathSum(root.right, Sum) # 左右节点作为起始节点的路径都要判断

    # 判断以当前点为起点往下是否有path，也就是path的数量，返回值应该是0或1
    def find_path(self, node, curSum):
        if node:
            return int(curSum == node.val) + \
                self.find_path(node.left, curSum-node.val) + \
                self.find_path(node.right, curSum-node.val)
        return 0
