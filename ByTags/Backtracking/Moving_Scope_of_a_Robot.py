'''
地上有一个 m 行和 n 列的方格，横纵坐标范围分别是 0∼m−1 和 0∼n−1。

一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格。

但是不能进入行坐标和列坐标的数位之和大于 k 的格子。

请问该机器人能够达到多少个格子？

样例1
输入：k=7, m=4, n=5

输出：20
样例2
输入：k=18, m=40, n=40

输出：1484

解释：当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
      但是，它不能进入方格（35,38），因为3+5+3+8 = 19。
注意:

0<=m<=50
0<=n<=50
0<=k<=100

[Method 1]: Backtracking
从[0,0]开始，先向右递归再向下递归，
用一个一维数组visited来标记已经走过了的格子。
最终走完全部格子后返回count。
'''

class Solution(object):
    def movingCount(self, threshold, rows, cols):
        """
        :type threshold: int
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if not threshold:
            return 1
        if not rows or not cols:
            return 0
        self.visited = [0]*rows*cols
        self.count = 0
        def helper(i,j):
            if i%10 + i//10 + j%10 + j//10 <= threshold and not self.visited[i*cols + j]:
                self.visited[i*cols + j] = 1
                self.count += 1
                if 0 <= i < rows and 0 <= j + 1 < cols:
                    helper(i,j+1)
                if 0 <= i+1 < rows and 0 <= j < cols:
                    helper(i+1,j)

        helper(0,0)
        return self.count


#Or:
# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold < 0 or rows <= 0 or cols <= 0: return 0
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        return self.count(threshold, cols, rows, 0 ,0 ,visited)

    def count(self,threshold, cols, rows, i , j ,visited):
        if i >= rows or j >= cols or visited[i][j] == 1 or threshold < sum(map(int,str(i)+str(j))): return 0
        visited[i][j] = 0
        return 1 + self.count(threshold, cols, rows, i + 1 , j ,visited) + self.count(threshold, cols, rows, i  , j + 1,visited)
