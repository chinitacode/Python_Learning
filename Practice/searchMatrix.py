def searchMatrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m < 1 :
            return False
        n = len(matrix[0])
        if n < 1:
            return False
        row = 0
        while row < m - 1 and matrix[row][0] <= target:
            row += 1
        print(row)
        for r in range(row + 1):
            if matrix[r][0] <= target and target <= matrix[r][-1]:
                left, right = 0, n-1
                while left + 1 < right:
                    mid = left + (right - left) // 2
                    if matrix[r][mid] == target:
                        return True
                    if matrix[r][mid] < target:
                        left = mid
                    else:
                        right = mid 
                if matrix[r][left] == target or matrix[r][right] == target:
                    return True
            
        return False
