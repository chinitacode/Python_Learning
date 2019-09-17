'''
21. Merge Two Sorted Lists [Easy]
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


Method1: [Iteration]piggybacking on merge sort: dummy head + two-pointer
O(n) time & O(1) space
Runtime: 44 ms, faster than 64.13% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l2 or l1
        dummy = node = ListNode(None)
        i, j = l1, l2
        while i and j:
            if i.val < j.val:
                node.next = i
                i = i.next
            else:
                node.next = j
                j = j.next
            node = node.next
        if i:
            node.next = i
        if j:
            node.next = j
        return dummy.next

'''
#可以改进最后一步：
Runtime: 40 ms, faster than 88.19% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.8 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            return l2 or l1
        dummy = node = ListNode(None)
        i, j = l1, l2
        while i and j:
            if i.val < j.val:
                node.next = i
                i = i.next
            else:
                node.next = j
                j = j.next
            node = node.next
        node.next = i or j
        return dummy.next


'''
Method2: [Recursion]
Runtime: 48 ms, faster than 25.19% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.9 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.
'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #因为None没有next
        if l1 and l2:
            #使l1始终为最小
            if l1.val > l2.val:
                l1, l2 = l2, l1
            #递归到的base case为其中一方为none，则返回非none的链表
            #当未递归到base case时，只是不停地交换l1和l2
            l1.next = self.mergeTwoLists(l1.next, l2)
        #返回非none
        return l1 or l2

'''
Method3:[Recursion2]
First make sure that a is the "better" one (meaning b is None or has larger/equal value).
Then merge the remainders behind a.
Runtime: 48 ms, faster than 25.19% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.7 MB, less than 6.61% of Python3 online submissions for Merge Two Sorted Lists.

'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #相当于：
        #if not l1 or (l2 and l1.val > l2.val):
        #如果l1是None，则把l2换成l1；
        #再判断换了之后的l1(原l2)是不是None，若是，则直接返回l1(None)
        if not l1 or l2 and l1.val > l2.val:
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
