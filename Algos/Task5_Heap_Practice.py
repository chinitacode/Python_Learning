import heapq
'''
· 求一组动态数据集合的最大 Top K
· 利用优先级队列合并 K 个有序数组
· 堆排序


Ex.1 Kth Largest Element in Arary
Find the kth largest element in an unsorted array.

[Method 1]:
Maintain a min heap of size k,
traversing the numbers of the input array,
if the number is bigger than the top of the heap,
replace the top of the heap by the number.
In the end, output the top of the heap.
[Time]:O(nlogk)
'''
def kthLargest(nums,k):
    h = []
    for num in nums:
        heapq.heappush(h, num)
        if len(h) > k:
            heapq.heappop(h)
    return h[0]
if __name__ == '__main__':
    nums = [5,11,3,6,12,9,8,10,14,1,4,2,7,15]
    k = 5
    kthLargest(nums, k) #10

# O(nlogk) time, min-heap
def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[k-1]
'''
[Method 2]:
'''
#O(n + (n-k)logn)
def KthLargest(nums,k):
    heapq.heapify(nums)
    for i in range(len(nums)-k):
        print(heapq.heappop(nums))
    return heapq.heappop(nums)
if __name__ == '__main__':
    nums = [5,11,3,6,12,9,8,10,14,1,4,2,7,15]
    k = 5
    KthLargest(nums, k)

'''
Find the kth smallest element in an unsorted array.
'''
#O(n + klogn)
def KthSmallest(nums,k):
    heapq.heapify(nums)
    for i in range(k):
        print(heapq.heappop(nums))
    return heapq.heappop(nums)
if __name__ == '__main__':
    nums = [5,11,3,6,12,9,8,10,14,1,4,2,7,15]
    k = 5
    KthSmallest(nums, k)


'''
Ex.2 Top K Frequent Words
Leetcode 692 [Medium]
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, then the word with the lower alphabetical order comes first.

[Method 1]:Min heap
O(nlogk)
'''
from collections import Counter
import heapq
class Item(object):
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self,other):
        if self.count == other.count:
            #首字母在前的单词优先级高，所以这里要反着来
            return self.word > other.word
        return self.count < other.count

    def __eq__(self,other):
        return self.count == other.count and self.word == other.count

def topkfrequent(words,k):
    if not words or k < 0 or k > len(words): return []
    #maintain a min heap of k words
    h = []
    #count the freqs of each word
    counted = Counter(words)
    for word, count in counted.items():
        #以tuple的形式(Item instance, word)入堆
        heapq.heappush(h, (Item(count,word),word))
        #优先级低的都被pop出去了
        if len(h) > k:
            heapq.heappop(h)
    res = []
    for _ in range(k):
        #优先级低的先入
        res.insert(0,heapq.heappop(h)[1])
    return res

if __name__ == '__main__':
    words = ["i", "love", "you", "i", "love", "coding","i","like","sports"]
    k = 2
    print(topkfrequent(words, k)) #['i', 'love']


'''
[Method 2]: Counter().most_common(k)
'''
def topKFrequent(nums, k):
    from collections import Counter as ct
    return [num for (num,count) in ct(nums).most_common(k)]
