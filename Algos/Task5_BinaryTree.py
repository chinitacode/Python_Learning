'''
---------------------------------------------------------------------
【二叉树】
1.实现一个二叉查找树，并且支持插入、删除、查找操作
2.实现查找二叉查找树中某个节点的后继、前驱节点
3.实现二叉树前、中、后序以及按层遍历
4.并完成leetcode上的验证二叉搜索树(98)及二叉树层次遍历(102,107)！（选做）（保留往期第四天任务）
---------------------------------------------------------------------
'''
#1.
class Node:
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    def __init__(self, root = None):
        self.root = root

    # Get methods (pre-order traversal)
    # Time: Average: O(log(n+1)) = height(如果是个完整的二叉树)
    #       Worst: O(n)(若只是单边二叉树)
    '''
    ### Recursive Method ###
    def get(self, key):
        return self._get(self.root, key)
    # helper
    def _get(self, node, key):
        if node is None:
            return None
        if key == node.item:
            return node.item
        if key < node.item:
            return self._get(node.left, key)
        else:
            return self._get(node.right, key)
    '''
    ### Iterative Method ###
    def get(self, key):
        node = self.root
        while node is not None:
            if key == node.item:
                return node.item
            if key < node.item:
                node = node.left
            else:
                node = node.right
        return None
    '''
    ### Recursive Method ###
    def add(self, key):
        self.root = self._add(self.root, key)

    def _add(self, node, key):
        if node is None:
            return Node(key)
        if key == node.item:
            return
        if key < node.item:
            #需要把新加的Node给连接起来
            node.left = self._add(node.left, key)
        else:
            node.right = self._add(node.right, key)
        #如果不return，则_add()会返回None，导致self.root = None
        return node
    '''
    ### Iterative Method ###
    def add(self, key):
        node = self.root
        #while node is not leaf:
        while node.left or node.right is not None:
            if key == node.item:
                return
            if key < node.item:
                node = node.left
            else:
                node = node.right
        if key < node.item:
            node.left = Node(key)
        else:
            node.right = Node(key)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if node is None:
            return
        if key < node.item:
            node.left = self._remove(node.left, key)
        elif key > node.item:
            node.right = self._remove(node.right, key)
        else:
            if node.right is None:
                node = node.left
            elif node.left is None:
                node = node.right
            else:
                node.item = self._get_max(node.left)
                node.left = self._remove(node.left, node.item)
        return node

    def get_max(self):
        return self._get_max(self.root)

    def _get_max(self, node):
        if node is None:
            return None
        while node.right:
            node = node.right
        return node.item

    def get_min(self):
        return self._get_min(self.root)

    def _get_min(self, node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.item

    # Traversal Methods
    def print_inorder(self):
        self._print_inorder(self._root)
        print('')

    def _print_inorder(self, node):
        if (node is None):
            return
        self._print_inorder(node._left)
        print ('[', node._item, ']', end = " ")
        self._print_inorder(node._right)

    def print_preorder(self):
        self._print_preorder(self._root)
        print('')

    def _print_preorder(self, node):
        if (node is None):
            return
        print ('[', node._item, ']', end = " ")
        self._print_preorder(node._left)
        self._print_preorder(node._right)

    def print_postorder(self):
        self._print_postorder(self._root)
        print('')

    def _print_postorder(self, node):
        if (node is None):
            return
        self._print_postorder(node._left)
        self._print_postorder(node._right)
        print ('[', node._item, ']', end = " ")


'''
###### 2.遍历 ######
--------------------------------------------------------------------
### 前/先序遍历（pre-order traversal）:
    先（打印）parent,再（打印）child
    根结点 ---> 左子树 ---> 右子树

                   1
                /     \
              /         \
             2           7
           /   \        /  \
          3     4      8    9
              /   \
             5     6

        Algorithm preOrder(v): #v--vertex,节点
            visit(v)
            for each child w of v:
                preOrder(w)

---------------------------------------------------------------------
### 后序遍历（post-order traversal）:
    先（打印）child,再（打印）parent
    左子树 ---> 右子树 ---> 根结点

                   9
                /     \
              /         \
             5           8
           /   \        /  \
          1     4      6    7
              /   \
             2     3

Algorithm postOrder(v):
    for each child w of v:
        postOrder(w)
    visit(v)
---------------------------------------------------------------------
### 中序遍历/顺序遍历(in-order traversal)
    左子树---> 根结点 ---> 右子树
    *在二叉树的顺序遍历中，常常会发生先遇到的节点到后面再访问的情况，
    这和先进后出的栈的结构很相似，因此在非递归的实现方法中，我们最常使用的数据结构就是栈。

                   6
                /     \
              /         \
             2           8
           /   \        /  \
          1     4      7    9
              /   \
             3     5

Algorithm inOrder(v):
    if hasLeft(v):
        inOrder(left(v))
    visit(v)
    if hasRight(v):
        inOrder(right(v))
---------------------------------------------------------------------
### 层次遍历


---------------------------------------------------------------------



'''


'''
98. Validate Binary Search Tree

> 类型：DFS遍历
> Time Complexity O(n)
> Space Complexity O(h)

错误代码(Buggy Code)：
class Solution(object):
    def isValidBST(self, root):
        return self.helper(root)

    def helper(self, node):
        if not node: return True
        if node.left and node.left.val >= node.val:
            return False
        if node.right and node.right.val <= node.val:
            return False
        left = self.helper(node.left)
        right = self.helper(node.right)
        return left and right
上面代码看起来好像也没什么毛病，但以下这种情况是过不了的

    5
   / \
  1   4
     / \
    3   6
为什么？因为我们每层在当前的root分别做了两件事情：

检查root.left.val是否比当前root.val小
检查root.right.val是否比当前root.val大
大家可以用这个思路过一下上面这个例子，完全没问题。
那么问题来了，Binary Search Tree还有一个定义，就是

左边所有的孩子的大小一定要比root.val小
右边所有的孩子的大小一定要比root.val大
我们错就错在底层的3，比顶层的5，要小。

ok，概念弄懂了，如何解决这个问题呢？我们可以从顶层开始传递一个区间，举个例子。
在顶层5，向下传递的时候，
他向告诉左边一个信息：
左孩子，你和你的孩子，和你孩子的孩子，孩子的...........孩子都不能比我大哟
他向告诉右边一个信息：
右孩子，你和你的孩子，和你孩子的孩子，孩子的...........孩子都不能比我小哟

所以5告诉左边1的信息/区间是：(-infinite, 5)
所以5告诉右边4的信息/区间是：(5 , infinite)

然后我们要做的就是把这些信息带入到我们的代码里，我们把区间的左边取名lower_bound, 右边取名upper_bound
这样才有了LC被复制到烂的标准答案

class Solution(object):
    def isValidBST(self, root):
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, node, lower_bound, upper_bound):
        if not node: return True
        if node.val >= upper_bound or node.val <= lower_bound:
            return False
        left = self.helper(node.left, lower_bound, node.val)
        right = self.helper(node.right, node.val, upper_bound)
        return left and right

或者更直观的写法：

def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
    if not root:
        return True
    if root.val <= floor or root.val >= ceiling:
        return False
    # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
    return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)


这题呢，还有另外一个根据BST性质进行Inorder操作的答案

暴力解法：

利用数组储存inorder过的数，如果出现重复，或者数组不等于sorted(arr)，证明不是Valid Tree
这个解法比较易读，如果对Space Complexity要求不严格，可以通过比对数组里面的数而不是sorted(arr)来达到O(N)时间复杂。

class Solution(object):
    def isValidBST(self, root):
        self.arr = []
        self.inorder(root)
        return self.arr == sorted(self.arr) and len(self.arr) == len(set(self.arr))

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)

    #
    def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
    if not root:
        return True
    if root.val <= floor or root.val >= ceiling:
        return False
    # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
    return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)
O(1) Space解法：

在上面的算法里进行了优化，每次只需要将当前root.val和上次储存的self.last比对即可知道是否满足条件。然后设立self.flag用于返回。

class Solution(object):
    def isValidBST(self, root):
        self.last = -float('inf')
        self.flag = True
        self.inorder(root)
        return self.flag

    def inorder(self, root):
        if not root: return
        self.inorder(root.left)
        if self.last >= root.val:
            self.flag = False
        self.last = root.val
        self.inorder(root.right)
'''

'''
100. Same Tree
> 类型：DFSF分制
> Time Complexity O(N)
> Space Complexity O(h)

Runtime: 32 ms, faster than 92.27% of Python3 online submissions for Same Tree.
Memory Usage: 13.9 MB, less than 5.72% of Python3 online submissions for Same Tree.

'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
#Or:
def isSameTree(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #Return True only if p and q are both None else return False(because it's reference comparison)
    return p is q

# DFS with stack
def isSameTree2(self, p, q):
    stack = [(p, q)]
    while stack:
        node1, node2 = stack.pop()
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
    return True

# BFS with queue
def isSameTree3(self, p, q):
    queue = [(p, q)]
    while queue:
        node1, node2 = queue.pop(0)
        if not node1 and not node2:
            continue
        elif None in [node1, node2]:
            return False
        else:
            if node1.val != node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
    return True


'''
101. Symmetric Tree
Method1: Preorder + Recursion
这道题具体的Recursion Rule不是传递Root本身，而是对两个子孩子的比较，所以Helper的参数定义为root.left 和 root.right.
然后根据题目的特性，在每一层往下传递之前要做比较，所以是preorder的写法，先写比较的几种格式，然后在做递归。递归向上返回的参数是一个Boolean。
时间复杂度 : O(N) 空间复杂度 : O(N) or O(Height)

Runtime: 36 ms, faster than 92.57% of Python3 online submissions for Symmetric Tree.
Memory Usage: 13.9 MB, less than 5.17% of Python3 online submissions for Symmetric Tree.
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            outpair = self.is_mirror(p.left, q.right)
            inpair = self.is_mirror(p.right, q.left)
            return outpair and inpair
        return False
#or:
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(L,R):
            if not L and not R: return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False
        if root is None:
            return True
        return isSym(root.left, root.right)
'''
Method2: Preorder + Iteration using Stack(slow)
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False

'''
Method3: Level-order + stack
'''
def isSymmetric(self, root):
    last = [root]
    while True:
        if not any(last):
            return True
        current = []
        for node in last:
            if node is not None:
                current.append(node.left)
                current.append(node.right)
        if not self.is_list_symmetric(current):
            return False
        else:
            last = current

def is_list_symmetric(self, lst):
    head, tail = 0, len(lst) - 1
    while head < tail:
        h, t = lst[head], lst[tail]
        head += 1
        tail -= 1
        if h == t == None:
            continue
        if None in (h, t) or h.val != t.val:
            return False
    return True
        return True
