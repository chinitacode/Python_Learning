'''
排序子序列为一个数组中一段连续的子序列，
并且这段子序列是非递增或者非递减排序的。
有一个长度为n的数组A，
把它分成若干排序子序列，
最少可以分为几段排序子序列？

6
1 2 3 2 2 1
2
'''

import sys 

def sub_arrs(arr):
    if not arr: return 0
    count = 1
    if n < 3: return count
    l, i, r = 0, 1, 2
    while i < n:
        while r < n and arr[i] == arr[r]:
            r += 1
        if r == n: break 
        if arr[i] == arr[l]:
            i += 1
        elif (arr[l] < arr[i] and arr[i] > arr[r])or (arr[l] > arr[i] and arr[r] > arr[i]):
            count += 1
        l = i
        i = r
        r += 1
    return count
        
if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    print(sub_arrs(arr))
        
