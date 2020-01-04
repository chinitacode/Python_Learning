# always use the first element of the array as the pivot element
def partition(arr,lo,hi):
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
        global counter
        if lo >= hi:
            return
        pivot_idx = partition(arr,lo,hi)
        _quick_sort(arr, lo, pivot_idx-1)
        _quick_sort(arr, pivot_idx+1, hi)
        counter += hi - lo
    _quick_sort(arr, 0, len(arr) - 1)
    print(counter)

if __name__ == '__main__':
    with open('QuickSort.txt') as f:
        arr = list(map(int, f.read().strip().split('\n')))
    quick_sort(arr)
