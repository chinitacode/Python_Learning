'''
Three Sum（求三数之和）

'''

# 15. 3Sum
# Time Complexity O(n^2)
# Space Complexity O(1)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        nums = sorted(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            new_target = -nums[i]
            while j < k:
                summ = nums[j] + nums[k]
                if summ < new_target:
                    j += 1
                elif summ > new_target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j += 1
                    j += 1
                    while k > j and nums[k-1] == nums[k]:
                        k -= 1
                    k -= 1
        return res

# 169. Majority Element
# two pass + dictionary
def majorityElement1(self, nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    for num in nums:
        if dic[num] > len(nums)//2:
            return num

# one pass + dictionary
def majorityElement2(self, nums):
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        if dic[num] > len(nums)//2:
            return num
        else:
            dic[num] += 1

# TLE
def majorityElement3(self, nums):
    for i in xrange(len(nums)):
        count = 0
        for j in xrange(len(nums)):
            if nums[j] == nums[i]:
                count += 1
        if count > len(nums)//2:
            return nums[i]

# Sotring
def majorityElement4(self, nums):
    nums.sort()
    return nums[len(nums)//2]

# Bit manipulation
def majorityElement5(self, nums):
    bit = [0]*32
    for num in nums:
        for j in xrange(32):
            bit[j] += num >> j & 1
    res = 0
    for i, val in enumerate(bit):
        if val > len(nums)//2:
            # if the 31th bit if 1,
            # it means it's a negative number
            if i == 31:
                res = -((1<<31)-res)
            else:
                res |= 1 << i
    return res

# Divide and Conquer
def majorityElement6(self, nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    a = self.majorityElement(nums[:len(nums)//2])
    b = self.majorityElement(nums[len(nums)//2:])
    if a == b:
        return a
    return [b, a][nums.count(a) > len(nums)//2]

# the idea here is if a pair of elements from the
# list is not the same, then delete both, the last
# remaining element is the majority number
def majorityElement(self, nums):
    count, cand = 0, 0
    for num in nums:
        if num == cand:
            count += 1
        elif count == 0:
            cand, count = num, 1
        else:
            count -= 1
    return cand


'''
# 141. Linked List Cycle I
# no use of dummy node

Method 1
Best solution:
#  Tortoise and hare algorithm
The "trick" is to not check all the time whether
we have reached the end but to handle it via an exception.
"Easier to ask for forgiveness than permission."
'''
# When initialize, fast is one step ahead of slow
def hasCycle1(head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False

'''
Method 2
'''
def has_cycle2(head):
    if head is None: return False
    slow, fast = head, head.next
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            return True
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

'''
# 142. Linked List Cycle II
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
        arriving H of the cycle, in order to find out where they meet,
        the problem becomes like this: slow starts at E while fast starts at H,
        and fast travels twice as quickly as slow. So when fast catches slow,
        fast must have travelled one cycle already.
        Suppose they meet at k: L-K = (L + (L-K-H))/2
        ==> K = H
        So the problem evolves into solving K.
        Because slow forwards one step each time, so we put slow to head,
        make it and fast both travel to E at the speed of one step a time,
        and return slow when they meet again.


# Considering dummy node and the self-defined classes here:
#O(n) 最多跑2n
'''
def detectCycle(head):
    '''
    >>> ll1= SLL(1, 2)
    >>> ll1[1].next = ll1[0]
    >>> detectCycle(ll1)
    0
    >>> ll2 = SLL(4, 8, 1, 3)
    >>> ll2[-1].next = ll2[1]
    >>> detectCycle(ll2)
    1

    >>> ll3 = SLL(2, 3, 4, 5)
    >>> detectCycle(ll3)
    -1
    '''

    try:
        slow, fast = head.head.next, head.head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                slow = head.head.next
                break
        else:
            return -1
        while slow != fast:
            slow, fast = slow.next, fast.next
            index += 1
        return index
    except:
        return -1

'''
leetcode solution format:
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
                return null
            while slow != fast:
                slow, fast = slow.next, fast.next
            return slow
        except:
            return None

'''
19. Remove Nth Node From End of List

Note: Given n will always be valid.

# Two-pointer method: Make fast take n steps first,
then check whether fast is None, if is, then the length
of the list is n, we remove the Nth node from end of list
which equals to the head of the node, so we return head.next;
if not, then we make slow and fast keep running one step a time
until reaching the end of the list (when fast.next == None), thus
slow and fast are at a distance of N, that way, slow.next is the node
to delete, so we reconnect the list and return head.
'''
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = fast = head
        for i in range(n):
            if fast != None:
                fast = fast.next
        #Crucial step:
        #If after taking n steps fast is None,
        # it means the length of the list is n,
        # so we only need to delete the first element(return head.next)
        if not fast:
            return head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return head

'''
237. Delete Node in a Linked List
Delete Node in Linked List: except the tail, given only access to that node.
'''
def delete_node(node):
    node.value = node.next.value
    node.next = node.next.next

'''
Split in Half
Give a list, split in into two lists, one for the front half, and one for the back half.
If the length is odd, then the front half contains one more node than the back half.
'''
def split(head):
    if not head: return None
    slow = fast = head
    front_end = slow
    while fast:
        front_end = slow
        slow = slow.next
        fast = fast.next.next if fast.next else None
    back = slow
    front_end.next = None
    front = head
    return (front, back)


'''
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list.

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''
# iteratively
# O(m + n)
def mergeTwoLists1(l1, l2):
    dummy = cur = Node(0)
    while l1 and l2:
        if l1.value < l2.value:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

# 23. Merge k Sorted Lists
# divide and conquer solution, Time: O(Nlogk), Space: O(1)
#Recursive solution:
def mergeKLists(self, lists):
    if not lists:
        return
    if len(lists) == 1:
        return lists[0]
    mid = len(lists)//2
    l = self.mergeKLists(lists[:mid])
    r = self.mergeKLists(lists[mid:])
    return self.merge(l, r)

#Iterative solution
def mergeKLists_iter(self, lists):
    if not lists:
        return
    if len(lists) == 1:
        return lists[0]
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = self.merge(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else lists



def merge(self, l, r):
    dummy = cur = ListNode(0)
    while l and r:
        if l.val < r.val:
            cur.next = l
            l = l.next
        else:
            cur.next = r
            r = r.next
        cur = cur.next
    cur.next = l or r
    return dummy.next

'''
# 160. Intersection of Two Linked Lists
Method 1: Use len(), Time: O(n),  Space: O(1)
Make A and B have the same length and find the node when A == B
'''
def getIntersectionNode(headA, headB):
    curA, curB = headA, headB
    lenA, lenB = 0, 0
    while curA is not None:
        lenA += 1
        curA = curA.next
    while curB is not None:
        lenB += 1
        curB = curB.next
    curA, curB = headA, headB
    if lenA > lenB:
        for i in range(lenA-lenB):
            curA = curA.next
    elif lenB > lenA:
        for i in range(lenB-lenA):
            curB = curB.next
    while curB != curA:
        curB = curB.next
        curA = curA.next
    return curA

#Method 2: Make A and B both run the same distance and they will finally meet at the intersection node
def getIntersectionNode2(headA, headB):
    if headA and headB:
        A, B = headA, headB
        while A!=B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A



#41. First Missing Positive(Optional)
