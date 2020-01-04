'''
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留。

样例1
输入：1->2->3->3->4->4->5

输出：1->2->5
样例2
输入：1->1->1->2->3

输出：2->3


[Method 1]:
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplication(self, pHead):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not pHead or not pHead.next: return pHead
        dummy = prev = ListNode(None)
        dummy.next = pHead
        h = pHead
        node = h.next
        while node:
            if node.val != h.val:
                prev = h
                h, node = h.next, node.next
            else:
                while node.val == h.val:
                    node = node.next
                    if not node:
                        prev.next = None
                        return dummy.next
                h.val = node.val
                h.next = node.next
                node = node.next
        return dummy.next

# 优化为：
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        dummy = pre = ListNode(None)
        dummy.next = h = pHead
        while h:
            if h.next and h.val == h.next.val:
                cur  = h.next
                while  cur and cur.val == h.val:
                    cur = cur.next
                pre.next,h = cur,cur
            else:
                pre = h
                h = h.next

        return dummy.next
