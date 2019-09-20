'''
2. Add Two Numbers [Medium]

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

[Note] 特别注意一下边际情况，如当两个链表长度不一样时，以及涉及到进位：
Special cases:
Input:
    [1,8]
    [0]
Output:
    [1,8]

Input:
    [9,8]
    [1]
Output:
    [0,9]

Input:
    [9,9,9,9]
    [1]
Output:
    [0,0,0,0,1]


[Method1]：有额外空间，two-pointer + dummy head + iteration
时间复杂度：O(max(m,n))，m 和 n 分别表示 l1 和 l2 的长度，下面的算法最多重复max(m,n) 次。
空间复杂度：O(max(m,n))， 新列表的长度最多为max(m,n)+1。
Runtime: 76 ms, faster than 79.29% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.1 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        i, j = l1, l2
        dummy = node = ListNode(0)
        while i and j:
            value = i.val + j.val + node.val
            if value > 9:
                node.val = value - 10
                node.next = ListNode(1)
            else:
                node.val = value
                node.next = ListNode(0) if (i.next or j.next) else None
            #如果i的长度大于j的长度，则补足j的长度
            if not j.next and i.next:
                j.next = ListNode(0)
            #如果j的长度大于i的长度，则补足i的长度
            if not i.next and j.next:
                i.next = ListNode(0)
            i, j, node = i.next, j.next, node.next
        return dummy

'''
[Optimization]精简代码：以下解法不需要分开讨论l1和l2的长短，
carry为进位，取值只能是0或者1（最多也只有（9 + 9 = 18， 进1留8）
时间复杂度：O(max(m,n))，m 和 n 分别表示 l1 和 l2 的长度，下面的算法最多重复max(m,n) 次。
空间复杂度：O(max(m,n))， 新列表的长度最多为max(m,n)+1。
Runtime: 64 ms, faster than 99.59% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.1 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            #只能是carry取10的余数，如果是-10，则当carry小于10时值会为负
            cur.next = ListNode(carry % 10)
            cur = cur.next
            #这里的进项carry只有0和1两个取值
            carry //= 10
        return dummy.next

'''
[Method2] 递归: 将链表转换为Integer，求和后再转换为链表。
Runtime: 64 ms, faster than 99.59% of Python3 online submissions for Add Two Numbers.
Memory Usage: 14.1 MB, less than 5.67% of Python3 online submissions for Add Two Numbers.
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            node = ListNode(n % 10)
            if n > 9:
                node.next = tolist(n // 10)
            return node
        return tolist(toint(l1) + toint(l2))

'''
[Follow up]:
What if the the digits in the linked list are stored in non-reversed order?
For example:
(3→4→2) + (4→6→5) = 8→0→7

[思路1]参照上面递归的方法，把l1和l2转化为integer，求和后再转换为链表

[思路2(复杂)]仍然用迭代法，只是得找出最长的链表，将最短的链表头部用ListNode(0)补齐，再从尾部相加

[思路3]先reverse l1和l2，再用原思路。
'''
