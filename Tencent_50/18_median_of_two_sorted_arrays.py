'''
4. Median of Two Sorted Arrays [Hard]
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
'''

'''
O(log(min(m,n))
It's guaranteed to be O(log(min(m,n)) because every time the findKth function cuts the shorter array by half of its size.
Runtime: 108 ms, faster than 70.76% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 13.9 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.
首先我们来看如何找到两个数列的第k小个数，即程序中getKth(A, B , k)函数的实现。
用一个例子来说明这个问题：A = {1，3，5，7}；B = {2，4，6，8，9，10}；
如果要求第7个小的数，A数列的元素个数为4，B数列的元素个数为6；
我们可以通过对比A和B的k/2位的大小来排除一些元素：k/2 = 7/2 = 3，
而A中的第3个数A[2]=5；B中的第3个数B[2]=6；而A[2]<B[2]；
则A[0]，A[1]，A[2]中必然不可能有第7个小的数。
因为A[2]<B[2]，所以比A[2]小的数最多可能为A[0], A[1], B[0], B[1]这四个数，
也就是说A[2]最多可能是第5个大的数，由于我们要求的是getKth(A, B, 7)；
现在就变成了求getKth(A', B, 7-(2+1))；即A' = {7}；B不变，求这两个数列的第4个小的数。
因为A[0]，A[1]，A[2]中没有解，所以我们直接删掉它们就可以了。这个可以使用递归来实现。
'''
class Solution:
    def getKth(self, A, B, k):
        lenA = len(A); lenB = len(B)
        if lenA > lenB: return self.getKth(B, A, k)
        if lenA == 0: return B[k - 1]
        if k == 1: return min(A[0], B[0])
        pa = min(k//2, lenA); pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenA = len(nums1); lenB = len(nums2)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(nums1, nums2, (lenA + lenB)//2 + 1)
        else:
            return (self.getKth(nums1, nums2, (lenA + lenB)//2) + self.getKth(nums1, nums2, (lenA + lenB)//2 + 1)) * 0.5


#或更严格来说的二分法写法(比较A和B里面中位数的大小来减小K)：
class Solution:
    def findMedianSortedArrays(self, A, B):
        l = len(A) + len(B)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2 , len(b) // 2
        ma, mb = a[ia], b[ib]

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)

'''
[Note]
The slice operation for list is o(k). So as we are using a[:ia] & a[ia+1:], these operations are really o(n)/o(m).
Thus we cannot use slice operations but pass start/end index is the solution.
'''
class Solution:
    def find(self, nums1, s1, e1, nums2, s2, e2, k):
        if e1 - s1 < 0:
            return nums2[k + s2]
        if e2 - s2 < 0:
            return nums1[k + s1]
        if k < 1:
            return min(nums1[k + s1], nums2[k + s2])
        ia, ib = (s1 + e1) // 2 , (s2 + e2) // 2
        ma, mb = nums1[ia], nums2[ib]
        if (ia - s1) + (ib - s2) < k:
            if ma > mb:
                return self.find(nums1, s1, e1, nums2, ib + 1, e2, k - (ib - s2) - 1)
            else:
                return self.find(nums1, ia + 1, e1, nums2, s2, e2, k - (ia - s1) - 1)
        else:
            if ma > mb:
                return self.find(nums1, s1, ia - 1, nums2, s2, e2, k)
            else:
                return self.find(nums1, s1, e1, nums2, s2, ib - 1, k)

    def findMedianSortedArrays(self, nums1, nums2):
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2)
        else:
            return (self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2) + self.find(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, l // 2 - 1)) / 2.0
18

'''
O(m+n)
Runtime: 124 ms, faster than 13.60% of Python3 online submissions for Median of Two Sorted Arrays.
Memory Usage: 14.2 MB, less than 5.71% of Python3 online submissions for Median of Two Sorted Arrays.
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if not nums1:
            return self.find_median(nums2)
        elif not nums2:
            return self.find_median(nums1)
        else:
            arr = self.merge(nums1, nums2)
            return self.find_median(arr)

    def find_median(self, arr):
        if len(arr) % 2:
            return float(arr[len(arr)//2])
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1]) / 2

    def merge(self, arr1, arr2):
        arr = [0] * (len(arr1) + len(arr2))
        i = j = k = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else:
                arr[k] = arr2[j]
                j += 1
            k += 1
        while i < len(arr1):
            arr[k] = arr1[i]
            i += 1
            k += 1
        while j < len(arr2):
            arr[k] = arr2[j]
            j += 1
            k += 1
        return arr
