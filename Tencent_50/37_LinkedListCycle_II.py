'''
# 142. Linked List Cycle II [Medium]
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.
[Note]: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow-up:
Can you solve it without using extra space?

Indeed it's more a math problem(环形追击问题)
1. find the position where slow and fast first meet;
2. the distance between the beginning loop position and it
is the same as the position of the beginning loop;
3. set slow to the head of the link, index = 0;
4. when slow and fast meet again(both forward at the same speed), return index.

Consider the following linked list, where E is the cylce entry and k, the crossing point of fast and slow.
        H: distance from head to cycle entry E
        D: distance from E to k(the shortest)
        L: cycle length
                          _____
                         /      \
                        /        H
        head_____H______E         \
                        \        /
                         k______/


        When slow reaches E, fast has already travelled 2H,
        arriving H of the cycle, in order to find out where they meet, the problem becomes like this:

        slow starts at E while fast starts at H, and fast travels twice as quickly as slow.
        So when fast catches slow, fast must have travelled one cycle already.
        Suppose they meet at k: L-K = (L + (L-K-H))/2
        ==> K = H

        So the problem evolves into solving K.
        Because slow forwards one step each time, so we put slow to head,
        make it and fast both travel to E at the speed of one step a time,
        and return slow when they meet again.

#O(n) 最多跑2n
Runtime: 52 ms, faster than 95.00% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow, fast = slow.next, fast.next
                return fast
        return None

'''
#Or:
Runtime: 48 ms, faster than 99.17% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 17.1 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while slow and fast:
            fast = fast.next
            slow = slow.next
            if fast:
                fast = fast.next
            if slow == fast:
                break
        if fast and slow and fast == slow:
            cur = head
            while(cur != fast):
                cur = cur.next
                fast = fast.next
            return fast
        return None

'''
#Or: try-except
Runtime: 56 ms, faster than 83.33% of Python3 online submissions for Linked List Cycle II.
Memory Usage: 16.8 MB, less than 100.00% of Python3 online submissions for Linked List Cycle II.
'''
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            slow, fast = head, head
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
                if slow == fast:
                    slow = head
                    break
            else:
                return None
            while slow != fast:
                slow, fast = slow.next, fast.next
            return slow
        except:
            return None
