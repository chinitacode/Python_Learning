'''
桶排序，又叫计数排序。类似于抽屉原理。
可以用于1-n中有元素缺失的情况（重复）。

Best      Average    Worst    Memory    Stable      Method        Note
  n        n          n         k         No       Counting       k为duplicates最大个数（抽屉的最大空间）

1、适用于最大值和最小值之差range比较小的时候，和duplicate很多的情况（节省空间）；

2、找出最小值和最大值，为它们和之间的每一个整数设一个抽屉，
即最小值为第一个最大值为最后一个抽屉，抽屉个数为Max - Min + 1,
每个抽屉记录该属于抽屉元素的个数（即duplicate的个数）；

3、最后用一个for循环按抽屉把数排好；

4、时间复杂度全为O(n), 空间复杂度为O(k), 因为最后是in-place排列的，k抽屉个数，
即最大值和最小值之间的范围range, 当range非常大，比如1和100000之间差太多，则空间开销无法想象。

5、不稳定排序。
'''
def bucket_sort(arr):
    #用一个for循环同时找齐最大最小值比分开用min()和max()省一遍遍历
    Min, Max = arr[0], arr[0]
    # O(n)
    for num in range(1,len(arr)):
        if num < Min:
            Min = num
        elif num > Max:
            Max = num
    #桶的个数
    count = Max - Min + 1
    buckets = [0]*count
    #把元素放进桶里 O(n)
    for num in arr:
        buckets[num-Min] += 1

    pos = 0
    #把桶里元素按顺序取出来排好
    # O(n)，因为总共就只需要把n个元素拿出来放好
    for i in range(count):
        for j in range(buckets[i]):
            arr[pos] = Min + i
            pos += 1
