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
    __slots__ = '_item' , '_left' , '_right'

    def __init__ (self, item, left=None, right=None):
        self._item = item
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__ (self, root=None):
        self._root = root

    # Get methods
    def get(self, key):
        return self.__get(self._root, key);

    def __get(self, node, key): # helper
        if (node is None):
            return None
        if (key == node._item):
            return node._item
        if (key < node._item):
            return self.__get(node._left, key)
        else:
            return self.__get(node._right, key)

    # add methods
    def add(self, value):
        self._root = self.__add(self._root, value)

    def __add(self, node, value): # return node ,helper
        if (node is None):
            return Node(value)
        if (value == node._item):
            pass
        else:
            if (value < node._item):
                node._left = self.__add(node._left, value)
            else:
                node._right = self.__add(node._right, value)
        return node

    # remove methods
    def remove(self, key):
        self._root = self.__remove(self._root, key)

    def __remove(self, node, key):  # helper
        if node is None:
            return None
        if (key < node._item):
            node._left = self.__remove(node._left, key)
        elif (key > node._item):
            node._right = self.__remove(node._right, key)
        else:
            if (node._left is None):
                node = node._right  # if right is None,  node = None; case 1: no child
                                    # if right is not None, node = node._right; case 2: one child
            elif (node._right is None):
                node = node._left
            else:
                node._item = self.__get_max(node._left)
                node._left = self.__remove(node._left, node._item)

        return node

    # get max/min methods
    def get_max(self):
        return self.__get_max(self._root)

    def __get_max(self, node): # helper
        if (node is None):
            return None
        while (node._right is not None):
            node = node._right
        return node._item

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
