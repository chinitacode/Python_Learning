'''
63. 不同路径 II [中等]

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2

解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

[注意！]：因为没说明是否只有一个障碍物，所以不好用数学的组合方法（总路径去掉有障碍物的路径），
因为多个障碍物之间可能存在交叉重复的情况。

[Method 1]: DP
如果格子上有障碍，那么我们不考虑包含这个格子的任何路径。
我们从左至右、从上至下的遍历整个数组，那么在到达某个顶点之前我们就已经获得了到达前驱节点的方案数，
这就变成了一个动态规划问题。我们只需要一个 obstacleGrid 数组作为 DP 数组。

注意： 根据题目描述，包含障碍物的格点有权值 1，我们依此来判断是否包含在路径中，
然后我们可以用这个空间来存储到达这个格点的方案数。

算法

如果第一个格点 obstacleGrid[0,0] 是 1，说明有障碍物，那么机器人不能做任何移动，我们返回结果 0。
否则，如果 obstacleGrid[0,0] 是 0，我们初始化这个值为 1 然后继续算法。
遍历第一行，如果有一个格点初始值为 1 ，说明当前节点有障碍物，没有路径可以通过，设值为 0 ；
否则设这个值是前一个节点的值 obstacleGrid[i,j] = obstacleGrid[i,j-1]。
遍历第一列，如果有一个格点初始值为 1 ，说明当前节点有障碍物，没有路径可以通过，设值为 0 ；
否则设这个值是前一个节点的值 obstacleGrid[i,j] = obstacleGrid[i-1,j]。
现在，从 obstacleGrid[1,1] 开始遍历整个数组，如果某个格点初始不包含任何障碍物，
就把值赋为上方和左侧两个格点方案数之和 obstacleGrid[i,j] = obstacleGrid[i-1,j] + obstacleGrid[i,j-1]。
如果这个点有障碍物，设值为 0 ，这可以保证不会对后面的路径产生贡献。

[时间复杂度] ： O(M×N) 。长方形网格的大小是 M×N，而访问每个格点恰好一次。
[空间复杂度] ： O(1)。我们利用 obstacleGrid 作为 DP 数组，因此不需要额外的空间。
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0]: return 0
        for col in range(len(obstacleGrid[0])):
            if obstacleGrid[0][col]:
                obstacleGrid[0][col] = 0
            elif col == 0:
                obstacleGrid[0][col] = 1
            else:
                obstacleGrid[0][col] = obstacleGrid[0][col-1]
        for row in range(1, len(obstacleGrid)):
            obstacleGrid[row][0] = 0 if obstacleGrid[row][0] else obstacleGrid[row-1][0]
        for row in range(1, len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                obstacleGrid[row][col] = obstacleGrid[row-1][col] + obstacleGrid[row][col-1] if not obstacleGrid[row][col] else 0
        return obstacleGrid[-1][-1]
