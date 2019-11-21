'''
101. Symmetric Tree
Method1: Preorder + Recursion
这道题具体的Recursion Rule不是传递Root本身，而是对两个子孩子的比较，所以Helper的参数定义为root.left 和 root.right.
然后根据题目的特性，在每一层往下传递之前要做比较，所以是preorder的写法，先写比较的几种格式，然后在做递归。递归向上返回的参数是一个Boolean。
时间复杂度 : O(N) 空间复杂度 : O(N) or O(Height)

Runtime: 16 ms, faster than 93.75% of Python online submissions for Symmetric Tree.
Memory Usage: 12 MB, less than 39.13% of Python online submissions for Symmetric Tree.
'''
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self,p,q):
        if not p and not q: return True
        if None in (p,q): return False
        if p.val == q.val:
            return self.is_mirror(p.left, q.right) and self.is_mirror(p.right, q.left)
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
Method2: Preorder + Iteration using Stack
把对称的节点配对成元组压入栈
Runtime: 24 ms, faster than 48.70% of Python online submissions for Symmetric Tree.
Memory Usage: 12 MB, less than 67.39% of Python online submissions for Symmetric Tree.
'''
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        stack = [(root.left, root.right)]
        while stack:
            l,r = stack.pop()
            if not l and not r: continue
            elif None in (l,r):
                return False
            else:
                if l.val != r.val:
                    return False
                stack.append((l.left,r.right))
                stack.append((l.right,r.left))
        return True

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
