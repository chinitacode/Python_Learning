'''
剑指offer22. 链表中倒数第k个节点
输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。
这个链表的倒数第3个节点是值为4的节点。

示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.

[Method 1]: 双指针一次遍历
当不允许求链表长度时，可以用一个fast指针先走k-1步，再用一个slow指针指向head，
使得两个指针之间相差k-1个节点，再同时让两个指针一起一步步地走，当fast走到最后一个节点时，
slow指向的就是倒数第k个节点。

注意：
此题由其要注意非法输入，如链表为空、k为0和链表长度小于k的情况，通通都要先考虑到并且避免。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head or not k: return
        fast = slow = head
        # make a distance of (k-1) between slow and fast
        for _ in range(k-1):
            try:
                fast = fast.next
            except: # 如果链表还没有k长则输入非法
                raise(IndexError)

        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow
