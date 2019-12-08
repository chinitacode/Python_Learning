'''
74. Search a 2D Matrix [Medium]

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
注意：这个题目说的是每一行行首元素都大于上一行的行末元素。

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


[Method 1]：
因为每行每列都是排好序的，所以对于一个位于非边界的元素，比它小的有向上向左两种方向，
比它大的有向右向下两种方向，比较起来比较麻烦。但是对于边界元素，如最后一行的第一个元素，
要找比它小的元素只有往上遍历，找比它大的只能往右遍历，所以这样下来worst case的时间复杂度也就(m + n),
即最多需要遍历 m + n 个元素。（这种方法对于非每一行行首元素都大于上一行的行末元素的情况也适用）。

[Time]: O(m+n)
[Space]: O(1)
Runtime: 64 ms, faster than 94.00% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 15 MB, less than 5.88% of Python3 online submissions for Search a 2D Matrix.

同样适用于：
Your input
[[1,3,5,7],[2,4,6,8],[12,13,18,21],[20,25,30,35]]
22
Output
false
Expected
false
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        i,j = rows-1,0
        while i >= 0 and j < cols:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                j += 1
            else:
                i -= 1
        return False



'''
[Method 2]: 二分法
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
