'''
206. Reverse Linked List [Easy]
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively.
Could you implement both?

[Method 1] Iteration + 3-pointer(prev, curr, nxt)
实际上就是把链表的指向全部反转,每次都要更新prev为curr。
注意链接最后的节点到prev后再返回。
Assume that we have linked list 1 → 2 → 3 → Ø, we would like to change it to Ø ← 1 ← 2 ← 3.
While you are traversing the list, change the current node's next pointer to point to its previous element.
Since a node does not have reference to its previous node, you must store its previous element beforehand.
You also need another pointer to store the next node before changing the reference.

Time: O(n); Space: O(1)
Runtime: 36 ms, faster than 95.88% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15 MB, less than 31.82% of Python3 online submissions for Reverse Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        prev = nxt = None
        curr = head
        while curr.next is not None:
            #先记下下一个节点(再反转curr链接方向)
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr.next = prev
        return curr

'''
[Method 2]: Recursion
让函数返回只是链接方向改变了的链表，其在计算机内存储的reference地址是不变的
Time: O(n); Space: O(n)
Runtime: 44 ms, faster than 55.94% of Python3 online submissions for Reverse Linked List.
Memory Usage: 19.2 MB, less than 18.18% of Python3 online submissions for Reverse Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
