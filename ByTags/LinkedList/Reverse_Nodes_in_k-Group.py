'''
25. Reverse Nodes in k-Group [Hard]
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes,
only nodes itself may be changed.

[Method 1]: Iteration using stack (piggybacking on Swap_Nodes_In_Pairs)
[Time]: O(n)
[Space]: O(k), 栈的空间。
Runtime: 48 ms, faster than 86.24% of Python3 online submissions for Reverse Nodes in k-Group.
Memory Usage: 13.4 MB, less than 100.00% of Python3 online submissions for Reverse Nodes in k-Group.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k <=1: return head
        cur = head
        count = 1
        stack = []
        while count <= k:
            if cur:
                stack.append(cur)
                cur = cur.next
                count += 1
            else:
                return head
        head = stack[-1]
        while len(stack) > k-1:
            last = stack[-1].next
            for i in range(k-1):
                node = stack.pop()
                node.next = stack[-1]
            node = stack.pop()
            nxt = last
            for j in range(k):
                if nxt:
                    stack.append(nxt)
                    nxt = nxt.next
                else:
                    node.next = last
                    return head
            node.next = stack[-1]
        return head
