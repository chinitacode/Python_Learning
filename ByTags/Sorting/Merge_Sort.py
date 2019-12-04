'''
Best      Average    Worst    Memory    Stable      Method        Note
nlogn       nlogn    nlogn      O(n)      Yes       Selection     n大时较好

1、把序列递归地分成短序列，递归出口是短序列只有1个元素(认为直接有序)或者2个序列(1次比较和交换),
然后把各个有序的短序列合并成一个有序的长序列，不断合并直到原序列全部排好序；

2、合并过程中我们可以保证如果两个当前元素相等时，我们把处在前面的序列的元素保存在结果序列的前面，这样就保证了稳定性；

3、稳定排序算法；

4、空间复杂度 O(n);
n + logn = 临时的数组和递归时压入栈的数据占用的空间；所以空间复杂度为: O(n)。
'''

def merge_sort(arr):
    if len(arr) <= 1: return
    # list slicing making new copies of arr, using extra space
    l, r = arr[:len(arr)//2], arr[len(arr)//2:]
    merge_sort(l)
    merge_sort(r)
    # merging process
    i = j = k = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    # complet filling arr, 因为最后总会剩下l或者r的元素（最大的几个元素）
    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1
    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

if __name__ == '__main__':
    random_list_of_nums = [5, 8, 10, 8, 9, 10, 8]
    print('Before: ',random_list_of_nums)
    merge_sort(random_list_of_nums)
    print('After: ',random_list_of_nums)
    random_list_of_nums = [4,4,2,4,5,6,1,9,4]
    print('Before: ',random_list_of_nums)
    merge_sort(random_list_of_nums)
    print('After: ',random_list_of_nums)
