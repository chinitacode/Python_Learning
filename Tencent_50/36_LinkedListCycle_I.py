'''
# 141. Linked List Cycle I [Easy]
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed)
in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list,
where tail connects to the second node.
3 -> 2 -> 0 -> 4 -- >
     ^
     |              |
      - - - - - - -

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list,
where tail connects to the first node.


Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it using O(1) (i.e. constant) memory?


[Method 1]:iteration + two-pointer
# 龟兔赛跑算法Tortoise and hare algorithm
slow和fast两个指针，slow一次只跑一步，fast一次跑两步；
如果有循环，fast和slow必定会重合，则返回True;
否则返回False。
Time Complexity: O(n), 如果有循环，最差也是slow走完整个链表；若无，则当fast走到尽头就结束（O(n/2)）
Space Complexity: O(1)
Runtime: 40 ms, faster than 58.71% of Python online submissions for Linked List Cycle.
Memory Usage: 18.1 MB, less than 60.99% of Python online submissions for Linked List Cycle.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

'''
[Method 2(Best)]: **try - except block**
The "trick" is to not check all the time whether
we have reached the end but to handle it via an exception.
"Easier to ask for forgiveness than permission."
Runtime: 32 ms, faster than 93.58% of Python online submissions for Linked List Cycle.
Memory Usage: 18.1 MB, less than 70.92% of Python online submissions for Linked List Cycle.
'''
# When initialize, fast is one step ahead of slow
def hasCycle1(head):
    try:
        slow = head
        #如果head.next不存在（即head只有一个node且无循环）则出现error到except里return False
        fast = head.next
        #只要fast赶上slow，则return True
        while slow is not fast:
            #一旦出现None，None无next属性则会到except里报错
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

'''
[Method 3]: Hashmap
Runtime: 40 ms, faster than 58.71% of Python online submissions for Linked List Cycle.
Memory Usage: 19.3 MB, less than 6.38% of Python online submissions for Linked List Cycle.
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeseen = {}
        while head:
            if head in nodeseen:
                return True
            nodeseen[head] = head
            head = head.next
        return False

'''
[Method 4]: Set()
Runtime: 36 ms, faster than 81.08% of Python online submissions for Linked List Cycle.
Memory Usage: 18.8 MB, less than 12.06% of Python online submissions for Linked List Cycle.
'''
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeSeen = set() # init set
        while head != None:
            if head in nodeSeen:
                return True
            else:
                nodeSeen.add(head)
            head = head.next
        return False


'''
# Considering dummy node and the self-defined classes here:
'''
def has_cycle(ll):
    '''
    >>> ll1 = SLL(4, 8, 1, 3)
    >>> ll1[-1].next = ll1[1]
    >>> has_cycle(ll1)
    True
    '''
    assert ll.size > 0, 'The linked list is empty!'
    slow, fast = ll.head.next, ll.head.next
    index = 0
    while fast.next != None and fast.next.next != None:
        slow, fast = slow.next, fast.next.next
        index += 1
        if slow == fast:
            return True
    return False
