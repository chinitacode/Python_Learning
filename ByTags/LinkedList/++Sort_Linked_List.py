'''
字节跳动后端面试计算题目
题目
一个链表，假设第一个节点我们定为下标为1，第二个为2，那么下标为奇数的结点是升序排序，
偶数的结点是降序排序，如何让整个链表有序？（分离链表，合并两个有序链表）
比如：   1 -> 8 -> 3 -> 6 -> 5 -> 4 -> 7 -> 2 -> 9，
最后输出 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9。

思路
[思路1]：先将链表拆分成奇数的链表，和偶数的链表，然后翻转偶数的链表，在合并两个链表。
[思路2]：用双向链表来存储分离后的偶数节点，因为是逆序排列的，所以每个节点往头部加，
就可以省去反转再遍历一遍的时间成本。（奇数位节点不需要用双向链表，则可以不用prev指针）

[思路1]：
'''
# 翻转链表
def reverseList(head):
    p = head
    while p.next:
        t = p.next
        p.next = t.next
        t.next = head
        head = t
    return head

# 奇偶拆分
def splitList(head):
    if not head: # 如果是空的直接返回None,None
        return None,None
    odd_head = head
    if not head.next: # 如果链表长度为1
        return odd_head,None
    even_head = head.next
    p = odd_head
    t = even_head
    while p and t:
        if t:
            p.next = t.next
            p = t.next
        else:
            p.next = None
        if p :
            t.next = p.next
            t = p.next
        else:
            t.next = None
    return odd_head,even_head

# 合并两个有序的链表
def mergeList(odd_head,even_head):
    if not odd_head:
        return even_head
    elif not even_head:
        return odd_head
    result_head = None
    if odd_head.val < even_head.val:
        result_head = odd_head
        result_head.next = mergeList(odd_head.next,even_head)
    else:
        result_head = even_head
        result_head.next = mergeList(odd_head,even_head.next)
    return result_head

def main(head):
    odd_list,even_list = splitList(head)
    even_list = reverseList(even_list)
    result = mergeList(odd_list,even_list)
