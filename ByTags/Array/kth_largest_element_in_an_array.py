'''
215. Kth Largest Element in an Array [Medium]
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

[Method 1]: Heap
因为size = k的最小堆的特点就是堆顶为第k大元素（堆里一共k个元素而堆顶是最小的，其他元素都比堆顶大）。
所以我们可以维持一个k个元素的最小堆，即把数列里的元素先加入堆里，当元素个数超过k时，
pop掉堆顶（只需要第k大），最后得到的堆顶元素就是第k大的元素。
[Time]: O(nlogk),因为要遍历n个元素，且在size=k+1的堆里进行pop和push是log(k+1) = O(nlog(k+1)) = O(nlogk)；
[Space]：O(k + 1) = O(k)。
Runtime: 68 ms, faster than 86.30% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Kth Largest Element in an Array.
'''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 0 or k > len(nums): return
        h,n = [],len(nums)
        for num in nums:
            heapq.heappush(h,num)
            if len(h) > k:
                heapq.heappop(h)
        return heapq.heappop(h)

'''
[Method 2]:快速选择 + Random seed
用快速选择巧妙地设置为直接选出符合条件的index，而不是第k大第k小的(比较的时候加一减一的不方便)
[Time]: 平均情况 O(n) + O(logn) = O(n)，最坏情况 O(N^2)。
也可以由主项定理：T(n) = T(n/2) + n，每次都可以分成两个问题，pivot左边和右边，然后选一边继续递归，
所以问题的规模是减半的，最后得T(n) = n。
[Space]: O(1),只是修改数组和传递边界索引。
Runtime: 72 ms, faster than 78.21% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 13.9 MB, less than 30.00% of Python3 online submissions for Kth Largest Element in an Array.
'''
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 0 or k > len(nums): return
        #找index为k的元素
        def select(lo,hi,k): #k-smallest
            if lo == hi:
                return nums[lo]
            #O(n)
            p = partition(lo,hi)
            if p == k:
                return nums[p]
            elif p < k:
                #如果pivot选的好，则只需要遍历一半，O(logn)，类似二分查找的时间复杂度
                return select(p+1,hi,k)
            else:
                #参数仍然为k是因为我们并没切割数组，所以要找的index不变！
                return select(lo,p-1,k)
        #确定升序排列数组的pivot的index
        def partition(lo,hi):
            #random seed
            x = random.randint(lo, hi)
            nums[lo], nums[x] = nums[x], nums[lo]
            p = lo
            i = lo + 1
            for j in range(i, hi+1):
                if nums[j] < nums[p]:
                    if i != j:
                        nums[i],nums[j] = nums[j],nums[i]
                    i += 1
            nums[p],nums[i-1] = nums[i-1],nums[p]
            return i-1
        #找第k大的数，实际上是找升序数组中index为len(nums)-k的数
        return select(0,len(nums)-1,len(nums)-k)


'''
[Method 3]:quick sort + random seed
因为题目是找第k大，则我们用快排修改数组，使其从左到右降序排列，
因为快排的partition方法每一次可以确定pivot的正确位置，
我们在每次确定了pivot的位置时看pivot的index，如果刚好为k-1，则返回；
如果小于k-1，则说明我们还要找更小的元素，那么我们到右边继续找k-pivot_idx-1大，
反之，我们到左边继续找第k大。
【注】这里用到list slicing需要额外的空间和时间，最好还是快速选择pass index。
[Time]: O(n)
[Space]:
Runtime: 72 ms, faster than 78.21% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 13.7 MB, less than 57.50% of Python3 online submissions for Kth Largest Element in an Array.
'''
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 0 or k > len(nums): return
        p = self.partition(nums,0,len(nums)-1)
        if p == k-1:
            return nums[p]
        elif p < k-1:
            return self.findKthLargest(nums[p+1:],k-p-1)
        else:
            return self.findKthLargest(nums[:p],k)

    def partition(self,nums,lo,hi):
        #random seed
        x = random.randint(lo, hi)
        nums[lo], nums[x] = nums[x], nums[lo]
        p = lo
        i = lo + 1
        for j in range(i, hi+1):
            if nums[j] > nums[p]:
                if i != j:
                    nums[i],nums[j] = nums[j],nums[i]
                i += 1
        nums[p],nums[i-1] = nums[i-1],nums[p]
        return i-1


'''
或者快排还是按从小到大升序排列：
Runtime: 68 ms, faster than 86.30% of Python3 online submissions for Kth Largest Element in an Array.
Memory Usage: 13.5 MB, less than 90.00% of Python3 online submissions for Kth Largest Element in an Array.
'''
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k < 0 or k > len(nums): return
        n = len(nums)
        p = self.partition(nums,0,n-1)
        if p == n-k:
            return nums[p]
        elif p < n-k:
            return self.findKthLargest(nums[p+1:],k)
        else:
            return self.findKthLargest(nums[:p],k-n+p)

    def partition(self,nums,lo,hi):
        #random seed
        x = random.randint(lo, hi)
        nums[lo], nums[x] = nums[x], nums[lo]
        p = lo
        i = lo + 1
        for j in range(i, hi+1):
            if nums[j] < nums[p]:
                if i != j:
                    nums[i],nums[j] = nums[j],nums[i]
                i += 1
        nums[p],nums[i-1] = nums[i-1],nums[p]
        return i-1

# Vice Versa:
def findKthSmallest(nums, k):
    return findKthLargest(nums, len(nums) + 1 - k)
