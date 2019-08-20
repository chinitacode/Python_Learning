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
