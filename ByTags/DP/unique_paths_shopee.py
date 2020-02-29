'''
[编程题]Shopee的办公室（二）
时间限制：C/C++ 1秒，其他语言2秒
空间限制：C/C++ 32M，其他语言64M
shopee的办公室非常大，小虾同学的位置坐落在右上角，而大门却在左下角，
可以把所有位置抽象为一个网格（门口的坐标为0，0），小虾同学很聪明，每次只向上，或者向右走，
因为这样最容易接近目的地，但是小虾同学不想让自己的boss们看到自己经常在他们面前出没，或者迟到被发现。
他决定研究一下如果他不通过boss们的位置，他可以有多少种走法？

输入描述:

第一行 x,y,n (0<x<=30, 0<y<=30, 0<=n<= 20) 表示x,y小虾的座位坐标,n 表示boss的数量（ n <= 20）

接下来有n行, 表示boss们的坐标(0<xi<= x, 0<yi<=y，不会和小虾位置重合)

x1, y1

x2, y2

……

xn, yn

输出描述:

输出小虾有多少种走法

输入例子1:

3 3 2
1 1
2 2

输出例子1:

4
'''


import sys

def unique_paths(m, n, grid):
    if grid[0][0] == 1: return 0
    grid[0][0] = 1
    for row in range(1,m):
        grid[row][0] = 0 if grid[row][0] else grid[row-1][0]
    for col in range(1,n):
        grid[0][col] = 0 if grid[0][col] else grid[0][col-1]
    for row in range(1,m):
        for col in range(1,n):
            grid[row][col] = grid[row-1][col] + grid[row][col-1] if not grid[row][col] else 0
    return grid[-1][-1]

if __name__ == '__main__':
    row1 = list(map(int,sys.stdin.readline().strip().split()))
    m, n, n_boss = row1
    m += 1
    n += 1
    bosses = []
    for _ in range(n_boss):
        bosses.append(list(map(int,sys.stdin.readline().strip().split())))
    grid = [[0]*m for _ in range(n)]
    for boss in bosses:
        grid[boss[0]][boss[1]] = 1
    # print(m,n,bosses,grid)
    print(unique_paths(m,n,grid))
