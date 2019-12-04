'''
Best      Average    Worst    Memory    Stable     Method     Note
n          n^2        n^2       1         Yes       Swap      n小时较好

1、重复列表比较每对相邻的元素，如果它们的顺序错误，则交换它们；

2、比较是相邻的两个元素比较，交换也发生在这两个元素之间；

3、在每次通过时，未排序的最大元素已经被“冒泡”到阵列末端的合适位置；

4、重复直到不需要交换，这表明列表已被排序（可以设一个标志位）

5、稳定排序算法。
如果两个元素相等，我想你是不会再无聊地把他们俩交换一下的；
如果两个相等的元素没有相邻，那么即使通过前面的两两交换把两个相邻起来，这时候也不会交换，
所以相同元素的前后顺序并没有改变，所以冒泡排序是一种稳定排序算法。

[属性]:
-稳定排序；
-O(1)的额外空间；
-O(n^2)的比较和交换；
-适应性： O(n)接近排序时；
'''
# 最普通的写法（最费时）
# O(n^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]

#最好的情况是当arr接近排好序时，只需要一个遍历维持is_sorted为True就可以返回，为O(n);
#最坏的情况是当arr刚好反向排好序，则需要O(n^2);
def bubble_sort2(arr):
    n = len(arr)
    for i in range(n-1):
        is_sorted = True
        for j in range(1, n-i):
            if arr[j-1] > arr[j]:
                is_sorted = False
                arr[j-1],arr[j] = arr[j],arr[j-1]
        if is_sorted: return

if __name__ == '__main__':
    arr1 = [5,4,3,2,1]
    arr2 = [6,7,8,2,8,2,1]
    print('Before sorting:\n')
    print('arr1: ', arr1, '\n')
    bubble_sort2(arr1)
    print('After sorting:\n')
    print('arr1: ', arr1, '\n')
    print('Before sorting:\n')
    print('arr2: ', arr2, '\n')
    bubble_sort2(arr2)
    print('After sorting:\n')
    print('arr2: ', arr2, '\n')
