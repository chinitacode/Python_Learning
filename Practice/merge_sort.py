'''
[Time]: O(nlogn)
[分析1]：先拆分，从上到下把n拆分到1，一共需要拆(logn+1)次，
然后从下到上排序合并，从1到n，共(logn+1)层，每层需要排n个元素，一共用时n(logn+1),
所以一共用时O(logn+1+n(logn+1)) = O(nlogn)

[分析2]:
递归式：T(n) = 2T(n/2) + n,
这里a = 2, 表示每次把问题拆分成a个子问题，
b = 2, 表示每个子问题的Input size为原问题的1/b，
c = n, 表示解决每个子问题需要n时间,这是因为在MergeSort中尽管input被分割成了全为1的子问题，
合并的时候都需要先两两排好序，用时加起来也为n。
如数列[3,2,5,1,6,4], 在从下往上合并时假设进行到最后一步，合并[2,3,5]和[1,4,6],则明显用时n，
因为需要左右两个数列逐数比较、排序、合并。
根据主项定理有：
n^(logb(a)) = n^(log2(2)) = n,
f(n) = n,
所以O(n) = nlogn。

[分析3]:
也可根据递归式：T(n) = 2T(n/2) + n画一课递归树，
假设解决最后的子问题用时为常数c，则对于n个待排记录来说整个问题的规模为cn。
                                                           用时
                        cn                 第0层            cn
                    /       \
                cn/2        cn/2           第1层            cn/2 + cn/2 = cn
               /   \        /   \
            cn/4  cn/4    cn/4  cn/4       第2层            cn/4 + cn/4 + cn/4 + cn/4 = cn
            /  \   / \     / \   / \
           c    c c   c   c   c c   c      第(logn+1)层     ... = cn

         递归总用时: cn * (logn+1)
'''

def merge_sort(arr):
    if len(arr) > 1:
        #Finding the mid of the array
        mid = len(arr) // 2
        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)
        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
