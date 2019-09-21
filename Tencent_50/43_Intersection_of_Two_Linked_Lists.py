'''
160. Intersection of Two Linked Lists [Easy]
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:
      a1 -> a2 ->
                  \
                   c1 -> c2
                  /
b1 -> b2 -> b3 ->

begin to intersect at node c1.

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5].
From the head of B, it reads as [5,0,1,8,4,5].
There are 2 nodes before the intersected node in A;
There are 3 nodes before the intersected node in B.


Example 2:

Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [0,9,1,2,4].
From the head of B, it reads as [3,2,4].
There are 3 nodes before the intersected node in A;
There are 1 node before the intersected node in B.


Example 3:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4].
From the head of B, it reads as [1,5].
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

[Method 1]:
计算两个链表分别的长度，求差值，使得两个指针指在链表长度相对应的位置，
再往后遍历，直到找到相交节点(l1 is l2, 包括无相交都为None)时return。
Time: O(max(m,n))， m和n分别为两个链表相应的长度；
Space: O(1)
Runtime: 192 ms, faster than 70.22% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 41.9 MB, less than 16.00% of Python online submissions for Intersection of Two Linked Lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        l1, l2 = headA, headB
        len1, len2 = 0, 0
        while l1:
            l1 = l1.next
            len1 += 1
        while l2:
            l2 = l2.next
            len2 += 1
        if len1 < len2:
            l1, l2 = headB, headA
        else:
            l1, l2 = headA, headB
        diff = abs(len1 - len2)
        for i in range(diff):
            l1 = l1.next
        while l1 is not l2:
            l1, l2 = l1.next, l2.next
        return l1

'''
[Method 2]: 不去算length。
可以把问题改成一个公平的跑步问题。
让A和B同时往前以1步的速度跑，假设A链表比B短。
当A跑到终点时B还没有到，于是让A到B的起点开始继续跑，
当B跑到终点时，让B回到A的起点继续跑，则A和B最后都会在交点相遇，
因为都各自跑了skipA + intersection + skipB的距离。
Time: O(len(skipA + intersection + skipB))
Space: O(1)
Runtime: 180 ms, faster than 95.74% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 41.9 MB, less than 16.00% of Python online submissions for Intersection of Two Linked Lists.
'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        l1, l2 = headA, headB
        while l1 is not l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1


'''
Test module:
input processing module:

'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def inpu(A,B,skipA,skipB):
    for i in range(skipA):
        A[i] = ListNode(A[i])
    for j in range(skipB):
        B[j] = ListNode(B[j])
    for p in range(len(A)-skipA):
        A[p+skipA] = ListNode(A[p+skipA])
    for i in range(len(A)):
        A[i].next = A[i+1] if i + 1 < len(A) else None
    for j in range(skipB-1):
        B[j].next = B[j+1] if j + 1 < len(B) else None
    B[skipB-1].next = A[skipA] if skipA < len(A) else None
    return A[0], B[0]
headA, headB = inpu([4,1,8,4,5],[5,0,1,8,4,5],2,3)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB: return None
        l1, l2 = headA, headB
        while l1 is not l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

res = Solution()
print(res.getIntersectionNode(headA, headB))
