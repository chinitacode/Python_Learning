'''
Best      Average    Worst    Memory    Stable      Method        Note
n          n^2        n^1.3       1         No       Selection

1. 希尔排序(Shell's Sort)是插入排序的一种又称“缩小增量排序”（Diminishing Increment Sort），
是直接插入排序算法的一种更高效的改进版本。
希尔排序是非稳定排序算法。 该方法因D.L.Shell于1959年提出而得名。

2.选择排序在n比较小的时候速度比较快，但当n很大时，可以拆分为很多小数组来进行插入排序；

3.希尔排序是按照不同步长对元素进行插入排序，当刚开始元素很无序的时候，步长最大，
所以插入排序的元素个数很少，速度很快；
当元素基本有序了，步长很小， 插入排序对于有序的序列效率很高。
所以，希尔排序的时间复杂度会比O(n^2)好一些。

4.不稳定性：
由于多次插入排序，我们知道一次插入排序是稳定的，不会改变相同元素的相对顺序，
但在不同的插入排序过程中，相同的元素可能在各自的插入排序中移动，
最后其稳定性就会被打乱，所以shell排序是不稳定的。
'''
def shellSort(arr):
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n//2

    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
        for i in range(gap,n):
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2

if __name__ == '__main__':
    # Driver code to test above
    arr = [ 12, 34, 54, 2, 3]

    n = len(arr)
    print ("Array before sorting:")
    print(arr)

    shellSort(arr)

    print ("\nArray after sorting:")
    print(arr)
