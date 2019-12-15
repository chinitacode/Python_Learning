'''
105. Construct Binary Tree from Preorder and Inorder Traversal [Medium]

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

[Analysis]:
我们需要考虑，前、中、后序遍历三种方式遍历结果有什么特点。
前序遍历：第一个元素必然是根节点，扩展一点将，
如果我们从前序遍历的序列中取出的一段属于某个子树的前序遍历段，
那么该子序列的第一个结点也将是该子树的根节点。

中序遍历：中序遍历由于是先左后根，最后再右的顺序，因此，当我们知道某个结点为跟结点的话，
那么它的左右两侧分别是左子树和右子树的中序遍历序列。同上，也扩展一点将，
只要可以找到某一段子树中序遍历序列的根节点，那么该序列中，跟结点的左右两侧序列也是该子树的左右子树。

后续遍历：后续遍历的特点是遍历完左右结点之后再遍历跟结点。
和前序遍历的区别就在于把根节点放到了最后访问，因此，两种遍历的结果类似，
只不过需要从后向前依次取元素。也就是说，最后一个元素，是当前树的根节点。


经过上面的分析，我们可以得出一个这样的结论，如果我们想重建二叉树，
我们至少需要两种遍历的序列，而且必须要有中序遍历序列。


[Method 1]: 递归 + list slicing
前序遍历的第一个元素为根节点，然后先dfs遍历完左子树再遍历右子树；
而在中序遍历中，该根节点所在位置的左侧为左子树，右侧为右子树。
例如在例题中：
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
preorder 的第一个元素 3 是整棵树的根节点。
inorder 中 3 的左侧 [9] 是树的左子树，右侧 [15, 20, 7] 构成了树的右子树。

所以构建二叉树的问题本质上就是：
找到各个子树的根节点 root
构建该根节点的左子树
构建该根节点的右子树
整个过程我们可以用递归来完成。

【注】假设 preorder = [3,15,9,20,7]
          inorder = [9,15,20,3,7]
          则根节点为3，在中序遍历序列的index为3，
          则其左子树的前序遍历节点序列为preorder[1:1+3],
          因为前序遍历是遍历了根节点后就先把左子树按前序遍历遍历完，再回到右子树进行前序遍历，
          所以可以通过根节点在中序遍历的位置把前序遍历序列拆分成左右两树的前序遍历序列。

[Time]: O(n);
[Space]: O(n), 存储整棵树的开销和递归时 list slicing的开销。
Runtime: 200 ms, faster than 31.62% of Python3 online submissions
Memory Usage: 86.5 MB, less than 31.58% of Python3 online submissions
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        root_idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:root_idx + 1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx + 1:], inorder[root_idx + 1:])
        return root


'''
[Method 2]: making preorder a queue (cheap left pops)
Runtime: 140 ms, faster than 58.31% of Python3 online submissions
Memory Usage: 51.1 MB, less than 71.05% of Python3 online submissions
'''
from collections import deque
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = deque(preorder)
        return self.getTree(preorder,inorder)

    def getTree(self,preorder,inorder):
        if inorder:
            idx = inorder.index(preorder.popleft())
            root = TreeNode(inorder[idx])
            root.left = self.getTree(preorder,inorder[:idx])
            root.right = self.getTree(preorder,inorder[idx+1:])
            return root

'''
[Method 3]: 递归 + hashmap + 传入边界index
因为每次都要递归通过root在inorder的index来分左树和右树，
所以为了节省时间开销，干脆直接把inorder映射到一个hash map，
这样每次通过val查询index就只需要O(1)的时间复杂度。
同时每次递归传入lo和hi左右边界作为递归终止的base case，
而root是从preorder[0]开始，每次递归都要将其在preorder里的索引值加1，
即最好是设置个global变量，但是内部递归函数可以对它进行修改。
【注】：每次找root val时可以只从跟踪的preorder里的root_idx去找，
而root_idx只需要线性递增不管右子树，是因为递归设计为先把左子树build好了，我
我们才返回来开始递归右子树，这个时候的root_idx已经递增到指向右子树的root了。
[Time]: O(n)
[Space]: O(n), hashmap的开销。
Runtime: 52 ms, faster than 95.98% of Python3 online submissions
Memory Usage: 17.1 MB, less than 86.84% of Python3 online submissions
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(lo = 0, hi = len(inorder)-1):
            #停止递归的条件
            if lo > hi:
                return None
            nonlocal root_idx
            root_val = preorder[root_idx]
            root = TreeNode(root_val)
            idx = idx_map[root_val]
            #split tree
            root_idx += 1
            root.left = helper(lo,idx-1)
            root.right = helper(idx + 1, hi)
            return root

        root_idx = 0
        # O(n)
        idx_map = {val:idx for idx,val in enumerate(inorder)}
        return helper()


'''
[Method 4]: 递归 + reverse preorder and inorder
因为每次递归的root都是preorder的列首，pop(0)的时间复杂度为O(n),
所以把preorder逆序，同时inorder只是起一个分裂左右子树的作用，
而且每次查找root在inorder里的位置也是接近O(n), 特别是最坏情况为树只有左分支，
即是从root往左长出的一条斜线的时候，inorder就是preorder的逆序，
那么每次递归时在inorder里搜索root的index都是O(n)，使得整个时间复杂度为O(n^2),
所以我们把inorder也逆序。
每次递归的终止条件是inorder为空或者inorder最后一个节点等于我们要找的root，
所以在从preorder中拿走root后我们就递归地把这个root.val作为建好左子树的终止条件，
那么每次建好左子树我们就把root在inorder中pop掉，即pop掉inorder的最后一个元素，
再建右子树，那么右子树的终止条件stop和主函数的stop条件相同。
Each recursive call gets told where to stop,
and it tells its subcalls where to stop.
It gives its own root value as stopper to its left subcall and
its parent`s stopper as stopper to its right subcall.
[Time]: O(n) + O(2n) = O(n);
[Space]: O(1), 除了最后返回的tree，不需要额外的空间。
Runtime: 48 ms, faster than 98.42% of Python3 online submissions
Memory Usage: 16.6 MB, less than 86.84% of Python3 online submissions
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root
        preorder.reverse()
        inorder.reverse()
        return build(None)






'''
[Explanation/Discussion]:

Consider this input:
preorder: [1, 2, 4, 5, 3, 6]
inorder: [4, 2, 5, 1, 6, 3]
The obvious way to build the tree is:

Use the first element of preorder, the 1, as root.
Search it in inorder.
Split inorder by it, here into [4, 2, 5] and [6, 3].
Split the rest of preorder into two parts as large as the inorder parts,
here into [2, 4, 5] and [3, 6].
Use preorder = [2, 4, 5] and inorder = [4, 2, 5] to add the left subtree.
Use preorder =[3, 6]andinorder = [6, 3] to add the right subtree.
But consider the worst case for this:
A tree that's not balanced but is just a straight line to the left.
Then inorder is the reverse of preorder, and already the cost of step 2,
searching in inorder, is O(n^2) overall.
Also, depending on how you "split" the arrays,
you're looking at O(n^2) runtime and possibly O(n^2) space for that as well.

You can bring the runtime for searching down to O(n) by building a map
from value to index before you start the main work, a
nd I've seen several solutions do that.
But that is O(n) additional space, and also the splitting problems remain.
To fix those, you can use pointers into preorder and inorder instead of splitting them.
And when you're doing that, you don't need the value-to-index map, either.

Consider the example again. Instead of finding the 1 in inorder,
splitting the arrays into parts and recursing on them,
just recurse on the full remaining arrays and stop when you come across the 1 in inorder.
That's what my above solution does. Each recursive call gets told where to stop,
and it tells its subcalls where to stop.
It gives its own root value as stopper to its left subcall and its parent`s stopper as stopper to its right subcall.

'''
