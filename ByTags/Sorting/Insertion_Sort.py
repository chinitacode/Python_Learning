'''
Best      Average    Worst    Memory    Stable      Method        Note
  n        n^2        n^2       1         Yes       Insertion

[直接插入排序]
1、已经有序的小序列的基础上，一次插入一个元素；刚开始这个有序的小序列只有1个元素，就是第一个元素。
移动的次数为n-1(从index=1开始遍历)。

2、比较是从有序序列的末尾开始，即想要插入的元素和已经有序的最大者开始比起，
如果比它大则直接插入在其后面（停止比较），否则一直往前找直到找到它该插入的位置，
即，每次对正确的位置进行O(n)的线性搜索，并且边搜索边交换（插入）元素；

3、稳定排序算法，如果碰见一个和想插入元素相等的，那么插入元素把想插入的元素放在相等元素的后面（不动），
所以，相等元素的前后顺序没有改变，以保障稳定的排序算法；

4、O(1)的空间，in-place;

5、平均O(n^2)的时间复杂度，
   最坏O(n^2), 如果每个待插元素都比已排好的元素小（比如逆序排好的数列），
   最好O(n), 当数列接近排好序时。

6、当n比较少的时候，插入排序的速度（从纯粹的运行时间来说，但是复杂度都一样）明显优于冒泡和选择，虽然都是O(n^2),
因为后两者每次移动都必须要把所有的元素全部比较完才能定一个元素的位置（冒泡找最大值并移动到末位，
选择排序找最小值并往前移，因此每一次移动都是O(n)的时间成本），但是插入排序就不需要，
因为是从后往前比，所以如果是已经排好序了就只需要和排好序的最大的元素比较那么1次就可以下一次移动了。
如 [1,2,2,5,6]，基本上里层循环是用不到的，所以best case的时间复杂度为O(n)。

'''
def insertion_sort(arr):
    # i 为下一个待排序的数字的索引
    for i in range(1, len(arr)):
        # 从已经拍好序的元素的最后一位开始往前比大小，如果小就交换
        pos = i
        while pos > 0 and arr[pos] < arr[pos-1]:
            arr[pos], arr[pos-1] = arr[pos-1], arr[pos]
            pos -= 1


'''
[折半插入排序 Binary Insertion Sort]

Best      Average    Worst    Memory     Stable       Method        Note
nlogn       n^2        n^2       1         Yes       Insertion

1.每次对正确的位置进行线性搜索，而是进行二分搜索，这是O(logn)而不是O(n);

2.但是用O(logn)找到位置后，还需要将元素插进去，由于数组的空间是连续的，所以插入的成本近似O(n),
因此每一次把元素插入到其正确位置的时间成本仍然是O(n),但是实际上还是会稍微快于直接插入;

3.唯一的问题是，即使元素处于当前位置，也必须执行二分搜索；

4.平均和最坏的情况都是O(logn);

5.最优情况可以达到O(nlogn)，当要插入的元素位于已排好的列表的右半部分时（这样插入的时间成本小于O(n/2)，
近似于O(logn),则总时间成本近似O(nlogn)）;

6.O(1)的时间复杂度；

7.稳定；
'''
def binary_search(arr, val, start, end):
    # we need to distinugish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1

    # this occurs if we are moving beyond left's boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if start > end:
        return start

    mid = (start+end)/2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

def bi_insertion_sort(arr):
    for i in xrange(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:] #Slicing, O(n), 最好用循环来swap元素，不然任何时候都是O(n^2),达不到O(nlogn的最优)
    return arr

 if __name__ == '__main__':
     print("Sorted array:")
     print bi_insertion_sort([37, 23, 0, 17, 12, 72, 31, 46, 100, 88, 54])
