'''
48. Rotate Image [Medium]
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]


[Method 1]: 不合格
Extra space making copy of all elements.
[Time]: O(n*n)
[Space]: O(n*n)
Runtime: 44 ms, faster than 53.41% of Python3 online submissions for Rotate Image.
Memory Usage: 13.8 MB, less than 6.25% of Python3 online submissions for Rotate Image.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        array = []
        for row in matrix:
            array += row
        for col in range(n):
            for row in range(n):
                matrix[row][col] = array[(n-col-1)*n + row]

'''
[Method 2]: Transpose + Reverse Row
先转置矩阵（把行与列index对换），再把每行翻转过来。
E.G.
[                     [                       [
  [1,2,3],  Transpose   [1,4,7]   Reverse Row    [7,4,1]
  [4,5,6],   ======>    [2,5,8]     ======>      [8,5,2]
  [7,8,9]               [3,6,9]                  [9,6,3]
]                     ]                       ]

[Time]: O(n*n)
[Space]: O(1)
Runtime: 36 ms, faster than 96.60% of Python3 online submissions for Rotate Image.
Memory Usage: 14 MB, less than 6.25% of Python3 online submissions for Rotate Image.
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for row in range(n):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        for row in range(n):
            matrix[row].reverse()

'''
[Method 2]: using *args, map() and zip()
The same intuition as method 1
A = zip(*A[::-1]) just reassigns the variable A to point at that new array,
whereas A[:] = zip(*A[::-1]) reassigns all of the contents of A to be equal to the contents of zip(*A[::-1])

>>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
>>> print(*matrix, sep = '\n')
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
>>> print(*matrix[::-1], sep = '\n')
[7, 8, 9]
[4, 5, 6]
[1, 2, 3]
>>> map(list,zip(*matrix[::-1]))
<map object at 0x02C6F750>
>>> matrix
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> rotated = list(map(list,zip(*matrix[::-1])))
>>> rotated
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
>>>

'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list,zip(*matrix[::-1]))
