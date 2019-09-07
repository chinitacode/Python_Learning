'''
54. Spiral Matrix
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

[Analysis]
The path that the spiral makes will turn clockwise whenever it would go out of bounds or into a cell that was previously visited.


Method1:
Let the array have R rows and C columns. 
seen[r][c] denotes that the cell on the r-th row and c-th column was previously visited. 
Our current position is (r, c), facing direction di, and we want to visit R x C total cells.

As we move through the matrix, our candidate's next position is (cr, cc). 
If the candidate is in the bounds of the matrix and unseen, then it becomes our next position; 
otherwise, our next position is the one after performing a clockwise turn.

[Time Complexity]: O(N), where NN is the total number of elements in the input matrix. 
We add every element in the matrix to our final answer.
[Space Complexity]: O(N), the information stored in seen and in ans. 


'''
class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans

#or:
def spiralOrder(self, matrix):
    res = []
    if not matrix:
        return []
    i,j,di,dj = 0,0,0,1
    m, n = len(matrix),len(matrix[0])
    for v in xrange(m * n):
        res.append(matrix[i][j])
        matrix[i][j] = ''
        if matrix[(i+di)%m][(j+dj)%n] == '':
            di, dj = dj, -di
        i += di
        j += dj
        
    return res

'''
Method2:
Peel the the matrix layer by layer.
Mutating the matrix, if this is not allowed, we can make a deep copy of the matrix first. 
And of course it comes with the additional memory usage.

Time: O(m(m+n)) because of pop(0)
Runtime: 36 ms, faster than 72.60% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.9 MB, less than 8.70% of Python3 online submissions for Spiral Matrix.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret
