'''
74. Search a 2D Matrix [Medium]

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false


[Method 1]:
[Time]:nlogm,n为行数，m为列数
[Space]: O(1)
Runtime: 52 ms, faster than 99.92% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.9 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        for row in matrix:
            if row[0] <= target <= row[-1]:
                idx = self.binary_search(row, target)
                if idx:
                    return True
                continue
        return False


    def binary_search(self,arr,k):
        lo,hi = 0, len(arr)-1
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if k == arr[mid]:
                return True
            elif k < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return False
