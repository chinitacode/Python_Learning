'''
19. Remove Nth Node From End of List [Medium]
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?

[Method] 双指针一次遍历（参照Nth_Node_From_End_of_List）
因为需要删除链表，所以我们添加一个哑结点pre来处理需要删除头/尾节点的情况，
如果不是头/尾节点，则按照题目Nth_Node_From_End_of_List用slow找到该节点后再用链表删除节点题目的方法
先修改slow的值再将其next指针后挪一位就可。
但是[注意！]在处理删除头/尾节点的情况时如果本身链表就只有一个节点(not head.next)时，
如list: 1, n = 1的情况
pre.next.next为None, 所以如果pre.next = pre.next.next就是pre.next = None,
即pre与链表不再有任何关联性，所以这时最好的做法时直接返回None。

Runtime: 24 ms, faster than 95.67% of Python3 online submissions for Remove Nth Node From End of List.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Remove Nth Node From End of List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or not n: return
        pre = ListNode(0)
        pre.next = head
        fast = slow = head
        # make a distance of (k-1) between slow and fast
        for _ in range(n-1):
            try:
                fast = fast.next
            except: # 如果链表还没有k长则输入非法
                raise(IndexError)
        while fast.next:
            fast, slow, pre = fast.next, slow.next, pre.next
        if n == 1:
            if not head.next: return None
            pre.next = None
        else:
            slow.val = slow.next.val
            slow.next = slow.next.next
        return head

'''
[Method 2] 双指针一次遍历，不需要哑结点pre
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = head
        for i in range(n):
            if fast != None:
                fast = fast.next
        #Crucial step:
        #If after taking n steps fast is None,
        # it means the length of the list is n,
        # so we only need to delete the first element(return head.next)
        if not fast:
            return head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next # slow and fast have a distance of n, i.e. slow is at the pre node of the target node 
        slow.next = slow.next.next
        return head
