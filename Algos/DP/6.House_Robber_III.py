'''
337. House Robber III [Medium]

The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root."
Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:
Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.


[Analysis]
Step I -- Think naively
At first glance, the problem exhibits the feature of "optimal substructure":
if we want to rob maximum amount of money from current binary tree (rooted at root),
we surely hope that we can do the same to its left and right subtrees.

So going along this line, let's define the function rob(root)
which will return the maximum amount of money that we can rob for the binary tree rooted at root;
the key now is to construct the solution to the original problem from solutions to its subproblems,
i.e., how to get rob(root) from rob(root.left), rob(root.right), ... etc.

Apparently the analyses above suggest a recursive solution.
And for recursion, it's always worthwhile figuring out the following two properties:
1.Termination condition: when do we know the answer to rob(root) without any calculation?
Of course when the tree is empty ---- we've got nothing to rob so the amount of money is zero.

2.Recurrence relation: i.e., how to get rob(root) from rob(root.left), rob(root.right), ... etc.
From the point of view of the tree root, there are only two scenarios at the end: root is robbed or is not.
a).If it is, due to the constraint that "we cannot rob any two directly-linked houses",
the next level of subtrees that are available would be the four "grandchild-subtrees"
(root.left.left, root.left.right, root.right.left, root.right.right).
b).However if root is not robbed, the next level of available subtrees would
just be the two "child-subtrees" (root.left, root.right).

We only need to choose the scenario which yields the larger amount of money.
Here is the program for the ideas above:
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Time Limit Exceeded
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        Sum = 0
        if root.left:
            Sum += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            Sum += self.rob(root.right.left) + self.rob(root.right.right)
        return max(Sum + root.val, self.rob(root.left) + self.rob(root.right))

'''
Step II -- Think one step further

In step I, we only considered the aspect of "optimal substructure",
but think little about the possibilities of overlapping of the subproblems.
For example,
to obtain rob(root), we need rob(root.left), rob(root.right), rob(root.left.left),
rob(root.left.right), rob(root.right.left), rob(root.right.right);
but to get rob(root.left), we also need rob(root.left.left), rob(root.left.right),
similarly for rob(root.right).
The naive solution above computed these subproblems repeatedly,
which resulted in bad time performance.

Now if you recall the two conditions for dynamic programming:
"optimal substructure" + "overlapping of subproblems",
we actually have a DP problem.

A naive way to implement DP here is to use a hash map to record the results for visited subtrees.

Time: O(n); Space: O(n)
Runtime: 56 ms, faster than 75.50% of Python3 online submissions for House Robber III.
Memory Usage: 16.6 MB, less than 13.33% of Python3 online submissions for House Robber III.
'''
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        self.dict = {}
        def dp(node):
            if not node: return 0
            if node not in self.dict:
                Sum = 0
                if node.left:
                    Sum += dp(node.left.left) + dp(node.left.right)
                if node.right:
                    Sum += dp(node.right.left) + dp(node.right.right)
                self.dict[node] = max(node.val + Sum, dp(node.left)+dp(node.right))
            return self.dict[node]
        return dp(root)


'''
Step III -- Think one step back [DFS]

In step I, we defined our problem as rob(root),
which will yield the maximum amount of money that can be robbed of the binary tree rooted at root.
This leads to the DP problem summarized in step II.

Now let's take one step back and ask why we have overlapping subproblems.
If you trace all the way back to the beginning,
you'll find the answer lies in the way how we have defined rob(root).
As I mentioned, for each tree root, there are two scenarios: it is robbed or is not.
rob(root) does not distinguish between these two cases,
so "information is lost as the recursion goes deeper and deeper",
which results in repeated subproblems.

If we were able to maintain the information about the two scenarios for each tree root,
let's see how it plays out.
Redefine rob(root) as a new function which will return a list of two elements,
the first element of which denotes the maximum amount of money that can be robbed if root is NOT ROBBED,
while the second element signifies the maximum amount of money robbed if it is ROBBED.

Runtime: 60 ms, faster than 52.06% of Python3 online submissions for House Robber III.
Memory Usage: 15.9 MB, less than 33.33% of Python3 online submissions for House Robber III.
'''
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node: return (0,0)
            left = dfs(node.left)
            right = dfs(node.right)
            return max(left) + max(right), node.val + left[0] + right[0]
        return max(dfs(root))
