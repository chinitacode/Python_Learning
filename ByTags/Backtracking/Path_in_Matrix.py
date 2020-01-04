'''
23.矩阵中的路径 [Medium]

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。

注意：
输入的路径不为空；
所有出现的字符均为大写英文字母；

样例
matrix=
[
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]

str="BCCE" , return "true"

str="ASAE" , return "false"

[Method 1]: Backtracking
本题是使用回溯法的典型题目。由于无法确定路径在字符矩阵中的起点，
因此在矩阵中任选一格作为起点，进行搜索，判断是否存在所求路径。
另外还需要与字符矩阵同样大小的标志数组visited，用来检查当前位置字符是否已经包含在路径中。
矩阵中找到的第i个字符也一定对应着路径中第i个位置的字符。
'''
class Solution(object):
    def hasPath(self, matrix, path):
        """
        :type matrix: List[List[str]]
        :type string: str
        :rtype: bool
        """
        if not matrix or not matrix[0] or not path:
            return False
        rows,cols = len(matrix),len(matrix[0])
        visited = [[0]*cols for _ in range(rows)]
        pathlength = 0
        for i in range(rows):
            for j in range(cols):
                # 以矩阵中每一个位置作为起点进行搜索
                if self.haspath(matrix,rows,cols,i,j,path,visited,pathlength):
                    return True
        return False

    def haspath(self,matrix,rows,cols,x,y,path,visited,pathlength):
        # 如果已经走完了
        if pathlength == len(path):
            return True
        curhaspath = False
        if 0 <= x < rows and 0 <= y < cols and matrix[x][y] == path[pathlength] and not visited[x][y]:
            visited[x][y] = 1
            pathlength += 1
            # 分别向左，向右，向上，向下移动一个格子，任一方向能够继续往下走均可
            curhaspath = self.haspath(matrix,rows,cols,x,y-1,path,visited,pathlength) \
                         or self.haspath(matrix,rows,cols,x,y+1,path,visited,pathlength) \
                         or self.haspath(matrix,rows,cols,x-1,y,path,visited,pathlength) \
                         or self.haspath(matrix,rows,cols,x+1,y,path,visited,pathlength)
            # 如果不能再走下一步，需要回退到上一状态
            if not curhaspath:
                pathlength -= 1
                visited[x][y] = 0
        return curhaspath

if __name__ == '__main__':
    matrix = [["A","B","C","E"],
              ["S","F","C","S"],
              ["A","D","E","E"]]
    sol = Solution()
    print(sol.hasPath(matrix,'BCCE')) # True
    print(sol.hasPath(matrix,'ASAE')) # False

'''
[剑指Offer]：

题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，
路径不能再次进入该格子。

注意：
此处的输入matrix是一个str，所以需要用rows和cols标明其行列数。
'''
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or len(matrix) != rows * cols or not path:
            return False
        visited = [0] * len(matrix)
        pathlength = 0
        for i in range(rows):
            for j in range(cols):
                # 以矩阵中每一个位置作为起点进行搜索
                if self.haspath(matrix,rows,cols,i,j,path,visited,pathlength):
                    return True
        return False

    def haspath(self,matrix,rows,cols,x,y,path,visited,pathlength):
        # 如果已经找到了
        if pathlength == len(path):
            return True
        curhaspath = False
        if 0 <= x < rows and 0 <= y < cols and matrix[x*cols + y] == path[pathlength] and not visited[x*cols + y]:
            visited[x*cols + y] = 1
            pathlength += 1
            # 分别向左，向右，向上，向下移动一个格子，任一方向能够继续往下走均可
            curhaspath = self.haspath(matrix,rows,cols,x,y-1,path,visited,pathlength) or self.haspath(matrix,rows,cols,x,y+1,path,visited,pathlength) or self.haspath(matrix,rows,cols,x-1,y,path,visited,pathlength) or self.haspath(matrix,rows,cols,x+1,y,path,visited,pathlength)
            # 如果不能再走下一步，需要回退到上一状态
            if not curhaspath:
                pathlength -= 1
                visited[x*cols + y] = 0
        return curhaspath


#or:
# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix:
            return False
        if not path:
            return True
        x = [list(matrix[cols*i:cols*i+cols]) for i in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if self.exist_helper(x, i, j, path):
                    return True
        return False
    def exist_helper(self, matrix, i, j, p):
        if matrix[i][j] == p[0]:
            if not p[1:]:
                return True
            matrix[i][j] = ''
            if i > 0 and self.exist_helper(matrix, i-1, j, p[1:]):
                return True
            if i < len(matrix)-1 and self.exist_helper(matrix, i+1, j ,p[1:]):
                return True
            if j > 0 and self.exist_helper(matrix, i, j-1, p[1:]):
                return True
            if j < len(matrix[0])-1 and self.exist_helper(matrix, i, j+1, p[1:]):
                return True
            matrix[i][j] = p[0]
            return False
        else:
            return False
