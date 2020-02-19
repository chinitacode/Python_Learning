# always use the final element of the array as the pivot element
def Median(a,b,c):
    if a < b:
        if b < c:
            return b, 2
        else:
            if a > c:
                return a, 1
            else:
                return c, 3
    else:
        if c > a:
            return a, 1
        else:
            if c > b:
                return c, 3
            else:
                return b, 2

def partition(arr,lo,hi):
    mid = lo + (hi-lo)//2
    m, n = Median(arr[lo],arr[mid],arr[hi])
    if n == 2:
        arr[lo], arr[mid] = arr[mid],arr[lo]
    elif n == 3:
        arr[lo],arr[hi] = arr[hi],arr[lo]
             
    p = lo
    i = lo + 1
    for j in range(i, hi+1):
        if arr[j] < arr[p]:
            if i != j:
                arr[i],arr[j] = arr[j],arr[i]
            i += 1
    arr[p],arr[i-1] = arr[i-1],arr[p]
    return i-1

def quick_sort(arr):
    counter = 0
    def _quick_sort(arr,lo,hi):
        nonlocal counter
        if lo >= hi:
            return
        counter += hi - lo
        pivot_idx = partition(arr,lo,hi)
        _quick_sort(arr, lo, pivot_idx-1)
        _quick_sort(arr, pivot_idx+1, hi)
    _quick_sort(arr, 0, len(arr) - 1)
    print(counter)

if __name__ == '__main__':
    with open('QuickSort.txt') as f:
        arr = list(map(int, f.read().strip().split('\n')))

    quick_sort(arr)
    # 138382
