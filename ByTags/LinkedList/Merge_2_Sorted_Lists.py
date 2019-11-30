'''
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

[Method 1]: Iterative: 利用Merge sort的merge解法
[Time]: O(m + n)
[Space]: O(m + n) 因为每次都创建新的node
Runtime: 24 ms, faster than 63.86% of Python online submissions for Merge Two Sorted Lists.
Memory Usage: 11.9 MB, less than 12.64% of Python online submissions for Merge Two Sorted Lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 不改变l1、l2的解法
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = node = ListNode(None)
        i, j = l1, l2
        while i and j:
            if i.val <= j.val:
                node.next = ListNode(i.val)
                i = i.next
            else:
                node.next = ListNode(j.val)
                j = j.next
            node = node.next
        while i:
            node.next = ListNode(i.val)
            i,node = i.next, node.next
        while j:
            node.next = ListNode(j.val)
            j,node = j.next, node.next
        return dummy.next

# or:
'''
[Time]: O(m + n)
[Space]: O(1) 迭代的过程只会产生几个指针，所以它所需要的空间是常数级别的。
'''
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


'''
[Method 2]: Recursive
[Time]: O(n + m)
[Space]: O(n + m),调用 mergeTwoLists 退出时 l1 和 l2 中每个元素都一定已经被遍历过了，
所以 n + m 个栈帧会消耗 O(n + m) 的空间。

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if None in (l1, l2): return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2
