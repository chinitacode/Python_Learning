'''
字节跳动面试题，
同样的条件，给出一个target，看在数组里面小于等于k的元素个数有多少个。
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

k = 16,
Output: 16


[解析]
因为每行每列都是排好序的，所以对于一个位于非边界的元素，比它小的有向上向左两种方向，
比它大的有向右向下两种方向，比较起来比较麻烦。但是对于边界元素，如最后一行的第一个元素，
要找比它小的元素只有往上遍历，找比它大的只能往右遍历，所以这样下来worst case的时间复杂度也就(m + n),
即最多需要遍历 m + n 个元素。
'''
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]: return None
    rows = len(matrix)
    cols = len(matrix[0])
    row, col = rows-1, 0
    count = 0
    while row >= 0 and col < cols:
        if target >= matrix[row][col]:
            count += row + 1
            col += 1
        else:
            row -= 1
    return count

if __name__ == '__main__':
    matrix = [
      [1,   4,  7, 11, 15],
      [2,   5,  8, 12, 19],
      [3,   6,  9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]
    ]
    print(searchMatrix(matrix,16)) #16
    matrix = [[1,2,3,3,4],[2,2,3,4,5],[3,3,3,5,8]]
    print(searchMatrix(matrix,3)) #10
