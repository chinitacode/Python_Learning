'''
Divide and Conquer + DFS Method with Helper Function updating a "global" maximum
Time: O(N);  Space: O(log(N)) = height of the binary tree
1.因为一条路径不能返回着走，所以在该节点不为最终确定路径的根节点时，
  左右两个分支只能选一条。
  如：
          10
         /   \
        9     20
             /   \
            15    7
  这种情况，20->15和20->7这两条路只能选其中最大的一条，即20->15，
  因此最大路径为9->10->20->15, 最大路径和为54

2.分治到底部，在返回的时候传入左右任意一边的最大值加上目前node.val:
  node.val + max(l, r)
  但当遇到child节点值为负时，通过与0比较大小来舍弃该节点（设置为0）：
  max(node.val + max(l, r), 0)
  这种情况处理了从Root到左右任意一边的最大值，也就是 root.val + left 或 root.val + right
  如：
           3
         /   \
       -1    -2
  -1节点的返回值为max(-1 + max(0, 0), 0)为0，-2节点同理返回0，因此根节点3返回的值为3。

3.还有一种情况就是当该节点为最终确定路径的根节点时，即当最大值max_sum = node.val + left + right，
  我们在放入global变量的时候与其比较。
    如：
            -10
           /   \
          9     20
               /   \
              15    7
  这种情况最大路径为15->20->7
4.最终返回的是global变量max_sum, 即整个过程中留下来的最大路径和。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

### Use Nonlocal in function ###
def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    max_sum = float('-inf')
    def max_gain(node):
        if node is None:
            return 0
        l = max_gain(node.left)
        r = max_gain(node.right)
        #开辟新路径的权值（即把当前节点作为根节点，左右child都要）
        price_newpath = node.val + l + r
        nonlocal max_sum
        max_sum = max(max_sum, price_newpath)
        #当遇到child节点值为负时，通过与0比较大小来舍弃该节点
        return max(node.val + max(l, r), 0)
    max_gain(root)
    return max_sum

'''
### Use instance attribute in class ###
Runtime: 72 ms, faster than 95.92% of Python online submissions for Binary Tree Maximum Path Sum.
Memory Usage: 24.5 MB, less than 70.00% of Python online submissions for Binary Tree Maximum Path Sum.
'''
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_sum = float('-inf')
        def max_gain(node):
            if node is None:
                return 0
            l = max_gain(node.left)
            r = max_gain(node.right)
            self.max_sum = max(self.max_sum, node.val + l + r)
            #Abandon the child if it's lnegative((set it to zero))
            #Each parent returns its maximum child plus its own value.
            return max(node.val + max(l, r), 0)
        max_gain(root)
        return self.max_sum
