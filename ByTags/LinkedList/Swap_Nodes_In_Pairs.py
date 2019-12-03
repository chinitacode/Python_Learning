'''
24. Swap Nodes in Pairs [Medium]
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.

[Method 1]: Recursion
借助helper方法reverse来把整个链表全部反转，但是实际上我们每次只传两个节点的链表给它，
从前两个节点开始reverse，之前先记下第三个节点nxt，剩下的我们用swapPairs(nxt)递归就可以。
[Time]: O(2n) = O(n)
[Space]: O(n)，递归栈
Runtime: 24 ms, faster than 97.33% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        cur = head
        nxt = self.swapPairs(cur.next.next)
        cur.next.next = None
        cur = self.reverse(cur)
        cur.next.next = nxt
        return cur

    def reverse(self, head):
        if not head or not head.next: return head
        p = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return p

'''
[Method 2]: Iteration using stack
每次放两个节点进栈里，pop出来的同时先把下面的两个（或1个，反正非空）节点压入栈，
然后改指针方向。关键是把反转后的第二个节点链接到栈里的最后一个节点上，
即nxt.next = stack[-1] if stack else None。
最后在栈内元素个数少于2时停下，因为我们只按对反转。

[Time]: O(n)，遍历每一个节点
[Space]: O(1), 栈最多也就容纳两个节点。
Runtime: 20 ms, faster than 99.37% of Python3 online submissions for Swap Nodes in Pairs.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Swap Nodes in Pairs.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        cur = head
        stack = [cur,cur.next]
        head = stack[-1]
        while len(stack) > 1:
            prev = stack.pop()
            nxt = stack.pop()
            if prev.next and prev.next.next:
                stack.append(prev.next)
                stack.append(prev.next.next)
            elif prev.next:
                stack.append(prev.next)
            prev.next = nxt
            nxt.next = stack[-1] if stack else None
        return head
