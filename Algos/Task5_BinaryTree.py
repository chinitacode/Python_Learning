'''
---------------------------------------------------------------------
【二叉树】
1.实现一个二叉查找树，并且支持插入、删除、查找操作
2.实现查找二叉查找树中某个节点的后继、前驱节点
3.实现二叉树前、中、后序以及层次遍历
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
--------------------------------------------------------------------
###### 2.遍历 ######
--------------------------------------------------------------------
1. 前/先序遍历（pre-order traversal）:
---------------------------------------------------------------------
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

Output: [1,2,3,5,4,6,7,8,9]

        Algorithm preOrder(v): #v--vertex,节点
            visit(v)
            for each child w of v:
                preOrder(w)

--------------------
---Recursive code---
--------------------
'''
def preOrder(self, root):
    if root == None:
        return
    print root.val
    self.preOrder(root.left)
    self.preOrder(root.right)

'''
--------------------
---Iterative code---
--------------------
preOrder每次都将遇到的节点压入栈，当左子树遍历完毕后才从栈中弹出最后一个访问的节点(后进先出，但是不影响先打印root)，
访问其右子树。
在同一层中，不可能同时有两个节点压入栈，因此栈的大小空间为O(h)，h为二叉树高度。
时间方面，每个节点都被压入栈一次，弹出栈一次，访问一次，复杂度为O(n)。
'''
def preOrder(self, root):
    if root == None:
        return
    myStack = []
    node = root
    while node or myStack:
        while node:
            # 从根节点开始，一直找它的左子树
            print node.val
            # 把node压入栈只是为了当左边为空时回到右子树
            myStack.append(node)
            # 继续遍历左子树，直到node为空跳出当前循环
            node = node.left
        # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = myStack.pop()
        # 开始查看它的右子树，若为空，则继续pop栈，接着遍历右子树
        node = node.right

'''
144. Binary Tree Preorder Traversal
DFS Stack Iteration
Runtime: 20 ms, faster than 41.38% of Python online submissions for Binary Tree Preorder Traversal.
Memory Usage: 11.7 MB, less than 68.57% of Python online submissions for Binary Tree Preorder Traversal.
'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        node = root
        myStack = []
        res = []
        while node or myStack:
            while node:
                res.append(node.val)
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            node = node.right
        return res
'''
Optimized iteration with stack:

初始化时先把root加入栈，pop出来处理其val，然后加右子树（后出）入栈，再加左子树（先出）入栈。
当node为None（即左子树为空），才会pop右子树。

> Time Complexity O(n)
> Space Complexity O(h)
Runtime: 8 ms, faster than 99.07% of Python online submissions for Binary Tree Preorder Traversal.
Memory Usage: 11.8 MB, less than 22.86% of Python online submissions for Binary Tree Preorder Traversal.
'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = [root] #因为一开始就要输出根节点，所以可以先放入stack等着pop用
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                #先加右子树，后出
                stack.append(node.right)
                #后加左子树，先出
                stack.append(node.left)
        return res

'''
DFS Recursion using helper and global attribute
> Time Complexity O(n)
Runtime: 12 ms, faster than 93.43% of Python online submissions for Binary Tree Preorder Traversal.
Memory Usage: 11.6 MB, less than 94.29% of Python online submissions for Binary Tree Preorder Traversal.
'''
class Solution(object):
    def preorderTraversal(self, root):
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return
        self.res.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)
'''
Recursion
Runtime: 20 ms, faster than 41.38% of Python online submissions for Binary Tree Preorder Traversal.
Memory Usage: 11.9 MB, less than 11.43% of Python online submissions for Binary Tree Preorder Traversal.
'''
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

'''
---------------------------------------------------------------------
2.### 中序遍历/顺序遍历(in-order traversal)
---------------------------------------------------------------------
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

--------------------
---Recursive code---
--------------------
'''
def inOrder(self, root):
    if root == None:
        return
    self.inOrder(root.left)
    print root.val
    self.inOrder(root.right)

'''
--------------------
---Iterative code---
--------------------
'''
def inOrder(self, root):
    if root == None:
        return
    myStack = []
    node = root
    while node or myStack:
        while node:
            # 从根节点开始，一直找它的左子树
            myStack.append(node)
            node = node.left
        # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = myStack.pop()
        print node.val
        # 开始查看它的右子树
        node = node.right
'''
94. Binary Tree Inorder Traversal
Recursion: DFS + Helper
Runtime: 20 ms, faster than 40.34% of Python online submissions for Binary Tree Inorder Traversal.
Memory Usage: 11.9 MB, less than 20.00% of Python online submissions for Binary Tree Inorder Traversal.
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node is None: return None
        self.dfs(node.left)
        self.res.append(node.val)
        self.dfs(node.right)

'''
Iteration： DFS + Stack
先把迭代到最左边的叶子节点，把所有途中的root放进stack，当左边走不通了，开始往res里面存数，并往右边走。
Runtime: 12 ms, faster than 92.85% of Python online submissions for Binary Tree Inorder Traversal.
Memory Usage: 11.9 MB, less than 10.00% of Python online submissions for Binary Tree Inorder Traversal.
'''
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        node = root
        res = []
        myStack = [] #因为顶点root需要保留到中间才用，所以一开始不能直接放入stack
        #先从top到bottom把最底部的左子树加入栈，
        #再pop出来处理其值（append到res），再加右子树
        while myStack or node:
            while node:
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            res.append(node.val)
            node = node.right
        return res

'''
---------------------------------------------------------------------
3.### 后序遍历（post-order traversal）:
---------------------------------------------------------------------
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

Output: [1,2,3,4,5,6,7,8,9]


                   1
                /     \
              /         \
             2           4
               \        /  \
                3      5    6
                  \
                   7

Input:  [1,2,4,null,3,5,6,null,7]
Output: [7,3,2,5,6,4,1]

[Pseudo-code]
Algorithm postOrder(v):
    for each child w of v:
        postOrder(w)
    visit(v)

--------------------
---Recursive code---
--------------------
'''
def postOrder(self, root):
    if root == None:
        return
    self.postOrder(root.left)
    self.postOrder(root.right)
    print root.val

'''
--------------------
---Iterative code---
--------------------
从直觉上来说，后序遍历对比中序遍历难度要增大很多。因为中序遍历节点序列有一点的连续性，而后续遍历则感觉有一定的跳跃性。
先左，再右，最后才中间节点；访问左子树后，需要跳转到右子树，右子树访问完毕了再回溯至根节点并访问之
'''
def postorder(self, root):
    if root == None:
        return
    myStack1 = []
    myStack2 = []
    node = root
    myStack1.append(node)
    while myStack1:
    # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
        node = myStack1.pop()
        if node.left:
            myStack1.append(node.left)
        if node.right:
            myStack1.append(node.right)
        myStack2.append(node)
    while myStack2:
    # 将myStack2中的元素出栈，即为后序遍历次序
        print myStack2.pop().val

'''
145. Binary Tree Postorder Traversal [Hard]
Recursive solution: DFS + Helper
Runtime: 8 ms, faster than 99.21% of Python online submissions for Binary Tree Postorder Traversal.
Memory Usage: 11.8 MB, less than 25.00% of Python online submissions for Binary Tree Postorder Traversal.
'''
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if node is None: return None
        self.dfs(node.left)
        self.dfs(node.right)
        self.res.append(node.val)

'''
Iteration:
Method1: 2 stacks
Runtime: 12 ms, faster than 93.40% of Python online submissions for Binary Tree Postorder Traversal.
Memory Usage: 11.7 MB, less than 87.50% of Python online submissions for Binary Tree Postorder Traversal.
'''
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None: return []
        myStack1 = [root]
        myStack2 = []
        res = []
        node = root
        while myStack1:
            node = myStack1.pop()
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            myStack2.append(node)
        while myStack2:
            res.append(myStack2.pop().val)
        return res

'''
[Method 2]: 1 stack (the same as method1)
Use only one stack to store the preorder traversal,
but reverse the return list to post-order traversal in the end.
其实就是用stack来前序遍历（parent-->left child-->right child）每个节点,
每pop出一个节点，就把左、右子树节点再压入栈，
把该节点的值加入输出数列中。
所以输出数列其实保存了后序遍历的逆序，因为节点进入的顺序是按照：
parent --> right tree（子树按照同样地规律进入）--> left tree。

[Time]: O(N)
[Space]: O(h)
Runtime: 12 ms, faster than 93.36% of Python online submissions for Binary Tree Postorder Traversal.
Memory Usage: 11.7 MB, less than 83.33% of Python online submissions for Binary Tree Postorder Traversal.
'''
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]

'''
---------------------------------------------------------------------
4.### 层次遍历 (Level-order Traversal):
---------------------------------------------------------------------


---------------------------------------------------------------------
102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

[Method 1]: Using 2 stacks
按层更新名为level的stack，
对每一层的节点，先把节点的val加进这一层的list里面，
再把其左右节点加进next_level的stack里，
当把这一层的节点都遍历完时就用next_level来更新level，
直到level为空。
Runtime: 24 ms, faster than 51.43% of Python online submissions for Binary Tree Level Order Traversal.
Memory Usage: 12.3 MB, less than 48.53% of Python online submissions for Binary Tree Level Order Traversal.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        res = []
        level = []
        level.append(root)
        while level:
            nodes = []
            next_level = []
            for node in level:
                nodes.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(nodes)
            level = next_level
        return res

'''
[Method 2]：BFS + queue
queue的概念用deque来实现，popleft() 时间复杂为O(1)即可
外围的While用来定义BFS的终止条件，所以我们最开始initialize queue的时候可以直接把root放进去
在每层的时候，通过一个cur_level记录当前层的node.val，
size用来记录queue的在增加子孙node之前大小，因为之后我们会实时更新queue的大小。
当每次从queue中pop出来的节点，把它的左右子节点放进Queue以后，记得把节点本身的的value放进cur_level。
for loop终止后，就可以把记录好的整层的数值，放入我们的return数组里。
[Time]: O(N)
[Space]: O(size of return array + size of queue) -> Worst Case O(2N)
Runtime: 24 ms, faster than 51.43% of Python online submissions for Binary Tree Level Order Traversal.
Memory Usage: 12.4 MB, less than 26.47% of Python online submissions for Binary Tree Level Order Traversal.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        queue, res = deque([root]), []
        while queue:
            #size是关键！用来记录每一层的节点个数！
            size = len(queue)
            nodes = []
            for i in range(size):
                node = queue.popleft()
                nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(nodes)
        return res


'''
107. Binary Tree Level Order Traversal II [Easy]
Given a binary tree, return the bottom-up level order traversal of its nodes' values.
 (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


[Method 1]: 按照之前的思路，最后做个reverse。
Runtime: 24 ms, faster than 48.79% of Python online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 12.5 MB, less than 26.09% of Python online submissions for Binary Tree Level Order Traversal II.
'''
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        level = [root]
        while level :
            res.append([node.val for node in level])
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        return res[::-1]

'''
[Method 2]：
按层遍历时，把新一层的节点插入到最前面。
Runtime: 20 ms, faster than 79.16% of Python online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 12.3 MB, less than 56.52% of Python online submissions for Binary Tree Level Order Traversal II.
'''
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        level, res = [root], []
        while level:
            res.insert(0,[node.val for node in level]) #因为每一层的节点也要按照左右的顺序输出
            next_level = []
            for node in level:
                next_level.extend([node.left, node.right])
            level = [node for node in next_level if node]  #去除空节点
        return res


# dfs recursively
def levelOrderBottom1(self, root):
    res = []
    self.dfs(root, 0, res)
    return res

def dfs(self, root, level, res):
    if root:
        if len(res) < level + 1:
            res.insert(0, [])
        res[-(level+1)].append(root.val)
        self.dfs(root.left, level+1, res)
        self.dfs(root.right, level+1, res)

# dfs + stack
def levelOrderBottom2(self, root):
    stack = [(root, 0)]
    res = []
    while stack:
        node, level = stack.pop()
        if node:
            if len(res) < level+1:
                res.insert(0, [])
            res[-(level+1)].append(node.val)
            stack.append((node.right, level+1))
            stack.append((node.left, level+1))
    return res

# bfs + queue
def levelOrderBottom(self, root):
    queue, res = collections.deque([(root, 0)]), []
    while queue:
        node, level = queue.popleft()
        if node:
            if len(res) < level+1:
                res.insert(0, [])
            res[-(level+1)].append(node.val)
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return res
