'''
958. Check Completeness of a Binary Tree [Medium]
验证完全二叉树
Given a binary tree, determine if it is a complete binary tree.
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible.
It can have between 1 and 2h nodes inclusive at the last level h.



Example 1:



Input: [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}),
and all nodes in the last level ({4, 5, 6}) are as far left as possible.


Example 2:



Input: [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Note:
The tree will have between 1 and 100 nodes.


[完全二叉树]：
·二叉树(Binary Tree): 二叉树左右侧连接为空或者节点。
·完全树(Complete tree): 除了最底层，完全对称平衡。

完全二叉树特性：
1.有N个节点的完全树的高度是： logN  (root的高度为0算)
2.有N个节点的完全树的层数是：高度+1 = logN + 1;
  每一层填满后的总节点数为2^n - 1, n为当前层数（root为第1层）， 如3层的完全对称平衡树的总节点个数为1+2+4 = 2^3 -1 = 7。
3.反推，如果高度为h，则总节点数至少为2^h个(至少比高度为h-1,即层数为h的完全对称平衡树总节点个数多1)，并且小于2^(h+1) 个(最后一层可以全满，即总节点数为2^(h+1)-1。
 (当N是2的指数时层数才会增加)。
4.可以按照层次遍历把节点全部sort成一个list，就是按照层序遍历顺序将每个节点上的值存放在数组中。
  则对于任何一个index为i的node,它的parent的index为(i-1)//2;
  其left child的index为2*i + 1(如果存在的话); 右child为2*i + 2(如果存在的话)。

[Method 1]: Level-order Traversal (BFS)
首先，空树、完全平衡二叉树（左右平衡，都是满的）也是完全二叉树。

  1           1           1           1
   \                     /           /
    2                   2           2
                                   /
                                  3

 False       True       True          False

不是完全二叉树有两种情况：
1.当前层还有剩余要遍历的节点(非空节点)，目前已遇到空节点；（不满足节点尽量靠左的条件）
2.当下一层还有要遍历的节点(非空节点)，当前层却已有空节点。（不满足除最后一层外其余层都是满节点的条件）

我们可以引入一个flag变量来标注遇到空节点。

此外，
层次遍历的迭代写法里面，stack记录当前要遍历的层，
对于其中的每个节点的遍历，用的是 for 循环，循环的同时把其children压入记录下一层节点的的另一个栈 nxt_level 里，
完成 for 循环后直接用 stack = nxt_level 赋值更新stack， 从始至终都 不pop 任何一个节点。
同时，因为对stack遍历的方式是通过 for 循环， 所以在加入节点的时候按左右顺序就好了，不需要颠倒（因为不是后进先出）。
nxt_level.extend([node.left, node.right]) 即可。

[Time]:O(n)
[Space]: O(h**2)

Runtime: 24 ms, faster than 61.20% of Python online submissions for Check Completeness of a Binary Tree.
Memory Usage: 11.8 MB, less than 75.00% of Python online submissions for Check Completeness of a Binary Tree.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        stack = [root]
        has_None = False
        while stack:
            nxt_level = []
            for node in stack:
                if not node:
                    has_None = True # if there's empty node in the current level
                else:
                    if has_None: return False
                    nxt_level.extend([node.left, node.right])
            if [node for node in nxt_level if node]: # if there are still node to traverse in the next level
                if has_None: return False
                stack = nxt_level
            else:
                return True



'''
[Method 2]: BFS
利用完全二叉树（或者堆）其list化后的index的对应关系：
如果按照层序遍历顺序将每个节点上的值存放在数组中，
  则对于任何一个index为i的node,它的parent的index为 (i-1)//2 ;
  其left child的index为 2*i + 1 (如果存在的话); 右child为 2*i + 2 (如果存在的话)。
 所以我们只需要看最后一个node的index是否等于整个list的长度减1，
 因为如果中间有空节点，则它的index肯定会发生变化。

[Time]: O(N), where N is the number of nodes in the tree.
[Space]: O(N)
Runtime: 24 ms, faster than 61.20% of Python online submissions for Check Completeness of a Binary Tree.
Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Check Completeness of a Binary Tree.
'''
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bfs = [(root,0)]
        i = 0
        while i < len(bfs):
            node,idx = bfs[i]
            i += 1
            if node:
                bfs.append((node.left, 2*idx + 1))
                bfs.append((node.right, 2*idx + 2))

        return bfs[-1][1] == len(bfs)-1
