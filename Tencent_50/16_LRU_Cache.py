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

[Method 1]: Hashset + Doubly Linked List
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

Runtime: 268 ms, faster than 21.21% of Python3 online submissions for LRU Cache.
Memory Usage: 23.1 MB, less than 6.06% of Python3 online submissions for LRU Cache.
[注]以下代码中实际上将头部和尾部弄反了，新插入的元素应该插入尾部，头部的才是LRU。
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.add(Node(key, value))
        if self.size > self.capacity:
            self.delete(self.tail.prev)

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.cache[node.key]
        self.size -= 1

    def add(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        self.cache[node.key] = node
        self.size += 1


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
[Method 2]: OrderedDict
OrderedDict is essentially a HashMap and a Doubly Linked List internally.
OrderedDict objects

Ordered dictionaries are just like regular dictionaries but they remember
the order that items were inserted.
When iterating over an ordered dictionary,
the items are returned in the order their keys were first added.

class collections.OrderedDict([items])
Return an instance of a dict subclass, supporting the usual dict methods.
An OrderedDict is a dict that remembers the order that keys were first inserted.
If a new entry overwrites an existing entry, the original insertion position is left unchanged.
Deleting an entry and reinserting it will move it to the end.

New in version 2.7.

OrderedDict.popitem(last=True)
The popitem() method for ordered dictionaries returns and removes a (key, value) pair.
The pairs are returned in LIFO order if last is true or FIFO order if false.

In addition to the usual mapping methods,
ordered dictionaries also support reverse iteration using reversed().

Equality tests between OrderedDict objects are order-sensitive
and are implemented as list(od1.items())==list(od2.items()).
Equality tests between OrderedDict objects and other Mapping objects
are order-insensitive like regular dictionaries.
This allows OrderedDict objects to be substituted anywhere a regular dictionary is used.

The OrderedDict constructor and update() method both accept keyword arguments,
but their order is lost because Python’s function call semantics pass-in keyword arguments
using a regular unordered dictionary.

[OrderedDict Examples and Recipes]
Since an ordered dictionary remembers its insertion order,
it can be used in conjunction with sorting to make a sorted dictionary:

# regular unsorted dictionary
>>> d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key
>>> OrderedDict(sorted(d.items(), key=lambda t: t[0]))
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# dictionary sorted by value
>>> OrderedDict(sorted(d.items(), key=lambda t: t[1]))
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

# dictionary sorted by length of the key string
>>> OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])
The new sorted dictionaries maintain their sort order when entries are deleted.
But when new keys are added, the keys are appended to the end and the sort is not maintained.

It is also straight-forward to create an ordered dictionary variant
that remembers the order the keys were last inserted.
If a new entry overwrites an existing entry,
the original insertion position is changed and moved to the end:

class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        OrderedDict.__setitem__(self, key, value)

An ordered dictionary can be combined with the Counter class
so that the counter remembers the order elements are first encountered:

class OrderedCounter(Counter, OrderedDict):
     'Counter that remembers the order elements are first encountered'

     def __repr__(self):
         return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

     def __reduce__(self):
         return self.__class__, (OrderedDict(self),)

[Time]：对于 put 和 get 操作复杂度是 O(1)，
有序字典中的所有操作get/in/set/move_to_end/popitem（get/containsKey/put/remove）都可以在常数时间内完成。
[Space]：O(capacity)因为空间只用于有序字典存储最多 capacity + 1 个元素。
Runtime: 228 ms, faster than 64.78% of Python3 online submissions for LRU Cache.
Memory Usage: 22.8 MB, less than 6.06% of Python3 online submissions for LRU Cache.
'''
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.maxsize = capacity
        self.lrucache = OrderedDict()

    def get(self, key: int) -> int:
        # 说明在缓存中,重新移动字典的尾部
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
        return self.lrucache.get(key, -1)



    def put(self, key: int, value: int) -> None:
        # 如果存在,删掉,重新赋值
        if key in self.lrucache:
            del self.lrucache[key]
        # 在字典尾部添加
        self.lrucache[key] = value
        if len(self.lrucache) > self.maxsize:
            # 弹出字典的头部(因为存储空间不够了)
            self.lrucache.popitem(last = False)

'''
???疑问
Another solution by using dictionary and deque
Note: deque.remove() actually uses O(capacity) Time
If we use OrderedDict, both get() and put() operations would be O(1) on average.
And when we use deque instead, at least for put() operation,
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
