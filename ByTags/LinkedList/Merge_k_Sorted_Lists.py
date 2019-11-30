'''
23. Merge k Sorted Lists [Hard]
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

[Method 1]: divide and conquer 分而治之，链表两两合并
把lists分成两部分，对每部分各进行k为len(lists)//2的个链表的合并，逐一两两合并链表，
最后再用合并两个链表的算法来合并两个链表。
[Time]: O(Nlogk), k为链表个数，N是合并两个链表时两个链表中的总节点数。
[Space]: O(1)， 重复利用原来的链表节点，每次选择节点时将它直接接在最后返回的链表后面，而不是创建一个新的节点。
整个过程中链表存的只是指针而已。
Runtime: 112 ms, faster than 43.18% of Python online submissions for Merge k Sorted Lists.
Memory Usage: 17.5 MB, less than 37.88% of Python online submissions for Merge k Sorted Lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: return
        if len(lists) == 1: return lists[0]
        mid = len(lists)//2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        # 因为两两合并，一共会调用log(k)次
        return self.merge(l, r)

    # 修改了l1和l2的指针，使它们连接起来
    # 【Time】: O(n), n为l1,l2的node数之后
    # 【Space】: O(1)，只是修改了指针
    def merge(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next



'''
[Method 2]: Iterative, dummy node + 优先级队列(最小堆)
设置一个dummy node和cur node，
利用python自带的由最小堆建立起的优先级队列，
先遍历k个链表的头部节点，
把每个链表里的头部节点按(node.val, node)元组放入（put操作相当于append的同时还维持优先级队列）
优先级队列里面(按node.val维持的最小优先级队列)，
get优先级队列里面的值最小的node（get操作相当于pop），
然后每次把cur节点的next指针指向这个node，同时更新cur和node为其next，
如果node不为空，则加入优先级队列。
最后返回dummy.next
[Time]: O(nlogk)
[Space]: O(k), 维持最小优先队列所需的额外空间
Runtime: 148 ms, faster than 31.64% of Python online submissions for Merge k Sorted Lists.
Memory Usage: 17.5 MB, less than 50.00% of Python online submissions for Merge k Sorted Lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        queue = PriorityQueue()
        # O(k)
        for l in lists:
            if l: # there may be empty linked list
                queue.put((l.val, l))
        # O(nlogk),因为一共有n个元素
        while not queue.empty():
            # O(logk)
            val, node = queue.get()
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                queue.put((node.val, node))
        return dummy.next

'''
同上，但是用最小堆直接实现：
[Time]: O(nlogk)
[Space]: O(k), 维持最小堆所需的额外空间
Runtime: 92 ms, faster than 75.15% of Python online submissions for Merge k Sorted Lists.
Memory Usage: 17.5 MB, less than 40.91% of Python online submissions for Merge k Sorted Lists.
'''
from heapq import heappush, heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        heap = []
        for l in lists:
            if l: # there may be empty linked list
                heappush(heap, (l.val, l))
        while heap:
            val, node = heappop(heap)
            cur.next = node
            cur = cur.next
            node = node.next
            if node:
                heappush(heap, (node.val, node))
        return dummy.next

'''
[Method 3]: Iterative
'''
def mergeKLists_iter(self, lists):
    if not lists:
        return
    if len(lists) == 1:
        return lists[0]
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = self.merge(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else lists



def merge(self, l, r):
    dummy = cur = ListNode(0)
    while l and r:
        if l.val < r.val:
            cur.next = l
            l = l.next
        else:
            cur.next = r
            r = r.next
        cur = cur.next
    cur.next = l or r
    return dummy.next
