'''
347. Top K Frequent Elements [Medium]

Given a non-empty array of integers,
return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

[Method 1]: 字典+排序
用一个字典统计每个元素出现的频次，再根据其频次降序排列。

[Time]: The worst case is O(n + nlgn) = O(nlgn) when there are no duplicate numbers.
[Space]: O(n)
Runtime: 88 ms, faster than 81.10% of Python online submissions for Top K Frequent Elements.
Memory Usage: 15.5 MB, less than 17.07% of Python online submissions for Top K Frequent Elements.
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if not nums or k > len(nums) or k < 1:
            return []
        res = []
        mydict = {}
        for i in range(0, len(nums)):
            mydict[nums[i]] = mydict.get(nums[i], 0) + 1
        sort = sorted([(key, val) for key, val in mydict.items()], key = lambda x: x[1], reverse=True)
        return [e[0] for e in sort[:k]]


'''
还可以用冒泡排序
不再全局排序，只对最大的k个排序。
冒泡是一个很常见的排序方法，每冒一个泡，找出最大值，冒k个泡，就得到TopK。

伪代码：

for(i=1 to k){
         bubble_find_max(arr,i);
}
return arr[1, k];

[时间复杂度]：O(n*k)


[Method 2]: 字典+桶排序（箱排序）
桶排序：
找出所有数取值的范围，给每个数一个桶（初始为0），根据数列里的数使其代表的桶表示它出现的次数。
如数列[3,2,5,2,8]，最小值为2，最大值为8，则中间取值范围有7个数，从2到8，
所以我们创建Bucket = [0]*7
然后从第一个数3开始，使得bucket[3-2] += 1
bucket[2-2] += 1, bucket[5-2] += 1...最后得到bucket = [2,1,0,1,0,0,1]
然后按顺序输出每个index+2,次数为bucket[i],
即：2,2,3,5,8

但是这里我们把每个桶设置为[]，
不同的桶代表不同的出现次数，
然后把每个数添加到桶里。
当添加的数够k时，返回前k个数即可。

[注意！！！]：
>>> [[]*8]
[[]]
>>> [[] for _ in range(8)]
[[], [], [], [], [], [], [], []]
>>>

[Time]: O(n)
[Space]: O(n)
Runtime: 100 ms, faster than 27.85% of Python online submissions for Top K Frequent Elements.
Memory Usage: 18.9 MB, less than 7.32% of Python online submissions for Top K Frequent Elements.
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k > len(nums) or k < 1:
            return []
        bucket = [[] for _ in range(len(nums))]
        mydict, res = {}, []
        for i in range(len(nums)):
            #记录每个数出现的频率
            mydict[nums[i]] = mydict.get(nums[i], 0) + 1
        for num, freq in mydict.items():
            #取负index，以便于最后输出时freq顺序减小
            #freq之和是为len(nums),所以一定在有效index的范围内。而因为取负index，所以出现次数越多的，其index越小，排越前面。
            bucket[-freq].append(num)
        for j in range(len(bucket)):
            res += bucket[j]
            if len(res) >= k: return res[:k]

'''
#Or:
itertools.chain('ABC', 'DEF') --> A B C D E F
>>> bucket = [[3],[5],[6]]
>>> list(itertools.chain(*bucket))
[3, 5, 6]
>>>
Runtime: 100 ms, faster than 27.85% of Python online submissions for Top K Frequent Elements.
Memory Usage: 19.5 MB, less than 7.32% of Python online submissions for Top K Frequent Elements.
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        bucket = [[] for _ in nums]
        for num, freq in collections.Counter(nums).items():
            bucket[-freq].append(num)
        return list(itertools.chain(*bucket))[:k]

'''
[Method 3]:堆
堆将冒泡的TopK排序优化为了TopK不排序，节省了计算资源。堆是求TopK的经典算法。

对于海量数据，我们不需要一次性将全部数据取出来，可以一次只取一部分，因为我们只需要将数据一个个拿来与堆顶比较。

另外还有一个优势就是对于动态数组，我们可以一直都维护一个 K 大小的小顶堆，
当有数据被添加到集合中时，我们就直接拿它与堆顶的元素对比。这样，无论任何时候需要查询当前的前 K 大数据，我们都可以里立刻返回给他。

整个操作中，遍历数组需要 O(n) 的时间复杂度，一次堆化操作需要 O(logK)，加起来就是 O(nlogK) 的复杂度，
换个角度来看，如果 K 远小于 n 的话， O(nlogK) 其实就接近于 O(n) 了，甚至会更快，因此也是十分高效的。

[最小堆]
题目最终需要返回的是前 k 个频率最大的元素，
可以想到借助堆这种数据结构，对于 k 频率之后的元素不用再去处理，进一步优化时间复杂度。

先用前k个元素生成一个小顶堆，这个小顶堆用于存储，当前最大的k个元素。
接着，从第k+1个元素开始扫描，和堆顶（堆中最小的元素）比较，如果被扫描的元素大于堆顶，
则替换堆顶的元素，并调整堆，以保证堆内的k个元素，总是当前最大的k个元素。
直到，扫描完所有n-k个元素，最终堆中的k个元素，就是求的TopK。

[Time]: O(nlogk)，n 表示数组的长度。
n个元素扫一遍，假设运气很差，每次都入堆调整，调整时间复杂度为堆的高度，即lg(k)，故整体时间复杂度是n*lg(k)。
所以这一系列操作的时间复杂度是 O(nlogk) 的；因此，总的时间复杂度是 O(nlog⁡k)。
[Space]：O(n)，最坏情况下（每个元素都不同），map 需要存储 n 个键值对，优先队列需要存储 k 个元素，因此，空间复杂度是O(n)。
Runtime: 104 ms, faster than 76.77% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 17.3 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
'''
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k < 0: return []
        if len(nums) == k: return nums
        counts = collections.Counter(nums) # O(n)
        freqs = [(freq, num) for num,freq in counts.items()] # O(n)
        top_k_freqs = freqs[:k] # O(k)
        heapq.heapify(top_k_freqs) # O(k)
        for i in range(k,len(freqs)):  # O((n-k)*logk)
            if freqs[i][0] > top_k_freqs[0][0]:
                heapq.heapreplace(top_k_freqs,freqs[i])
        return [freq[1] for freq in top_k_freqs]

'''
[最大堆]
Uses a dict to maintain counts, heapifys the list of counts,
then selects K elements out of the max heap.
[Time]: O(n + klogn)
Runtime: 112 ms, faster than 37.64% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 17.3 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.

'''
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        freq_list=[]
        #O(n)
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
        for key in freq:
            freq_list.append((-freq[key], key)) #Generate a Max Priority Queue
        heapq.heapify(freq_list) # O(n)
        topk = []
        #O(klogn)
        for i in range(k):
            #O(logn)
            topk.append(heapq.heappop(freq_list)[1]) # O(logn)
        return topk

# or:
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


'''
[Method 4]: 快速选择
Use a dictionary to get the frequencies,
and then used quick select to get the top k frequenct elements.

如果我们直接在原序列上进行快速选择，则会打乱原来序列中元素的位置。
如果不想打乱元素的位置，可以拷贝临时的一份作为快速选择的序列。

[code 1]: use list slicing
[Time]: 平均情况下可以达到O(N)，最差的时间复杂度为O(N*N)。
[Space]: O(N)
Runtime: 100 ms, faster than 90.49% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 17.1 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.

[缺点]：
虽然时间复杂度是 O(n) ，但是缺点也很明显，最主要的就是内存问题，在海量数据的情况下，
我们很有可能没办法一次性将数据全部加载入内存，这个时候这个方法就无法完成使命了
同时需要我们修改输入的数组，这也是值得考虑的一点

所以面对海量数据，我们就可以放分布式的方向去思考了

我们可以将数据分散在多台机器中，然后每台机器并行计算各自的 TopK 数据，最后汇总，
再计算得到最终的 TopK 数据 （相当于分治）
这种数据分片的分布式思想在面试中非常值得一提，在实际项目中也十分常见
'''
import collections
import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k < 0: return []
        if len(nums) == k: return nums
        counts = list(collections.Counter(nums).items())
        top_k_counts = self.quickSelect(counts, k)
        return [count[0] for count in top_k_counts]

    # quick selection:
    def quickSelect(self, counts, k):
        if len(counts) <= k: return counts
        rand = random.randint(0,len(counts)-1)
        counts[0],counts[rand] = counts[rand],counts[0]
        p = counts[0]
        right = [p] + [count for count in counts[1:] if count[1] >= p[1]]
        r_len = len(right)
        if r_len == k:
            return right
        elif r_len > k:
            return self.quickSelect(right, k)
        else:
            return self.quickSelect([count for count in counts[1:] if count[1] < p[1]], k-r_len) + right

'''
[code 2]: pass index bounds instead of slicing list
Runtime: 108 ms, faster than 56.94% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 17.2 MB, less than 6.25% of Python3 online submissions for Top K Frequent Elements.
'''
import collections
import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k < 0: return []
        if len(nums) == k: return nums
        counts = list(collections.Counter(nums).items())
        top_k_counts = self.quickSelect(counts, 0, len(counts)-1, k)
        return [count[0] for count in top_k_counts]

    # quick selection:
    def quickSelect(self, counts, lo, hi, k):
        if hi-lo+1 <= k: return counts
        rand = random.randint(lo,hi)
        counts[lo],counts[rand] = counts[rand],counts[lo]
        p = lo
        i = lo + 1
        for j in range(i, hi+1):
            if counts[j][1] < counts[p][1]:
                if i != j:
                    counts[i],counts[j] = counts[j],counts[i]
                i += 1
        counts[i-1],counts[p] = counts[p],counts[i-1]
        p = i-1
        r_len = hi - p + 1
        if r_len == k:
            return counts[p:hi+1]
        elif r_len > k:
            if r_len-1 == k: return counts[p+1: hi+1]
            return self.quickSelect(counts, p, hi, k)
        else:
            return self.quickSelect(counts, lo, p-1, k-r_len) + counts[p:hi+1]

'''
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Use Counter to extract the top k frequent elements
        # most_common(k) return a list of tuples, where the first item of the tuple is the element,
        # and the second item of the tuple is the count
        # Thus, the built-in zip function could be used to extract the first item from the tuples
        return zip(*collections.Counter(nums).most_common(k))[0]
'''
