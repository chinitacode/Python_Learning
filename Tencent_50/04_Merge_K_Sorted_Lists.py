'''
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# iteratively
# O(m + n)
def mergeTwoLists1(l1, l2):
    dummy = cur = Node(0)
    while l1 and l2:
        if l1.value < l2.value:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next


# 23. Merge k Sorted Lists
# divide and conquer solution, Time: O(Nlogk), Space: O(1)
#Recursive solution:
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return
        if len(lists) == 1: return lists[0]
        mid = len(lists)//2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge2Lists(l,r)

    def merge2Lists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

#Iterative solution
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
