'''
54. Spiral Matrix [Medium]
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

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
The path that the spiral makes will turn clockwise whenever it would go out of bounds
or into a cell that was previously visited.


[Method 1]: Traversing each element by changing directions
Let the array have m rows and n columns.
seen[r][c] denotes that the cell on the r-th row and c-th column was previously visited.
Our current position is (row, col), facing direction di, and we want to visit m x n total cells.

As we move through the matrix, our candidate's next position is (r, c).
If the candidate is in the bounds of the matrix and unseen, then it becomes our next position;
otherwise, our next position is the one after performing a clockwise turn.

[Time Complexity]: O(N), where N is the total number of elements in the input matrix.
We add every element in the matrix to our final answer.
[Space Complexity]: O(N), the information stored in seen and in ans.

Runtime: 36 ms, faster than 73.43% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.6 MB, less than 8.70% of Python3 online submissions for Spiral Matrix.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        di_r = [0, 1, 0, -1]
        di_c = [1, 0, -1, 0]
        seen = [[0]*n for row in matrix]
        ans = []
        row = col = di = 0
        for cell in range(m*n):
            ans.append(matrix[row][col])
            seen[row][col] = 1
            r, c = row + di_r[di], col + di_c[di]
            if 0 <= r < m and 0 <= c < n and not seen[r][c]:
                row, col = r, c
            else:
                di = (di+1) % 4
                row, col = row + di_r[di], col + di_c[di]
        return ans
'''
#or [Optimization]:
Runtime: 36 ms, faster than 73.43% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.8 MB, less than 8.70% of Python3 online submissions for Spiral Matrix.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans
        i, j, di, dj = 0, 0, 0, 1
        m, n = len(matrix), len(matrix[0])
        for cell in range(m * n):
            ans.append(matrix[i][j])
            matrix[i][j] = ''
            if matrix[(i + di) % m][(j + dj) % n] == '':
                di, dj = dj, -di
            i += di
            j += dj
        return ans

'''
[Method 2]: Peeling off the matrix layer by layer.
Time: O(N), Space: O(N)
Runtime: 36 ms, faster than 73.43% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.6 MB, less than 8.70% of Python3 online submissions for Spiral Matrix.
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if not matrix:
            return ans
        l, t, b, r = 0, 0, len(matrix)-1, len(matrix[0])-1
        while l < r and t < b:
            #Peeling the top
            for i in range(l, r):
                ans.append(matrix[l][i])

            #Peeling the right
            for i in range(t, b):
                ans.append(matrix[i][r])
            #Peeling the bottom
            for i in range(r, l, -1):
                ans.append(matrix[b][i])
            #Peeling the left
            for i in range(b, t, -1):
                ans.append(matrix[i][l])
            b -= 1
            t += 1
            l += 1
            r -= 1
        #Adding the leftover in the middle
        #Horizontal line left
        if t == b:
            for i in range(l, r+1):
                ans.append(matrix[l][i])
        #Vertical line left
        elif l == r:
            for i in range(t,b+1):
                ans.append(matrix[i][l])
        return ans


'''
[Method 3]: Peeling off the matrix by pop(),
if this is not allowed, we can make a deep copy of the matrix first.
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


'''
[Method 4]: Python One-liner
[Note]:
if matrix = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
Then:
>>> [*matrix.pop(0)]
[1, 2, 3]
>>> matrix
[[4, 5, 6], [7, 8, 9]]
>>>

[Visualization]
Here's how the matrix changes by always extracting the first row
and rotating the remaining matrix counter-clockwise:

    |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
    |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
    |7 8 9|      |4 7|

Now look at the first rows we extracted:

    |1 2 3|      |6 9|      |8 7|      |4|      |5|

Those concatenated are the desired result.

[Another visualization]
  spiral_order([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

= [1, 2, 3] + spiral_order([[6, 9],
                            [5, 8],
                            [4, 7]])

= [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                     [5, 4]])

= [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                              [5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

= [1, 2, 3, 6, 9, 8, 7, 4, 5]
'''
def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
