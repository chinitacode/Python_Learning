'''
随机挑选pivot元素 更符合实际场景中数组大部分已排好序的场景(不易退化为O(n^2)复杂度).
但产生随机数的过程会增加时间消耗,有相应的解决方法(如,提前生成一张随机表,每次在表中选取实现伪随机)
[写法一]：
'''
import random

# # always use the first element of the array as the pivot element
def quicksort(arr):
    # # 返回pivot index的同时也给arr in-place排序了（mutate arr，虽然只是给pivot安置好了位置）
    def partition(arr,lo,hi):
        p_idx = lo
        i = lo + 1
        for j in range(i, hi+1):
            if arr[j] < arr[p_idx]:
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i-1], arr[p_idx] = arr[p_idx], arr[i-1]
        return i-1

    def quick_sort(arr, lo, hi):
        if lo >= hi:
            return
        rand = random.randint(lo,hi)
        arr[lo], arr[rand] = arr[rand], arr[lo]
        p_idx = partition(arr, lo, hi)
        quick_sort(arr, lo, p_idx-1)
        quick_sort(arr, p_idx+1, hi)
    quick_sort(arr, 0, len(arr)-1)
    return arr #因为是in-place sorting,可以不return

'''
[写法二]
排序数组为a,游标left从a的最左边开始,游标right从最右边开始
把pivot记为数组第一个数(即a[left]),作为数组左右的分界值
从右边开始向左移动游标(right = right - 1)直到找到第一个小于pivot的数,存储在a[left]当中
从左边开始向右移动游标(left = left + 1)直到找到第一个大于pivot的数,存储在a[right]当中
重复上述两步直到两个游标相遇
将pivot放置到a[left]位置上
随后递归地将pivot左右两部分分别排序
'''
def ranqsort(a, low, high):
    if low < high:
        l, r = low, high
        #random and swap
        rand = random.randint(low,high)
        a[rand], a[l] = a[l], a[rand]
        p = a[l]
        while l < r:
            while l < r and a[r] >= p:
                r -= 1
            a[l] = a[r]
            while l < r and a[l] <= p:
                l += 1
            a[r] = a[l]
        a[l] = p
        ranqsort(a, low, l-1)
        ranqsort(a, l+1, high)



'''
[更pythonic一点的写法]:
这种方式应该更加直观便捷,几乎看代码就能直到排序原理,而且使用了python中列表生成式这个特性,
但是从空间复杂度上,增加了额外开销存储数组.时间复杂度上应该是2倍于方法1,但是仍可视为是O(NlogN)
'''
def pythonicqs(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        pivots = [n for n in a if n == pivot]
        return pythonicqs([n for n in a if n < pivot]) + pivots + pythonicqs([n for n in a if n > pivot])

'''
[算法导论上对于快排的实现]:
算是一个聪明又方便的方式. 主要区别在于取最左端做主元(pivot)改为取最右端做主元.
'''
def algqsort(a, l ,r):
    if l < r:
        p = a[r]
        i = l - 1
        for j in range(l,r):
            if a[j] <= p:
                i += 1 # i标志从左往右数<=p的最右数的索引
                a[i],a[j] = a[j], a[i] #未找到右边起第一个大于p的数之前,i==j 相当于不改变
        i += 1
        a[i],a[r] = a[r],a[i] # 安置好p的位置
        algqsort(a,l,i-1)
        algqsort(a,i+1,r)


if __name__ == "__main__":
    random_list_of_nums = [5, 8, 10, 8, 9, 10, 8]
    print('Before: ',random_list_of_nums)
    quicksort(random_list_of_nums)
    print('After: ',random_list_of_nums)
    random_list_of_nums = [4,4,2,4,5,6,1,9,4]
    print('Before: ',random_list_of_nums)
    quicksort(random_list_of_nums)
    print('After: ',random_list_of_nums)
    print(quicksort([random.randint(1,100) for _ in range(100)]))

    print(pythonicqs([random.randint(1,100) for _ in range(100)]))


    arr = [random.randint(1,100) for _ in range(100)]
    ranqsort(arr, 0, 99)
    print(arr)

    arr = [random.randint(1,100) for _ in range(100)]
    algqsort(arr, 0, 99)
    print(arr)

    # with open('QuickSort.txt') as f:
    #     arr = list(map(int, f.read().strip().split('\n')))
    # quicksort(arr)
