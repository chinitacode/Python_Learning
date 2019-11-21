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

# 前序遍历DFS with stack
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


#BFS with queue
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        queue = deque()
        queue.append((p,q))
        while queue:
            node1,node2 = queue.popleft()
            if not node1 and not node2:
                continue
            elif None in (node1,node2):
                return False
            else:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left,node2.left))
                queue.append((node1.right,node2.right))
        return True
