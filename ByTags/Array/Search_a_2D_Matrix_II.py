'''
240. Search a 2D Matrix II [Medium]

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:
Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example:

Consider the following matrix:
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

[Method 1]：和前一题同样的方法
因为每行每列都是排好序的，所以对于一个位于非边界的元素，比它小的有向上向左两种方向，
比它大的有向右向下两种方向，比较起来比较麻烦。但是对于边界元素，如最后一行的第一个元素，
要找比它小的元素只有往上遍历，找比它大的只能往右遍历，所以这样下来worst case的时间复杂度也就(m + n),
即最多需要遍历 m + n 个元素。
[Time]: O(m+n)
[Space]: O(1)
Runtime: 32 ms, faster than 93.28% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 17.4 MB, less than 92.59% of Python3 online submissions for Search a 2D Matrix II.
'''
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
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
和上一题一样，先定位到需要遍历的行，即row[0] <= target <= row[-1]，
再二分搜索看是否存在，如果不存在，继续遍历满足条件的下一行。
[Time]:nlogm,n为行数，m为列数
[Space]: O(1)
Runtime: 36 ms, faster than 83.81% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 17.4 MB, less than 92.59% of Python3 online submissions for Search a 2D Matrix II.
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
