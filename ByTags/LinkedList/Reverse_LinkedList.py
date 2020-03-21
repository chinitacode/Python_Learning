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
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        node = head
        while node:
            nxt = node.next
            node.next = pre
            pre = node
            node = nxt
        return pre



'''
[Method 2]: Recursion
让函数返回只是链接方向改变了的链表，其在计算机内存储的reference地址是不变的
Time: O(n);
Space: O(n)， 由于使用递归，将会使用隐式栈空间。递归深度可能会达到 n 层。
Runtime: 36 ms, faster than 55.75% of Python3 online submissions for Reverse Linked List.
Memory Usage: 17.4 MB, less than 22.73% of Python3 online submissions for Reverse Linked List.
'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        tail = head
        # 记录最后用来连接头结点后剩余节点全反转后的尾节点，因为反转后返回的是反转后的头结点，即之前的尾结点
        connection = head.next # 所以我们需要先记录这个节点的reference，记其为连接两部分的枢纽
        front = self.reverseList(head.next)
        connection.next = tail
        # !!!重要!!!最后必须把之前的头节点，现在的尾结点原先的next指针指向None，否则会形成环路！
        tail.next = None
        return front

# or optimized as:
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        p = self.reverseList(head.next) # p存的是反转前的尾部node，并且head.next节点所有的指针全部反转，
        head.next.next = head          # 反转后原来的head.next变为尾部node,指向None,所以这里将它反转链接到head
        head.next = None
        return p
