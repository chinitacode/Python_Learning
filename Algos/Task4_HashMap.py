'''
【散列表（哈希表）】
1. 实现一个基于链表法解决冲突问题的散列表
2. 实现一个 LRU 缓存淘汰算法

    1. 实现一个基于链表法解决冲突问题的散列表
    散列表(hash table)是实现字典操作的一种有效的数据结构。尽管最坏的情况下，
    散列表中查找一个元素的时间与链表中查找的时间相同，达到了O(n)。
    然而实际应用中，散列的查找的性能是极好的。在一些合理的假设下，
    在散列表中查找一个元素的平均时间是O(1)。

    Basic CRUD(Create, Retrieve, Update and Delete)： O(1)
    1. Hash collisions: (The generated hashcodes or index might be the same.)
        Ideally, the hash function will assign each key to a unique bucket,
        but most hash table designs employ an imperfect hash function,
        which might cause hash collisions where the hash function
        generates the same index for more than one key.

    Solutions:
        1. 开放寻址法 Open addressing:
           所有的元素都存放在散列表里。当查找某个元素时，要系统地检查所有的表项，
           直到找到所需的元素，或者最终查明该元素不在表中。
           不像链表法，这里既没有链表，也没有元素存放在散列表外。
           因此在开放寻址法中，散列表可能会被填满，以至于不能插入任何新的元素。
           -线性探查 Linear probing:
                    一直找下一个可以放的槽 O(n)
                    Cause primary clustering
           -二次探查 Quadratic probing(Better):
                    利用二次函数来查找下一个可以放的槽
                    如若冲突，把key放到递进2的幂的槽里
                    Cause secondary clustering
           -双重散列 Double hashing(Best):

        2. 链接法 Separated chain (= Linked List)
           以链表的方式把冲突的元素往链表中插。 O(n)

    Python字典实现:
    Python是使用开放寻址法中的二次探查来解决冲突的。
    如果使用的满载率超过数组大小的2/3，就申请更大的容量。
    原key的hashcode不变，但是因为size变了，则index = hashcode % size也变了(Rehash)
    数组大小较小的时候resize为*4，较大的时候resize*2。
    实际上是用左移的形式。

    Amortized O(1)

    *满载率load factor = #item / #size

    Java:链接法(两个满载率：0.75， 0.5)

'''
class chained_hash:
    def __init__(self,T=[],size=0):
        if len(T)==0:
            self.T=[None for i in range(size)]
        else:
            self.T=T
        self.size=size
    def search(self,k):
        if self.T[self.hash_h(k)]!=None:
            x=self.T[self.hash_h(k)].list_search(k)
            return x
        return None
    def insert(self,x):
        if self.T[self.hash_h(x.key)]==None:
            self.T[self.hash_h(x.key)]=DoublyLinkedList(x)
        else:
            self.T[self.hash_h(x.key)].list_insert(x)
    def delete(self,x):
        self.T[self.hash_h(x.key)].list_delete(x)
    def hash_h(self,key):
        return key%12

class Node:
    def __init__(self,key):
        self.key=key

#####双向链表####
class DoublyNode:
    def __init__(self,n_prev,n_next,key):
        self.prev=n_prev
        self.next=n_next
        self.key=key

class DoublyLinkedList:
    def __init__(self,head):
        self.head=head
    def list_search(self,k):
        x=self.head
        while x !=None and x.key!=k:
            x=x.next
        return x
    def list_insert(self,x):
        x.next=self.head
        if self.head != None:
            self.head.prev=x
        self.head=x
        x.prev=None
    def list_delete(self,x):
        if x.prev!=None:
            x.prev.next=x.next
        else:
            self.head=x.next
        if x.next !=None:
            x.next.prev=x.prev

'''
>>> T=[]
>>> x=DoublyNode(None,None,13)
>>> ch=chained_hash(T,12)
>>> ch.insert(x)
>>> x=DoublyNode(None,None,25)
>>> ch.insert(x)
>>> y=ch.search(25)
>>> y.key
25
>>> ch.delete(y)
>>> ch.T[1].head
<__main__.DoublyNode object at 0x038E8890>
>>> ch.T[1].head.key
13
>>> ch.T[1].head.next
>>> 
'''

'''
    2. 实现一个 LRU 缓存淘汰算法
    LRU：least recently used，最近最少使用算法。
    根据数据的历史访问记录来进行淘汰数据，
    其核心思想是“如果数据最近被访问过，那么将来被访问的几率也更高”。
    其实就是按使用时间倒排序，然后从尾部删除元素。
    它的使用场景是：在有限的空间中存储对象时，当空间满时，
    会按一定的原则删除原有的对象，常用的原则（算法）有LRU，FIFO，LFU等。
    在计算机的Cache硬件，以及主存到虚拟内存的页面置换，还有Redis缓存系统中都用到了该算法。

    实现原理:
    利用list记录key的次序，每次set,或get操作将key插入到list首位。
    缓冲区满之后再出现set操作，移除末尾的key。
    使用Python3 ，key in dict判断key是否出现过。
'''
class LRUcache:
    def __init__(self, size=3):
        self.cache = {}
        self.keys = []
        self.size = size

    def get(self, key):
        if key in self.cache:
            self.keys.remove(key)
            self.keys.insert(0, key)
            return self.cache[key]
        else:
            return None

    def set(self, key, value):
        if key in self.cache:
            self.keys.remove(key)
            self.keys.insert(0, key)
            self.cache[key] = value
        elif len(self.keys) == self.size:
            old = self.keys.pop()
            self.cache.pop(old)
            self.keys.insert(0, key)
            self.cache[key] = value
        else:
            self.keys.insert(0, key)
            self.cache[key] = value

if __name__ == '__main__':
    test = LRUcache()
    test.set('a',2)
    test.set('b',2)
    test.set('c',2)
    test.set('d',2)
    test.set('e',2)
    test.set('f',2)
    print(test.get('c'))
    print(test.get('b'))
    print(test.get('a'))
