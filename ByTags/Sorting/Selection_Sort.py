'''
Best      Average    Worst    Memory    Stable      Method        Note
n^2        n^2        n^2       1         No       Selection

1.选择排序是给每个位置选择当前元素最小的，记住其索引index为Min，每第i次遍历完后与index i-1的元素互换；
比如给第一个位置选择最小的，在剩余元素里面给第二个元素选择第二小的，依次类推，
直到第n - 1个元素，第n个元素不用选择了，因为只剩下它一个最大的元素了。

2. 不稳定排序：
在一趟选择里，如果当前元素比一个元素小，而该小的元素又出现在一个和当前元素相等的元素后面，
那么交换后稳定性就被破坏了。
比较拗口，举个例子，序列 5 8 5 2 9，我们知道第一遍选择第1个元素5会和2交换，
那么原序列中2个5的相对前后顺序就被破坏了，所以选择排序不是一个稳定的排序算法。

3.O(1)的额外空间（也是in-place）;

4.O(n^2)对比；

5.O(n)互换；

6.费适应性；即没有最好或者最坏的case, 永远O(n^2)的时间复杂度；

'''
def selection_sort(arr):
    for i in range(len(arr)-1):
        Min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[Min]:
                Min = j
        arr[Min],arr[i] = arr[i],arr[Min]

if __name__ == '__main__':
    arr1 = [5,4,3,2,1]
    arr2 = [6,7,8,2,8,2,1]
    print('Before sorting:\n')
    print('arr1: ', arr1, '\n')
    selection_sort(arr1)
    print('After sorting:\n')
    print('arr1: ', arr1, '\n')
    print('Before sorting:\n')
    print('arr2: ', arr2, '\n')
    selection_sort(arr2)
    print('After sorting:\n')
    print('arr2: ', arr2, '\n')
