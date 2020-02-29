'''
给出一个数组arr，
可以给任意数乘2(0次或无数次)，
判断能否使得arr里数都相等。

'''
import sys

def same_nums(arr):
    for i in range(n):
        while not (arr[i] & 1):
            arr[i] //= 2
    x = arr[0]
    for num in arr:
        if num != x:
            return "NO"
    return "YES"


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    if n != len(arr): print('NO')
    print(same_nums(arr))
