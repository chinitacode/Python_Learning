class Solution(object):
    def movingCount(self, threshold, rows, cols):
        """
        :type threshold: int
        :type rows: int
        :type cols: int
        :rtype: int
        """
        if not threshold or not rows or not cols:
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

if __name__ == '__main__':
    sol = Solution()
    print(sol.movingCount(7,4,5))
    print(sol.movingCount(18,40,40))
    
