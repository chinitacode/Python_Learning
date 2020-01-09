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

[Method 1]: Hashmap
Store number of occurrence of each different number in the dictionary,
then sort the dictionary by its occurrence in reversed order,
and output the top k frecuent numbers.
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
[Method 2]: ***Hashmap + Bucket Sort***
桶排序（箱排序）：
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
题目最终需要返回的是前 k 个频率最大的元素，
可以想到借助堆这种数据结构，对于 k 频率之后的元素不用再去处理，进一步优化时间复杂度。
具体操作：
借助哈希表来建立数字和其出现次数的映射，遍历一遍数组统计元素的频率
维护一个元素数目为 k 的最小堆
每次都将新的元素与堆顶元素（堆中频率最小的元素）进行比较
如果新的元素的频率比堆顶端的元素大，则弹出堆顶端的元素，将新的元素添加进堆中
最终，堆中的 k 个元素即为前 k 个高频元素。

[Time]：O(nlogk)，n 表示数组的长度。
首先，遍历一遍数组统计元素的频率，这一系列操作的时间复杂度是 O(n)；
接着，遍历用于存储元素频率的 Hash Map，如果元素的频率大于最小堆中顶部的元素，
则将顶部的元素删除并将该元素加入堆中，这里维护堆的数目是 k，
所以这一系列操作的时间复杂度是 O(nlogk) 的；因此，总的时间复杂度是 O(nlog⁡k)。
[Space]：O(n)，最坏情况下（每个元素都不同），map 需要存储 n 个键值对，优先队列需要存储 k 个元素，因此，空间复杂度是O(n)。
'''
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
#Or:
Uses a dict to maintain counts,
heapifys the list of counts,
then selects K elements out of the max heap.
O(klogn)
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
            topk.append(heapq.heappop(freq_list)[1])
        return topk

'''
[Method 4]:dictionary + quick select
快速选择实现原理和快速排序类似。

给出一个序列，我们不知道该序列是否已经排好序，如果我们想从中选择第k小的数，该怎么做？
最简单最直观的方法是对这个序列进行排序，然后依据k选择索引为k-1数即可。
由于排序的时间复杂度为O(NlogN)。所有这种选择第k小的数的时间复杂度是O(NlogN)。

这样会造成一定的浪费，因为我们仅仅是想从中选择第k个小的数，
而对序列进行排序导致前k-1个数和后面的n-k个数都是有序的，
这种有序对选择第k个小的数没有什么意义。
所以，排序造成了一定的浪费。

利用快速排序原理选择第k小的数，时间复杂度平均情况下可以达到O(N)，最差的时间复杂度为O(N*N)。
其原理是：每次对序列按照枢纽元进行左右风格，分割后，i指向枢纽元(pivot)。
如果k=i+1，则arr[i]就是序列中第k小的数；如果k<i+1，则第k小的数在左半部分，继续对左半部分进行分割，选择左半部分中第k个小的数；
如果k>i+1，则第k小的数在右半部分，继续对右半部分进行分割，选择右半部分中第k-i-1小的数。

如果我们直接在原序列上进行快速选择，则会打乱原来序列中元素的位置。
如果不想打乱元素的位置，可以拷贝临时的一份作为快速选择的序列。

Use a dictionary to get the frequencies,
and then used quick select to get the top k frequenct elements.
'''
def topKFrequent(nums, k):

    def quick_select(left, right):
        pivot = left
        l, r = left, right
        while l < r:
            while l < r and counts[r][1] <= counts[pivot][1]:
                r -= 1
            while l < r and counts[l][1] >= counts[pivot][1]:
                l += 1
            counts[l], counts[r] = counts[r], counts[l]
        counts[left], counts[l] = counts[l], counts[left]

        if l + 1 == k:
            return counts[:l+1]
        elif l + 1 < k:
            return quick_select(l + 1, right)
        else:
            return quick_select(left, l - 1)

    if not nums:
        return []

    # Get the counts.
    counts = {}
    for x in nums:
        counts[x] = counts.setdefault(x, 0) + 1

    counts = counts.items()
    # Use quick select to get the top k counts.
    return [c[0] for c in quick_select(0, len(counts) - 1)]

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
