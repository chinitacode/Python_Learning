'''
378. Kth Smallest Element in a Sorted Matrix [Medium]
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order,
not the kth distinct element.

Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.


[Method 1]: heap 小顶堆
因为是找第k小，所以我们可以遍历矩阵每个数来维持一个size为k的最大堆，
则堆顶元素就是第k小（因为其他元素都大于它），最后返回堆顶即可。

【注】因为此法需要遍历所有元素，所以实际上更适用于无序矩阵。

[Time]: O(n^2logk),因为需要遍历整个nxn矩阵，而在size为k的堆里push和pop都是logk的；
如果k为n^2，则时间复杂度就变成了O(n^3),并非最好的选择。
[Space]: O(K+1) = O(k), 堆所占用的额外空间。

Runtime: 204 ms, faster than 76.56% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.7 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
'''
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]: return
        n = len(matrix)
        if k < 0 or k > n**2: return
        h = []
        for row in range(n):
            for col in range(n):
                heapq.heappush(h,-matrix[row][col])
                if len(h) > k:
                    heapq.heappop(h)
        return -heapq.heappop(h)


'''
[Method 2]: heap 小顶堆
方法1的改进版。
因为题目说了矩阵每行每列都是升序的，所以我们如果把每一行的最小值汇在一起，
其中最小一个必定是矩阵的最小值，也就是第1小的值。
如果取走这个元素后，我们再把这个元素在该行的下一个元素加进去比较，最小的值就是第2小的，
依次类推......直到找到第k小的值。所以我们只需要维持一个size为n的小顶堆，遍历k次。
但是为了跟踪下一个要加入堆的元素，我们需要记录每个元素的位置和在该行的下一个元素的位置，
所以堆里面储存的是一个个包含了该元素和该元素的位置的一个list。
[Time]: O(klogn), 最坏是当k为n^2是，即O(n^2*logn)。
[Space]: O(3n) = O(n)
Runtime: 224 ms, faster than 58.52% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.6 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
'''
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]: return
        n = len(matrix)
        if k < 0 or k > n**2: return
        h = [[matrix[row][0], row, 0] for row in range(n)]
        heapq.heapify(h)
        while k > 0:
            num,i,j = heapq.heappop(h)
            if j + 1 < n:
                heapq.heappush(h,[matrix[i][j+1],i,j+1])
            k -= 1
        return num


'''
[Method 3]: 二分法
1.找出二维矩阵中最小的数left，最大的数right，那么第k小的数必定在left~right之间
2.mid=(left+right)//2；在二维矩阵中寻找小于等于mid的元素个数count(可以用bisect.bisect())
3.若这个count小于k，表明第k小的数在右半部分且不包含mid，即left=mid+1, right=right，又保证了第k小的数在left~right之间
4.若这个count大于等于k，表明第k小的数在左半部分且可能包含mid，即left=left, right=mid，又保证了第k小的数在left~right之间
5.因为每次循环中都保证了第k小的数在left~right之间，当left==right时，第k小的数即被找出，等于right
比如数组为:

[[1,2],
[12,100]]
k = 3
那么刚开始 left = 1, right = 100, mid = 50, 遍历完 cnt = 3，此时 right 更新为 50
此时 left = 1, right = 50, mid = 25, 遍历完之后 cnt = 3, 此时 right 更新为 25
此时 left = 1, right = 25, mid = 13, 遍历完之后 cnt = 3, 此时 right 更新为 13
此时 left = 1, right = 13, mid = 7, 遍历完之后 cnt = 2, 此时 left 更新为8
此时 left = 8, right = 13, mid = 10, 遍历完之后 cnt = 2, 此时 left 更新为 11
此时 left = 11, right = 12, mid = 11, 遍历完之后 cnt = 2, 此时 left 更新为 12
循环结束，left 和 right 均为 12，任意返回一个即可。

[Time]: O(nlognlog(max-min))
[Space]: O(1)
'''
class Solution(object):
    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo<hi:
            mid = (lo+hi)//2
            if sum(bisect.bisect_right(row, mid) for row in matrix) < k:
                lo = mid+1
            else:
                hi = mid
        return lo


'''
[Method 4]: 二分法的改进 【最优解】
因为每行每列都是排好序的，所以对于一个位于非边界的元素，比它小的有向上向左两种方向，
比它大的有向右向下两种方向，比较起来比较麻烦。但是对于边界元素，如最后一行的第一个元素，
要找比它小的元素只有往上遍历，找比它大的只能往右遍历，所以这样下来worst case的时间复杂度也就(m + n),
即最多需要遍历 m + n 个元素，所以搜索小于等于mid的元素的个数只需要O(2n) = O(n),
而之前用Bisect要O(nlogn)，明显更耗时。
[Time]: O(nlog(max-min))
[Space]: O(1)
Runtime: 160 ms, faster than 99.87% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
Memory Usage: 18.6 MB, less than 9.09% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]: return
        n = len(matrix)
        if k < 0 or k > n**2: return
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:
            mid = lo + (hi - lo) // 2
            count = self.search_lower_equal_than_mid(matrix, mid)
            if count < k:
                lo = mid+1
            else:
                hi = mid
        return hi

    def search_lower_equal_than_mid(self,matrix, mid):
        n = len(matrix)
        i, j = n - 1, 0
        cnt = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                j += 1
                cnt += i + 1
            else:
                i -= 1
        return cnt


'''
关于为什么二分法最后返回的hi一定在矩阵里：
因为矩阵里的数全部都是整数，我们lo和hi只是不断地缩小限定第k小的值的取值范围，
只要保证第K小的数在lo和hi之间，不停缩小lo和hi直到lo==hi时，最终第K小的数就是lo也就是hi。

当count(mid) < k,也就是说我们找到的范围中位数在矩阵里，小于等于它(mid)的数使少于k的，
所以k绝对不可能在左边，且不包含mid，因为count还包括了等于mid的数，即mid如果真的存在于矩阵中的话，
mid前面的数包括mid都不够k个，所以我们把左边界改进为lo = mid+1；
反之，当count(mid) >= k的时候，也就是说包含mid在内的元素的个数是符合k所在的条件的，
那么进一步限定hi = mid，这里得包含mid，因为有可能mid存在且重复。

如矩阵[[1,7],[8,9]], k = 2
用NO和YES来标记满足的取值区间，取值范围为：
    lo                      *            hi
    1   2   3   4   5   6   7   8   9   10
    NO  NO  NO  NO  NO  NO  YES YES YES YES

所以最终返回的lo(或者hi)是一定在矩阵里，才能满足以上的条件。
'''
