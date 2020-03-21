'''
876. Middle of the Linked List [Easy]

Given a non-empty, singly linked list with head node head,
return a middle node of linked list.
If there are two middle nodes, return the second middle node.

Example 1:
Input: [1,2,3,4,5]

Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).

Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])

Since the list has two middle nodes with values 3 and 4, we return the second one.


Note:
The number of nodes in the given list will be between 1 and 100.

[Method 1]: 快慢指针
[Time]: O(N),一次遍历，偶数个节点直接返回第二个中间节点
[Space]: O(1)
Runtime: 24 ms, faster than 85.05% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Middle of the Linked List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow



'''
[笨办法]：即偶数节点的话循环后返回的是第一个中间节点，还需要加判断修改
'''

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slow = fast = head
        # 奇数个节点时fast会走到最后一个节点，所以fast.next是None,这时再在while条件里用fast.next.next非法，因为None没有next属性，所以必须用AND判断！
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next: #如果偶数个节点，因为要返回靠后的中间节点
            return slow.next
        return slow
