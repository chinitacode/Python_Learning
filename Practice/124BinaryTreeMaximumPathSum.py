class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    max_sum = float('-inf')
    def max_gain(node):    
        if node is None:
            return 0
        l = max(max_gain(node.left), 0)
        r = max(max_gain(node.right), 0)            
        price_newpath = node.val + l + r
        nonlocal max_sum
        max_sum = max(max_sum, price_newpath)          
        return node.val + max(l, r)
        
    max_gain(root)
    return max_sum

node1 = TreeNode(9)
node2 = TreeNode(-10)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(7)

node2.left = node1
node2.right = node3
node3.left = node4
node3.right = node5
print(maxPathSum(node2))
