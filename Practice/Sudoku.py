def sudoku(matrix):
    n = len(matrix)

    for i in range(n):
        result_row = result_col = result_blk = 0
        for j in range(n):
            # Check row
            if result_row & (1 << (matrix[i][j] - 1 )) == 0:
                result_row = result_row | (1 << (matrix[i][j] - 1 ))
            else:
                print('row:', i, j)
                return False

            # Check column
            if result_col & (1 << (matrix[j][i] - 1)) == 0:
                result_col = result_col | (1 << (matrix[j][i] - 1))
            else:
                print('col:', j, i)
                return False

            # Check block
            blk_row = (i // 3) * 3 + j // 3
            blk_col = (i % 3) * 3 + j % 3
            tmp = matrix[blk_row][blk_col]

            if result_blk & (1 << (tmp - 1)) == 0:
                result_blk = result_blk | (1 << (tmp - 1))
            else:
                print('block:', blk_row, blk_col)
                return False

    return True

matrix = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]


matrix1 = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,5,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
