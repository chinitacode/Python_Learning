class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if not matrix or len(matrix) != rows or len(matrix[0]) != cols or not path:
            return False
        visited = [[0]*cols for _ in range(rows)]
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
    print(sol.hasPath(matrix,3,4,'BCCE'))
    print(sol.hasPath(matrix,3,4,'ASAE'))

                
        
                
