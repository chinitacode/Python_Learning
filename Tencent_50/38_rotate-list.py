'''
61. Rotate List [Medium]

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:
Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:
Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

[Method 1]: Iteration + Hash table
Time: O(n)   Space: O(n)
1.将整个链表的node分别加入哈希表mydict，并得到长度leng;
2.将k值取leng的余数，比如k为4而leng为3时，其实旋转后的结果和k为1是一样的；
3.此外还要注意特殊情况，如k为0时，最终结果都是和没有旋转过的链表；
4.处理完k后找到旋转后的头部node，即倒着找：head_pos = leng - k, 所以头部node为mydict[head_pos];
5.之后只需要做两件事：
    1).断开头部节点前一个节点的链接：
       mydict[head_pos - 1].next = None
    2).将原本的尾部节点与原头部节点链接起来：
       mydict[head + k - 1].next = mydict[0]
6.返回头部node就ok

Runtime: 36 ms, faster than 97.01% of Python3 online submissions for Rotate List.
Memory Usage: 13.8 MB, less than 6.45% of Python3 online submissions for Rotate List.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        node, leng = head, 0
        mydict = {}
        while node:
            mydict[leng] = node
            leng += 1
            node = node.next
        if leng < 1:
            return None
        if k >= leng:
            k = k % leng
        if k == 0:
            return head
        head_pos = leng - k
        mydict[head_pos - 1].next, mydict[head_pos + k - 1].next = None, mydict[0]
        return mydict[head_pos]


'''
[Method 2]: Iteration + circularly linked list
记住head的位置，然后将单向链表搞成环，那么只要将head的位置向右移动(n-k%n)个位置，然后再将环解开成单向链表，最后返回。
Time: O(n), Space: O(1)
Runtime: 40 ms, faster than 85.41% of Python3 online submissions for Rotate List.
Memory Usage: 14.1 MB, less than 6.45% of Python3 online submissions for Rotate List.
'''
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        #初始化leng为1因为下面的while循环是从head.next开始的
        node, curr, leng = head, head, 1
        while curr.next:
            leng += 1
            curr = curr.next
        k %= leng
        #得先判断是否需要rotate，再将链表连成环
        if k == 0:
            return head
        curr.next = node
        #-1是要为前一个node断裂链接而做记录
        pos = leng - k - 1
        for _ in range(pos):
            node = node.next
        #先准备好返回的节点
        ans = node.next
        #再断开前一个节点和它的链接
        node.next = None
        return ans

'''
#Or: 不用判断k==0时直接返回head了，依旧循环
Runtime: 32 ms, faster than 99.61% of Python3 online submissions for Rotate List.
Memory Usage: 13.8 MB, less than 6.45% of Python3 online submissions for Rotate List.
'''
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        node = curr = head
        leng = 1
        while curr.next:
            leng += 1
            curr = curr.next
        curr.next = head
        k %= leng
        for _ in range(leng - k - 1):
            node = node.next
        ans = node.next
        node.next = None
        return ans


'''
[Method 3]: Recursion: 直接在已经旋转k-1步后的链表上进行最后一步旋转
Time: O(kn)
Runtime: 52 ms, faster than 12.27% of Python3 online submissions for Rotate List.
Memory Usage: 13.8 MB, less than 6.45% of Python3 online submissions for Rotate List.
'''
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        leng = self.count_leng(head)
        k %= leng
        return self.rotate(leng, head, k)

    def count_leng(self, head):
        leng = 0
        while head:
            head = head.next
            leng += 1
        return leng

    def rotate(self, leng, head, k):
        if k == 0:
            return head
        head = self.rotate(leng, head, k-1)
        node = head
        while node.next.next:
            node = node.next
        ans = node.next
        ans.next = head
        node.next = None
        return ans
