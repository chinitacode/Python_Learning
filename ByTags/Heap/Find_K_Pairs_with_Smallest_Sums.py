'''
373. Find K Pairs with Smallest Sums [Medium]

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:
Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence:
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:
Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence:
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:
Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

[Method 1]: Min Heap
因为两个数组都是排好序的，我们可以维持一个最小堆，
先将由两个数组index i,j为0的元素组成的pair放进去（即最小和pair），然后把它右边和下边的那对也加进去。
如果右边的pair要小于下面的pair，即最小堆堆顶，那么被pop出来后又把右边的pair补进堆。
因为之前下面的pair（即(0,1)）是存在在堆里的，每次为了维持最小堆的特性，
新加进去的右边的那对都会和(0,1)比较，如果右边一直较小，则右边的元素加完后会把(0,1)也pop出来，
然后这个时候的j是为0的，所以又要把右边和下面同时加进堆，继续重复之前的步骤。
[Time]: O(k*log2) = O(k), 一次最多加两个pair进堆，而且每次还要pop一个pair进输出的pairs，
所以最小堆最多维持两个pair，所以堆操作都是log2。
[Space]: O(1)。
Runtime: 48 ms, faster than 92.23% of Python3 online submissions for Find K Pairs with Smallest Sums.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Find K Pairs with Smallest Sums.
'''
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or not k: return []
        minHeap = [(nums1[0]+nums2[0],0,0)]
        pairs = []
        while minHeap and len(pairs) < k:
            _,i,j = heapq.heappop(minHeap)
            pairs.append([nums1[i],nums2[j]])
            #一次最多加两个元素进最小堆
            if i < len(nums1) and j + 1 < len(nums2):
                heapq.heappush(minHeap,(nums1[i]+nums2[j+1],i,j+1))
            if j == 0 and i+1 < len(nums1):
                heapq.heappush(minHeap,(nums1[i+1]+nums2[j],i+1,j))
        return pairs
