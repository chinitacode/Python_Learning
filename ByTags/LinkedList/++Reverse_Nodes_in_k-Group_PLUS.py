'''
字节跳动版
https://juejin.im/post/5dc10fcb6fb9a04a903a6707
给定单链表的头结点 head，实现一个调整链表的函数，从链表尾部开始，
以 K 个结点为一组进行逆序翻转，头部剩余结点不足一组时，不需要翻转。
（不能使用队列或者栈作为辅助）
leetcode-25 是从头结点开始，以 K 个结点一组进行翻转。而字节跳动这道题，是从尾结点开始。
只是多了一个从尾结点开始分组翻转的条件，这道题的难度就增加了。

[Method 1]:
先将原始链表，进行一次「链表翻转」，再进行「K 个一组翻转链表」，最后再做一次「链表翻转」还原链表，就得出了需要的结果。

'''
ListNode revserseKGroupPlus(ListNode head, int k) {  
#翻转链表  
head = reverseList(head);  
# K 个一组翻转链表  
head = reverseKGroup(head, k);  
# 翻转链表  
head = reverseList(head);  
return head;
}


'''


'''
[Method 2]:
回忆一下 leetcode 第 25 题，它和这道题的差异，主要来自于，对不足一组的链表结点的处理。
leetcode-25 是从头结点开始处理，所以多出来的结点会在尾部，而字节跳动这道题则正好相反，余下的结点会在头部。
但是它们同时也有一种特殊情况，就是 K 个一组进行分组时，这里的 K 正好可以完整的分组，一个不多，一个不少的分成 N 组。
当链表结点数量正好为 K * N 时，那么又回到了我们熟悉的 leetcode-25 题了。
如果我们先将原始结点进行处理，找出它正好可以整除 K 的起始结点 offset，
将这个起始结点 offset 的子链表，再进行 K 个一组进行翻转链表，最后把它拼接回原始链表，就完成了这道题。
这个过程，需要额外定义两个结点，第一个满足 K 个分组条件的 offset 结点，
以及 offset 的前驱结点 prev 结点，prev 结点主要是用来拼接翻转后的两个链表，让其不会出现链表断裂的问题。

这其中还涉及到一些简单的链表运算，例如求链表的长度，这里就不展开说了，直接上核心代码，
逻辑都在注释里，我们先定义一个 reverseKGroupPlus() 方法。
'''
public ListNode reverseKGroupPlus(ListNode head, int k) {
    if (head == null || k <= 1) return head;
    // 计算原始链表长度
    int length = linkedLength(head);
      if (length < k)
         return head;
    // 计算 offset
    int offsetIndex = length % k;
      // 原始链表正好可以由 K 分为 N 组，可直接处理
    if (offsetIndex == 0) {
        return reverseKGroup(head, k);
    }
    // 定义并找到 prev 和 offset
    ListNode prev = head, offset = head;
    while (offsetIndex > 0) {
        prev = offset;
        offset = offset.next;
        offsetIndex--;
    }
    // 将 offset 结点为起始的子链表进行翻转，再拼接回主链表
    prev.next = reverseKGroup(offset, k);
    return head;
}

'''
'''
注意当链表长度正好可以用 K 分为 N 组时，我们直接处理，否者才需要后续复杂的逻辑。
代码的注释足够清晰了，在脑子里过一遍代码的执行流程应该能明白，为了帮助大家理解，我又画了个示意图。
假设以 head 为头结点的链表长度是 10，K 为 4 时，那么计算下来 offset Index 就是 2。

找到 prev 和 offset 结点后，就可以将以 offset 结点为头结点的子链表，进行 K 个一组翻转链表的操作了。
此时，head 结点为起始的链表，就是我们计算后的结果。
'''
