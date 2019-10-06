'''
59. Spiral Matrix II
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]


[Method 1]: Walk the spiral
Iteration using direction of rows and columns.
Initialize the matrix with zeros, then walk the spiral path and write the numbers 1 to n*n.
Make a right turn when the cell ahead is already non-zero.

Time: O(n**2), Space:O(n**2)
Runtime: 36 ms, faster than 85.71% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 13.8 MB, less than 9.09% of Python3 online submissions for Spiral Matrix II.
 '''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0: return []
        matrix = [[0]*n for _ in range(n)]
        row, col, di_r, di_c = 0, 0, 0, 1
        for num in range(1, n*n+1):
            matrix[row][col] = num
            if matrix[(row+di_r) % n][(col+di_c) % n]:
                di_r, di_c = di_c, -di_r
            row += di_r
            col += di_c
        return matrix

'''
[Method 2]: walking within step pattern of [n, n-1, n-1, n-2, n-2 ..., 2, 2, 1, 1]
If n is 5, step list will be [5, 4, 4, 3, 3, 2, 2, 1, 1],
it means move forward 5 steps, turn right, move forward 4 steps,
turn right, move forward 4 steps, turn right and so on.
x axis is from left to right, y axis is from top to bottom, we start from point (-1, 0).

Time: O(n**2),实际上是O(2n-1 + n**2)
Space: O(n**2)
Runtime: 40 ms, faster than 57.90% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 13.7 MB, less than 9.09% of Python3 online submissions for Spiral Matrix II.
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0: return []
        matrix, col, row, dc, dr, number = [[0] * n for i in range(n)], -1, 0, 1, 0, 0
        for step in [i // 2 for i in range(2 * n, 1, -1)]:
            for j in range(step):
                col, row, number = col + dc, row + dr, number + 1
                matrix[row][col] = number
            dc, dr = -dr, dc # turn right
        return matrix
