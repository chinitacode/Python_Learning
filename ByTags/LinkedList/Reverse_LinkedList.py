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
实际上就是遍历的时候把前后节点先存起来，再把链表的指向全部反转,每次都要更新prev和nxt。
注意链接最后的节点到prev后再返回。
Assume that we have linked list 1 → 2 → 3 → Ø, we would like to change it to Ø ← 1 ← 2 ← 3.
While you are traversing the list, change the current node's next pointer to point to its previous element.
Since a node does not have reference to its previous node, you must store its previous element beforehand.
You also need another pointer to store the next node before changing the reference.

Time: O(n); Space: O(1)
Runtime: 24 ms, faster than 59.90% of Python online submissions for Reverse Linked List.
Memory Usage: 13.7 MB, less than 44.44% of Python online submissions for Reverse Linked List.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Iterative method
        if not head: return
        prev = nxt = None
        cur = head
        while cur.next:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        cur.next = prev
        return cur



'''
[Method 2]: Recursion
让函数返回只是链接方向改变了的链表，其在计算机内存储的reference地址是不变的
Time: O(n);
Space: O(n)， 由于使用递归，将会使用隐式栈空间。递归深度可能会达到 n 层。
Runtime: 44 ms, faster than 55.94% of Python3 online submissions for Reverse Linked List.
Memory Usage: 19.2 MB, less than 18.18% of Python3 online submissions for Reverse Linked List.
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        last, lnk = head, head.next
        head = self.reverseList(head.next)
        lnk.next = last
        last.next = None
        return head

# or optimized as:
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        p = self.reverseList(head.next) # p存的是反转前的尾部node，并且head.next节点所有的指针全部反转，
        head.next.next = head          # 反转后原来的head.next变为尾部node,指向None,所以这里将它反转链接到head
        head.next = None
        return p
