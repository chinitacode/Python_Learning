'''
146. LRU Cache [Medium]
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4



[Method 1]: Dictionary + Doubly Linked List
为了在存取元素时维持O(1)的时间复杂度，只能用双向链表来存数据。
同样为了key in cache 的 O(1)时间复杂度，需要用哈希表来存key值，那么key对应的value就是链表的节点。
即node = self.cache[key], 要get元素的值，则需返回node.val。
[Time]: O(1)
[Space]: O(n)
Runtime: 232 ms, faster than 57.08% of Python online submissions for LRU Cache.
Memory Usage: 22 MB, less than 40.00% of Python online submissions for LRU Cache.
'''
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.cache = dict()
        self.head, self.tail = ListNode(0,0), ListNode(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.delete(node)
        self.add(node)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 如果存在,删掉,重新赋值！
        if key in self.cache:
            self.delete(self.cache[key])
        node = ListNode(key, value)
        self.add(node)
        if self.count > self.capacity:
            self.delete(self.head.next)

    def delete(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        del self.cache[node.key]
        self.count -= 1

    def add(self, node):
        node.next, node.prev = self.tail, self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        self.cache[node.key] = node
        self.count += 1

class ListNode():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''
[Method 2]: OrderedDict
Runtime: 180 ms, faster than 96.15% of Python3 online submissions for LRU Cache.
Memory Usage: 21.8 MB, less than 42.42% of Python3 online submissions for LRU Cache.
'''
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # 说明在缓存中,重新移动字典的尾部
        if key in self.cache:
            self.cache.move_to_end(key)
        return self.cache.get(key, -1)

    def put(self, key: int, value: int) -> None:
        # 如果存在,删掉,重新赋值
        if key in self.cache:
            del self.cache[key]
        # 在字典尾部添加
        self.cache[key] = value
        if len(self.cache) > self.maxsize:
            # 弹出字典的头部(因为存储空间不够了)
            self.cache.popitem(last = False) #FIFO

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
