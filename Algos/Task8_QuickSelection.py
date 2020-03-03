'''
[Randomized Selection]
用随机快速选择找出数组A中第i小的数（也就是在排好序的数组A中索引为i-1的数）。
因为只需要找出第i小的数，所以不需要对所有数组进行排序（浪费时间）。
我们可以通过改进快速排序算法来生成快速选择算法。

[Pseudocode]:
Rselect(array A, length n, order statistic i):
    0. if n == 1: return A[0]
    1. choose pivot p from A uniformly at random
    2. partion A around p,
       let j = new index of p (the right index of p)
    3. if j == i: return p
    4. if j > i: return RSelect(lst part of A, length j - 1, i)
    5. if j < i: return RSelect(2nd part of A, length n - j, i - j + 1)

[时间复杂度]：
Worst case: 如果每次pivot都选择最糟糕的情形，Randomized Selection的时间复杂度为n^2。
            假设i=n，每次都选择最小的的元素，那么一共要n次才能找到该元素，
            每次需要的时间为θ(n)，所以一共的时间为θ(n^2)。

Best case: 刚好一次划分后就找到了目标值，所以是O(n)。

average: 同Quick Sort一样，我们应该给出尽可能平衡的划分，最好的pivot是中位数的位置（但因为随机选择pivot无法保证）。
         但毕竟是随机选择，所以很难遇到worst case的情况，因此我们可以假设每次都得划分还是比较平衡，
         又因为我们只需在一部分里继续查找目标值，我们的问题规模每次都会缩小一倍，由主项定理有：
         T(n) = T(n/2) + n, 因为n^(log(b)(a)) < n, 得T(n) = O(n)。

[空间复杂度]：
如果切片，则为O(n), 否则看递归调用次数。
最坏空间复杂度： О(n) total, O(1) auxiliary

[Method 1]: 按照pseudocode
'''
import random
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


def RSelect(arr, k):
    if len(arr) == 1: return arr[0]
    lo, hi = 0, len(arr)-1
    p_idx = random.randint(lo, hi)
    arr[lo], arr[p_idx] = arr[p_idx], arr[lo]
    j = partition(arr,lo,hi)
    if j == k-1:
        return arr[j]
    elif j > k-1: # 目标数在左半部分
        return RSelect(arr[:j], k)
    else:
        return RSelect(arr[j+1:], k-j-1)


'''
[Method 2]: 不用切片
'''
# 找到数组arr中第k小的数 （即如果排好序的话找到索引为k-1的数）
def RSelect2(arr, target):
    # 返回正确（即如果排好序的话）索引为k的数
    def _RSelect(arr, lo, hi, k):
        if lo == hi: return arr[lo]
        p_idx = random.randint(lo,hi)
        arr[lo], arr[p_idx] = arr[p_idx], arr[lo]
        j = partition(arr,lo,hi)
        if j == k:
            return arr[j]
        elif j > k: # 目标数在左半部分
            return _RSelect(arr, lo, j-1, k)
        else:
            return _RSelect(arr, j+1, hi, k) # 因为并没有传入arr的切片，所以k不变
    return _RSelect(arr, 0, len(arr)-1, target-1)


'''
找到数组中前k个最大值并返回：
'''



if __name__ == '__main__':
    arr = [random.randint(1,100) for _ in range(50)]
    print(arr)
    print(RSelect(arr, 25))
    arr.sort()
    print(arr[24])
    print(RSelect([5,2,1,6,3,4,3,4], 3)) # 3

    print(RSelect([0,5,2,1,6,3,4,3,4], 5)) # 3
