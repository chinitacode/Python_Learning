'''
234. Palindrome Linked List
Easy

Given a singly linked list, determine if it is a palindrome.
Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?


[Method 1]: 迭代(找到中间节点+反转前一半链表+遍历两部分比较值)
先遍历一遍找到中间节点并判断节点总数是奇数还是偶数，然后设置中间节点mid为mid的下一位，
用来作为接下来反转前半部分链表的停止条件，反转了前半部分链表后，根据奇偶性找到相对应的
两个回文节点，再遍历一次比较val是否相等（注意此时本身就是不同的节点，只能比较值），
一旦不等就返回False，否则遍历完后返回True。

[Time]: O(n + n//2 + n//2) = O(n)
[Space]: O(1)
Runtime: 68 ms, faster than 75.09% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 22.8 MB, less than 100.00% of Python3 online submissions for Palindrome Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        # get the middle node of the list
        slow = fast =head
        odd = True
        while fast.next and fast.next.next:
            slow,fast = slow.next,fast.next.next
        if fast.next:
            odd = False
        mid = slow.next # set mid as the next node of the real mid
        node = head
        pre = nxt = None
        # reverse nodes from head to mid (not including mid)
        while node != mid:
            nxt = node.next
            node.next = pre
            pre = node
            node = nxt

        if odd:
            pre = pre.next
        while pre and node:
            if pre.val != node.val:
                return False
            pre = pre.next
            node = node.next
        return True
'''
或者：
Runtime: 76 ms, faster than 32.72% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 23 MB, less than 100.00% of Python3 online submissions for Palindrome Linked List.
'''
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next: return True
        # get the middle node of the list
        slow = fast =head
        while fast and fast.next: # 这样写能使偶数个节点时返回靠后的中间节点，同时用fast来判断总节点奇偶性
            slow,fast = slow.next,fast.next.next #偶数个节点则slow指向第二个mid节点，奇数的话slow就是mid
        if fast: # 如果奇数个节点，slow再往后一位方便反转链表
            slow = slow.next
        node = head
        pre = nxt = None

        # 将slow前面的节点的指针全部反转
        while node != slow:
            nxt = node.next
            node.next = pre
            pre = node
            node = nxt

        # 如果奇数个节点
        if fast: # 只能用fast来判断奇偶性，如果用fast.next，如果只有两哥节点，next指针也被反转了不可用
            pre = pre.next # pre还得往前一步才是回文比较的节点

        while pre and node:
            if pre.val != node.val:
                return False
            pre = pre.next
            node = node.next
        return True



'''
比较完成后我们应该将链表恢复原样。虽然不需要恢复也能通过测试用例，因为使用该函数的人不希望链表结构被更改。

[Method 2]: （pythonic写法）同时完成找中间节点和反转前半部分
'''
def isPalindrome(self, head):
    # rev 起反转链表的作用
    rev = None
    # initially slow and fast are the same, starting from head
    slow = fast = head
    while fast and fast.next:
        # fast traverses faster and moves to the end of the list if the length is odd
        fast = fast.next.next
        # （pythonic写法）
        # rev比rev.next先被赋值，所以当处理到rev.next的时候rev已经先被赋值为slow了,因此rev有next属性，然后slow的赋值也不影响rev和rev.next
        rev, rev.next, slow = slow, rev, slow.next # 最后一步的rev指向slow的前一个节点，也就是中间节点的前一个
    if fast: # 即总的有奇数个节点，因此使slow跳过中间节点，毕竟只需要比较回文的部分
       # 如果fast为None说明总的有偶数个节点，那么slow本来就指向的是偏后的中间节点
        slow = slow.next
    # compare the reversed first half with the second half
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next

    # if equivalent then rev become None, return True; otherwise return False
    return not rev
