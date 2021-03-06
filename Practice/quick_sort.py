'''
[缺点]：
1.不稳定：不稳定性是由随机选择pivot导致，如果每次固定列首为Pivot，则可以实现稳定的快排。

[优点]：
1.Runs O(nlogn) on average
2.Works in place(minimal extral memory needed)

[Key Idea]:
Partition array around a pivot element:
  1.Pick element of the array
  2.Rearrange the array so that :
    -left of pivot: less than pivot
    -right of pivot: greater than pivot
(Partial sorting, without caring about the right order within the two buckets around the pivot)
[Note]: Puts pivot in its "rightful" position.

[Two Cool Facts About Partition]
1.Linear O(n) time, no extra memory;
2.Reduces problem size (only need to sort the left part and the right part of the pivot element,
without combine or merge step).


[Algorithm: High-Level Descrption]:
(Hoare circa 1961)
QuickSort(array, len n)
-base case: if n == 1: return
-p = ChoosePivot(A, n)
-Partition A around p
-Recursively sort 1st part
-Recursively sort 2nd part

[In-place Implementation]:
Assume: pivot = 1st element of array
(if not, swap pivot <==> 1st element as preprocessing step)

High-Level Idea:
-Single scan through array
-Invariant: everything looked at so far is partitioned
 => Needs 2 boundaries, first to keep track of the elements that we've looked at so far and those not yet looked at, which is j;
 and i, for amongst the stuff we've seen, where is the split between those less than the pivot and those greater than it.
  So "j" records delineates the boundary between what we've looked at and what we haven't looked at,
  "i" delineates amongst the stuff we've looked at, where is the boundary between what's bigger than and what's less than the pivot.
  So we want "i" to be just to the left of all the stuff bigger than the pivot.


[Pseudocode for Partition]
Partition(A, l, r)     #l, r are boundaries of subarrays, input = A[l,r+1]
- p = A[l]
- i = l+1
- for j = l+1 to r:
    #if A[j] > p, do nothing
    - if A[j] < p:     #swap the this new element with the left-most element that's bigger than the pivot.
      - swap A[j] and A[i]    #because "i" is keeping track of the boundary between the elements less than the pivot and bigger than the pivot,
      - i += 1             #we can immediately access the leftmost element bigger than the pivot. That's just the "i"th entry in the array.
- swap A[l] and A[i-1]

[Running Time for Partition]:
O(n), where n = r-l+1, the length of the input (subarray)
Reason: O(1) work per array entry. Also, clearly works in place() repeated swap.

[代码执行：]
'''
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
    def _quick_sort(arr,lo,hi):
        if lo >= hi:
            return
        pivot_idx = partition(arr,lo,hi)
        _quick_sort(arr, lo, pivot_idx-1)
        _quick_sort(arr, pivot_idx+1, hi)
    _quick_sort(arr, 0, len(arr) - 1)

if __name__ == "__main__":
    random_list_of_nums = [5, 8, 10, 8, 9, 10, 8]
    print('Before: ',random_list_of_nums)
    quick_sort(random_list_of_nums)
    print('After: ',random_list_of_nums)
    random_list_of_nums = [4,4,2,4,5,6,1,9,4]
    print('Before: ',random_list_of_nums)
    quick_sort(random_list_of_nums)
    print('After: ',random_list_of_nums)
    #Output:
    '''
    Before:  [5, 8, 10, 8, 9, 10, 8]
    After:  [5, 8, 8, 8, 9, 10, 10]
    Before:  [4, 4, 2, 4, 5, 6, 1, 9, 4]
    After:  [1, 2, 4, 4, 4, 4, 5, 6, 9]
    '''

'''
[Time Complexity]：
1.理想情况：如果每次的pivot都为排序后的中位数，就是刚好能把元素分为小于和大于等于它的两部分，
则由T(n) = 2T(n/2) + n ==> T(n) = O(nlogn);
2.但是worst case：当pivot为最小值，并且元素都已经排好序了的情况，如arr=[1,2,3,4,5]
（或者arr = [3,3,3,3,3,3]）,有T(n) = T(n-1) + n = T(n-2) + (n-1) + n = ...
= n(n+1)/2 = n**2, 则是n的平凡的复杂度。所以对pivot的选择需要优化。

[对pivot的选择]：
1.一般可以用三点中值法，即选arr[0],arr[n//2]和arr[-1],找出其中位数的Index就是pivot的index，
把它和列首元素对换就可以开始了；
2.有严格地选取中位数的算法：

'''
def FindMedian(A):
    minvalue = min(A)
    maxvalue = max(A)
    for i in range(3):
        if A[i] != minvalue and A[i] != maxvalue:
            return A[i]

def ChoosePivot(A,flag):
    n = len(A)
    first = A[0]
    final = A[n-1]
    if n/2*2==n:
        k = n/2 - 1
        middle = A[k]
    elif n/2*2<n:
        k = n/2
        middle = A[k]
    else:
        print 'error in ChoosePivot to choose middle element of A'

    B = [first,middle,final]
    med = FindMedian(B)
    if med==B[0]:
        position = 0
    elif med==B[1]:
        position = k
    else:
        position = n-1

    if flag==1:
        return 0
    if flag==2:
        return n-1
    if flag==3:
        return position
    else:
        print 'wrong flag'

def Swap(A,first,second):
    second_value = A[second]
    first_value = A[first]
    A[first] = second_value
    A[second] = first_value
    return A

def Partition(A):
    pivot = A[0]
    r = len(A)
    i = 1
    for j in range(1,r):
        if A[j]<pivot:
            A = Swap(A,i,j)
            i +=1
    A = Swap(A,0,i-1)
    return A,i-1

def QuickSort(A,flag):
    n = len(A)

    if n>1:
        p = ChoosePivot(A,flag)
        A = Swap(A,0,p)
        A,pivot_position = Partition(A)
        A[:pivot_position],left = QuickSort(A[:pivot_position],flag)
        A[pivot_position+1:],right = QuickSort(A[pivot_position+1:],flag)

        return A,left+right+n-1
    else:
        return A,0

'''
[Method 2]: 用栈实现非递归的快排程序
栈里边保存的当然是需要迭代的函数参数，结束条件也是跟需要迭代的参数有关。
对于快速排序来说，迭代的参数是数组的上边界low和下边界high，迭代结束的条件是low == high。
'''
def quick_sort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])

nums = [5, 8, 4, 9, 2, 10, 8]
quick_sort(nums, 0, len(nums)-1)
print(nums)
