'''
797. 所有可能的路径 [中等]

给一个有 n 个结点的有向无环图，找到所有从 0 到 n-1 的路径并输出（不要求按顺序）

二维数组的第 i 个数组中的单元都表示有向图中 i 号结点所能到达的下一些结点
（译者注：有向图是有方向的，即规定了a→b你就不能从b→a）空就是没有下一个结点了。

示例:
输入: [[1,2], [3], [3], []]
输出: [[0,1,3],[0,2,3]]

解释: 图是这样的:
0--->1
|    |
v    v
2--->3
这有两条路: 0 -> 1 -> 3 和 0 -> 2 -> 3.

提示:

结点的数量会在范围 [2, 15] 内。
你可以把路径以任意顺序输出，但在路径内的结点的顺序必须保证。

[Method 1]: Recursion
[Time]: O(n*2^n) There are 2^(N-2) paths and (N+2)*2^(N-3) nodes in all paths. We can roughly say O(2^N)
(Each vertex can be in or not in the path, apart from the first and the last. So at most 2 ^ (n - 2))
[Space]: O(n*2^n), the size of the output dominating the final space complexity,
at most 2^(N-2) paths and each path contains at most N nodes.

[Detailed Analysis of Time Complexity]:
I think the time complexity is O(2^n).
Think about this worst case scenario:
Suppose we have n nodes, labeled 0 to n-1.
Think of it as an array: [0, 1, 2, 3, 4, 5, 6, ..., n-1]
For each pair of nodes i and j, if i < j, let there be an edge between node i and node j.
(So, there are O(n^2) edges, though this fact is not important.)
Now, we want to calculate how many paths there are from the 0th node to the (n-1)th node.
Well, notice that each path of length k corresponds to some choice of (k - 1) nodes between 0 and (n-1).
For example, here are two paths of length 2:
0->3->(n-1)
0->5->(n-1)
Here is a path of length 3:
0->1->5->(n-1)
How many paths of length k are there? The answer is (n-2 choose k-1) because we pick k - 1 nodes between 0 and (n - 1).
The total number of paths is the sum of (n-2 choose k-1) for k = 1, 2, ..., (n-1).
Using the binomial theorem, this sum is equal to 2^(n-2) which is O(2^n).

Runtime: 104 ms, faster than 77.86% of Python3 online submissions for All Paths From Source to Target.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for All Paths From Source to Target.
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        def dfs(tmp, s):
            if s == n-1:
                paths.append(tmp[:])
            for nbr in graph[s]:
                tmp.append(nbr)
                dfs(tmp, nbr)
                tmp.pop()
        dfs([0], 0)
        return paths

'''
[Method 2]: Iteration
Runtime: 92 ms, faster than 99.25% of Python3 online submissions for All Paths From Source to Target.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for All Paths From Source to Target.
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        paths = []
        stack = [(0, [0])]
        while stack:
            vertex, tmp = stack.pop()
            if vertex == n-1:
                paths.append(tmp[:])
            if graph[vertex]:
                stack += [(nbr, tmp+[nbr]) for nbr in graph[vertex]]
        return paths
