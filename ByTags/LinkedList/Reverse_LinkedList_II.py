'''
92. Reverse Linked List II  [Medium]
Reverse a linked list from position m to n. 反转从位置 m 到 n 的链表。
Do it in one-pass.  请使用一趟扫描完成反转。
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

[Method 1]: 迭代 + dummy node + 多指针：
记住要反转部分的前一个节点 begin，要反转部分的开头节点（即为反转后部分的尾节点）end，
然后按照全部分反转的思路，对要反转的节点记录prev和nxt,反转完后的prev即为反转后部分链表的起始节点，
nxt则为反转前该部分链表的后面部分，此时将begin的指针连改到指向prev, end的指针改向连接nxt，
返回dummy.next即可。

[Time]: O(n)，按题意，只需一次遍历。
[Space]: O(1)，只是改变了指针。
Runtime: 20 ms, faster than 46.08% of Python online submissions for Reverse Linked List II.
Memory Usage: 12 MB, less than 60.00% of Python online submissions for Reverse Linked List II.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m > n: return
        if m == n: return head
        dummy = ListNode(0) #以防m==1的情况
        dummy.next = head
        cur = dummy
        count = 0
        while count < m-1:
            cur = cur.next
            count += 1
        begin = cur # prev of the node to start reversion
        cur = cur.next
        count += 1
        end = cur # end node of the reversed linked list
        prev, nxt = None, None
        while count <= n:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count += 1
        begin.next = prev
        end.next = nxt
        return dummy.next


# or: without dummy node
# 需要reverse的部分按照reverse linked list I的方法做，
# 最后判断reverse部分的前后还有没有节点，
# 如果有，还需要将前后连接起来，返回head，
# 否则就直接返回反转后的链表的头结点pre 
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m > n: return head
        i = 1
        start, cur = None, head
        while i < m and cur:
            start = cur
            cur = cur.next
            i += 1
        last, pre = cur, None
        while i <= n and cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
            i += 1
        if start: # if m != 1
            start.next = pre
        if cur:
            last.next = cur
        return head if start else pre

'''
[Method 2]: 递归
'''
