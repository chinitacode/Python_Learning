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

Method1: Doubly Linked List
[分析]
1.用哈希表和双向链表存储数据：每个key对应的value以Node的instance的形式存储在哈希表中，
这样用key in dict时才能满足O(1).
2.增加_add和_delete两个private method，且此两个方法就是普通双向链表的相应方法，
在这里不考虑与哈希表的关系。
3.为了方便在链表里add和delete节点，初始化时加入头部和尾部两个dummy node.
add节点时往尾部加node（重新设置self.head和前最后一个节点的指针）.
delete节点时也只需要修改该节点前后的指针即可.
4.哈希表的get，如果目标存在于缓存中，则不需要修改哈希表，只需要更新链表里节点的位置：
将目标节点置于链表尾部（作为最recent的缓存），即先删除旧的节点，再在尾部加入新节点，否则不存在返回-1。
5.哈希表的put，如果目标的key存在于缓存中，则先从链表中删去旧的节点，在链表里加入新节点，
在哈希表中更新value（有可能同样的key对应不同的val），这时不需要考虑capacity（哈希表的size没发生变化）；
若不存在于缓存中，则在在链表里加入新节点，和在哈希表中更新value（同样的操作：self.cach[key] = node）后，
只需要再delete掉头部的最老的节点。
'''



class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cach = dict()
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cach:
            node = self.cach[key]
            self._delete(node)
            self._add(node)
            return node.val
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cach:
            self._delete(self.cach[key])
        node = Node(key, value)
        self._add(node)
        self.cach[key] = node
        if len(self.cach) > self.capacity:
            n = self.head.next
            self._delete(n)
            del self.cach[n.key]

    def _add(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def _delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


class Node:
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
Method2: OrderedDict
OrderedDict is essentially a HashMap and a Doubly Linked List internally
'''
def __init__(self, capacity):
    self.dic = collections.OrderedDict()
    self.remain = capacity

def get(self, key):
    if key not in self.dic:
        return -1
    v = self.dic.pop(key)
    self.dic[key] = v   # set key as the newest one
    return v

def set(self, key, value):
    if key in self.dic:
        self.dic.pop(key)
    else:
        if self.remain > 0:
            self.remain -= 1
        else:  # self.dic is full
            self.dic.popitem(last=False)
    self.dic[key] = value

'''
Another solution by using dictionary and deque
Note: deque.remove() actually uses O(capacity) Time
If we use OrderedDict,
both get() and put() operations would be O(1) on average. And when we use deque instead,
at least for put() operation, 
when capacity is full and the key we want to push is not in cache, we get O(1) on average.
'''
def __init__(self, capacity):
    self.deque = collections.deque([])
    self.dic = {}
    self.capacity = capacity

def get(self, key):
    if key not in self.dic:
        return -1
    self.deque.remove(key)
    self.deque.append(key)
    return self.dic[key]

def set(self, key, value):
    if key in self.dic:
        self.deque.remove(key)
    elif len(self.dic) == self.capacity:
        v = self.deque.popleft()  # remove the Least Recently Used element
        self.dic.pop(v)
    self.deque.append(key)
    self.dic[key] = value
