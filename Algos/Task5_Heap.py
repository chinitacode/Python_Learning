'''
【堆】Heap/Priority Queue
实现一个小顶堆、大顶堆、优先级队列
实现堆排序

[完美二叉树]：所有叶子节点都在同一层，毫无间隙地填充了H层。

[满二叉树]：每个内部节点（非叶节点）都包含两个孩子。

[完全二叉树]：
·二叉树(Binary Tree): 二叉树左右侧连接为空或者节点。
·完全树(Complete tree): 除了最底层，完全对称平衡。

完全二叉树特性：
1.有N个节点的完全树的高度是： logN  (root的高度为0算)
2.有N个节点的完全树的层数是：高度+1 = logN + 1;
  每一层填满后的总节点数为2^n - 1, 如三层的完全对称平衡树的总节点个数为1+2+4 = 2^3 -1 = 7。
3.反推，如果高度为h，则总节点数至少为2^(h-1)个(至少比高度为h-1的完全对称平衡树总节点个数多1)，并且小于(2^h - 1)。
 (当N是2的指数时层数才会增加)。
4.堆可以使用list实现，就是按照层序遍历顺序将每个节点上的值存放在数组中。
  则对于任何一个index为i的node,它的parent的index为(i-1)//2;
  其left child的index为2*i + 1(如果存在的话); 右child为2*i + 2(如果存在的话)。

 堆的操作：
 [100,84,71,60,23,12,29,1,37,41]
 1.insert：
   往最大堆(max heap)里添加一个元素，假设为90，我们在使用数组实现的时候直接使用append()方法将值添加到数组的最后。
   这时候我们需要维持最大堆的特性，添加的新值90首先被放到堆的最后，然后与父节点的值作比较。
   如果比父节点值大，则交换位置。
   这里涉及到的问题是子节点与父节点之间的关系。

   # 堆中父节点i与子节点left、right的位置关系
    parent = int((i-1) // 2)    # 取整
    left = 2 * i + 1
    right = 2 * i + 2

    # 已知子节点的位置j，求父节点的位置
    parent = int((j-1)//2)
    使用递归的方式，向上比较，直到根节点。
    最多需要换logn(即树的高度)次。

2.delete:
  对于堆的删除操作，永远是删除堆顶(先对优先级最高的进行操作)，然后重构堆。
  相当于是把优先级别最高的事件完成后，要把下一个优先级别最高的事件提上来。

  当我们把最大或者最小的值从堆中弹出，为了维持堆的特性，要使用shift-down操作。
  因为最大堆、最小堆的最值都在根节点，当弹出并返回根节点的值后，为了维持堆的特性，我们先将最后一个位置上的值放到根节点中。
  然后比较它与它的两个子节点中三个值的大小，选择最大的值放到父节点上。
  同理，我们这里也是使用递归的方式向下比较。
  这里涉及到两个问题：
  # 父节点的位置，left，rigth为左右子节点的位置
  left = 2 * ndx + 1
  right = 2 * ndx + 2
  交换位置要满足几个条件条件，比如跟左子节点交换的条件:
  ·存在左子节点，
  ·左子节点大于右子节点，
  ·左子节点大于父节点。
  [Time]:log(N)

[构建堆的时间复杂度]：O(n)
对于有N个节点的最大顶堆，高度为H = logN,
最后一层每个父节点(整个堆中的最小堆，只由3个节点构成)最多需要下调1次，
倒数第二层最多只需要下调2次,...,顶点最多需要下调H次；
而最后一层的父节点共有2^(H-1)个,倒数第二层有2^(H-2),...,顶点只有2^0=1个,
因此总的时间复杂度为 s = 1*2^(H-1) + 2*2^(H-2) + ... + (H-1)*2^1 + H*2^0,
将H = logN代入后,s = 2N - log(N), 近似O(N)

[最大堆]：
'''
class Array(object):
    #Achieve an Array by Python list
    def __init__(self, size = 32):
        self._size = size
        self._items = [None]*size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    # 清空数列（把数列里的值全部设置为None）
    def clear(self, value = None):
        for i in range(self._size):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

class MaxHeap(object):
    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('Heap is full!')
        self._elements[self._count] = value
        self._count += 1
        self._upheap(self._count - 1) #维持堆的特性

    def _upheap(self, idx):
        if idx > 0:
            parent = (idx - 1)//2
            if self._elements[idx] > self._elements[parent]:
                self._elements[idx], self._elements[parent] = self._elements[parent], self._elements[idx]
                self._upheap(parent) #递归，直到换到堆顶idx为0时停止

    def extract(self):
        if self._count <= 0:
            raise Exception('Heap is empty!')
        top = self._elements[0] #保存堆顶
        self._count -= 1 #因为只会在self._count内遍历，所以不需要再手动将最后一位设置为None
        #把最右下角的节点换到堆顶
        self._elements[0] = self._elements[self._count] #这里必须用self._count作为尾部index,因为当Array可能没填满，而且因为上一步self._count已经减了1，所以可以用它记录之前的尾部元素。
        self._downheap(0)
        return top

    def _downheap(self, idx):
        left, right = 2*idx + 1, 2*idx + 2
        Max = idx #记录父、左子、右子三个节点最大值的index
        #如果存在左child并且其值大于父节点值
        '''*注!*：根据完全二叉树的特性，要么就左右child一起存在，要么就只存在左child！'''
        if left < self._count and self._elements[left] > self._elements[Max]:
            #如果存在右child并且其值大于左child
            if right < self._count and self._elements[left] < self._elements[right]:
                Max = right
            Max = left
        if Max != idx:
            self._elements[idx], self._elements[Max] = self._elements[Max], self._elements[idx]
            self._downheap(Max)

    def __str__(self):
        elements = [str(self._elements[i]) for i in range(self._count)]
        return '[' + ','.join(elements) + ']'

def test_maxheap(n):
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    print(h)
    for i in reversed(range(n)):
        assert i == h.extract()
        print(h)

if __name__ == '__main__':
    test_maxheap(5)

'''
[最小堆]：
用python自带的list来构建：
'''
class MinHeap(object):
    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        self._elements = [None]*maxsize
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('Heap is full!')
        self._elements[self._count] = value
        self._count += 1
        self._upheap(self._count - 1) #维持堆的特性

    def _upheap(self, idx):
        if idx > 0:
            parent = (idx - 1)//2
            if self._elements[idx] < self._elements[parent]:
                self._elements[idx], self._elements[parent] = self._elements[parent], self._elements[idx]
                self._upheap(parent) #递归，直到换到堆顶idx为0时停止

    def extract(self):
        if self._count <= 0:
            raise Exception('Heap is empty!')
        top = self._elements[0] #保存堆顶
        self._count -= 1 #因为只会在self._count内遍历，所以不需要再手动将最后一位设置为None
        #把最右下角的节点换到堆顶
        self._elements[0] = self._elements[self._count] #这里必须用self._count作为尾部index,因为当Array可能没填满，而且因为上一步self._count已经减了1，所以可以用它记录之前的尾部元素。
        self._downheap(0)
        return top

    def _downheap(self, idx):
        left, right = 2*idx + 1, 2*idx + 2
        Min = idx #记录父、左子、右子三个节点最小值的index
        #如果存在左child并且其值小于父节点值，则更新 Max的index
        '''*注!*：根据完全二叉树的特性，要么就左右child一起存在，要么就只存在左child！'''
        if left < self._count and self._elements[left] < self._elements[Min]:
            #如果存在右child并且其值大于左child
            if right < self._count and self._elements[left] > self._elements[right]:
                Min = right
            Min = left
        if Min != idx:
            self._elements[idx], self._elements[Min] = self._elements[Min], self._elements[idx]
            self._downheap(Min)

    def __str__(self):
        return str(self._elements[:self._count])

def test_minheap(n):
    h = MinHeap(n)
    for i in reversed(range(n)):
        h.add(i)
    print(h)
    for i in range(n):
        assert i == h.extract()
        print(h)

if __name__ == '__main__':
    test_minheap(5)


'''
[堆排序]：
对于一个length为N的数列，我们先构建堆，需要O(N)的时间，然后把堆顶(最大值)一个个地pop到输出结果中，
(delete操作是O(logN)的)，则总共需要O(NlogN)的时间复杂度，O(N)的空间(但也有In-place的解法)。

[Python中的heapq模块]
这个模块提供了的堆是一个最小堆，索引值从0开始。

而很多教材中都使用最大堆作为教学的例子，因为其排序是稳定的，而最小堆排序是不稳定的。
Python中创建一个堆可以直接使用list的创建方式heap = [], 或者使用heapify()函数将一个存在的列表转为堆。

heapq是二叉堆，通常用普通列表实现，能在O(logN)时间内插入和获取最小的元素。

这个模块提供了下面几种堆的操作：
-heapq.heappush(heap, item)
往堆中插入一个值，同时要保持为最小堆。

-heapq.heappop(heap)
返回堆中的最小值，并把它从堆中删除，同时保持为最小堆；如果堆为空，发生 IndexError。
直接通过heap[0]可以获取最小值并不从堆中把它删除。

-heapq.heappushpop(heap, item)
向堆中插入值后再弹出堆中的最小值，这个函数的速度比直接使用heappush()后再heappop()的效率更加高。

-heapq.heapreplace(heap, item)
弹出和返回堆中的最小值再插入一个新的值。堆的大小没有改变。如果堆为空，产生 IndexError。
这一个操作也比直接使用heappop()再heappush()的效率更加高，尤其适合使用在固定堆大小不变的情况。
与上一个函数相比，这个函数返回的值可能要比将要插入到堆的值大。

-heapq.heapify(x)
将一个list转为最小堆，线性时间复杂度，O(n).

'''
from heapq import heappush,heappop
heap = []
data = [1,3,5,7,9,2,4,6,8,0]
for item in data:
    heappush(heap, item)
print(heap) #[0, 1, 2, 6, 3, 5, 4, 7, 8, 9]

#Heap Sort
ordered = []
while heap:
    ordered.append(heappop(heap))
print(ordered) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Or:
import heapq
data = [1,3,5,7,9,2,4,6,8,0]
heapq.heapify(data)
print(data) #[0, 1, 2, 6, 3, 5, 4, 7, 8, 9]

'''
[Extension]:
-heapq.merge(*iterables) :
Merge multiple sorted inputs into a single sorted output
(for example, merge timestamped entries from multiple log files).
Returns an iterator over the sorted values.

Similar to sorted(itertools.chain(*iterables)) but returns an iterable,
does not pull the data into memory all at once,
and assumes that each of the input streams is already sorted (smallest to largest).

E.G.
from heapq import merge
def mergeArray(arr1,arr2):
    return list(merge(arr1, arr2))

if __name__ == "__main__":
    arr1 = [1,3,4,5]
    arr2 = [2,4,6,8]
    print mergeArray(arr1, arr2)
Output:
[1, 2, 3, 4, 4, 5, 6, 8]


-heapq.nlargest(n, iterable[, key])
Return a list with the n largest elements from the dataset defined by iterable.
key, if provided, specifies a function of one argument that is used
to extract a comparison key from each element in the iterable:
key=str.lower Equivalent to: sorted(iterable, key=key, reverse=True)[:n]


-heapq.nsmallest(n, iterable[, key])
Return a list with the n smallest elements from the dataset defined by iterable.
key, if provided, specifies a function of one argument
that is used to extract a comparison key from each element in the iterable:
key=str.lower Equivalent to: sorted(iterable, key=key)[:n]

The latter two functions perform best for smaller values of n.
For larger values, it is more efficient to use the sorted() function.
Also, when n==1, it is more efficient to use the builtin min() and max() functions.
'''
import heapq
li1 = [6,7,9,4,3,5,8,10,1]
heapq.heapify(li1)
print('The 3 largest numbers in the list are: ', heapq.nlargest(3,li1))
#The 3 largest numbers in the list are: [10,9,8]

print('The 3 smallest numbers in the list are: ', heapq.nsmallest(3,li1))
#The 3 largest numbers in the list are: [1,3,4]


#对于没有可比性的数据结构，如dictionary,可以传入lambda函数:
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

if __name__ == '__main__':
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    #[{'name': 'YHOO', 'price': 16.35, 'shares': 45},
    #{'name': 'FB', 'price': 21.09, 'shares': 200},
    #{'name': 'HPQ', 'price': 31.75, 'shares': 35}]

'''
Class Objects
Python isn't strongly typed, so we can save anything we like:
just as we stored a tuple of (priority,thing) in previous section.
We can also store class objects if we override cmp() method:
# Override __lt__ in Python 3, __cmp__ only in Python 2
'''
import heapq
class Skill(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New Level:', description)
        return
    #def __cmp__(self, other):
        #return cmp(self.priority, other.priority)
    def __lt__(self, other):
        return self.priority < other.priority
    def __repr__(self):
        return str(self.priority) + ": " + self.description


if __name__ == '__main__':
    s1 = Skill(5, 'Proficient')
    s2 = Skill(10, 'Expert')
    s3 = Skill(1, 'Novice')

    l = [s1, s2, s3]

    heapq.heapify(l)
    print("The 3 largest numbers in list are : ",end="")
    print(heapq.nlargest(3, l))

    while l:
        item = heappop(l)
        print(item)

    '''
    ###Testing results###
    New Level: Proficient
    New Level: Expert
    New Level: Novice
    The 3 largest numbers in list are : [10: Expert, 5: Proficient, 1: Novice]
    1: Novice
    5: Proficient
    10: Expert
    '''

'''
[优先级队列(Priority Queue)]
 队列的特点是先进先出。通常都把队列比喻成排队买东西，大家都很守秩序，先排队的人就先买东西。
 但是优先队列有所不同，它不遵循先进先出的规则，而是根据队列中元素的优先权，优先权最大的先被取出。


优先队列是一种用来维护一组元素构成的结合S的数据结构，其中每个元素都有一个关键字key，
元素之间的比较都是通过key来比较的。优先队列包括最大优先队列和最小优先队列。
优先队列的应用比较广泛，比如作业系统中的调度程序，当一个作业完成后，
需要在所有等待调度的作业中选择一个优先级最高的作业来执行，并且也可以添加一个新的作业到作业的优先队列中。

优先队列的实现中，我们可以选择堆数据结构，最大优先队列可以选用大堆，最小优先队列可以选用小堆来实现。

特点：
☺ 优先级队列是0个或多个元素的集合，每个元素都有一个优先权或值。
☺当给每个元素分配一个数字来标记其优先级时，可设较小的数字具有较高的优先级，
这样更方便地在一个集合中访问优先级最高的元素，并对其进行查找和删除操作。
☺对优先级队列，执行的操作主要有：(1)查找，(2)插入，(3)删除。
☺ 在最小优先级队列(min Priority Queue)中，查找操作用来搜索优先权最小的元素，删除操作用来删除该元素。
☺在最大优先级队列(max Priority Queue)中，查找操作用来搜索优先权最大的元素，删除操作用来删除该元素。
☺ 插入操作均只是简单地把一个新的元素加入到队列中。

好处：
·自动排序

优先队列的基本操作
q.size();//返回q里元素个数
q.empty();//返回q是否为空，空则返回1，否则返回0
q.push(k);//在q的末尾插入k
q.pop();//删掉q的第一个元素
q.top();//返回q的第一个元素
q.back();//返回q的末尾元素


1.heapq模块是在Python中不错的优先级队列实现。
由于heapq在技术上只提供最小堆实现，因此必须添加额外步骤来确保排序稳定性，
以此来获得“实际”的优先级队列中所含有的预期特性。

'''
import heapq
q = []
heapq.heappush(q, (2, 'code'))
heapq.heappush(q, (1, 'eat'))
heapq.heappush(q, (3, 'sleep'))
print(q) #[(1, 'eat'), (2, 'code'), (3, 'sleep')]
while q:
    next_item = heapq.heappop(q)
    print(next_item)
# 结果：
#   (1, 'eat')
#   (2, 'code')
#   (3, 'sleep')

'''
2.queue.PriorityQueue——Python 优先队列
queue.PriorityQueue这个优先级队列的实现在内部使用了heapq，时间和空间复杂度与heapq相同。
区别在于PriorityQueue是同步的，提供了锁语义来支持多个并发的生产者和消费者。
在不同情况下，锁语义可能会带来帮助，也可能会导致不必要的开销。
不管哪种情况，你都可能更喜欢PriorityQueue提供的基于类的接口，而不是使用heapq提供的基于函数的接口。

>>> from queue import PriorityQueue
>>> q = PriorityQueue()
>>> q.put((2, 'code'))
>>> q.put((1, 'eat'))
>>> q.put((3, 'sleep'))
>>> q
<queue.PriorityQueue object at 0x02C2C6D0>
>>> while not q.empty():
	print(q.get())
(1, 'eat')
(2, 'code')
(3, 'sleep')
>>> q.empty()
True
>>> q.put((3, 'sleep'))
>>> q[0]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    q[0]
TypeError: 'PriorityQueue' object does not support indexing
>>> q.queue
[(3, 'sleep')]

(1).queue.PriorityQueue的基本操作
常用put()（入队列）与get()（出队列），queue（查看队列中的元素）。
put方法要注意方入队列的是一个元组，不要忘记括号，默认情况下队列根据元组的第一个元素进行排序。越小的优先级越低。
get方法是将优先级最低的一个元素出队列
'''
from queue import PriorityQueue as PQ
pq = PQ()
pq.put((2, 'a'))
pq.put((1, 'b'))
pq.queue # output: [(1, 'b'), (2, 'a')]
pq.get() # output: (1, 'b')
pq.queue # output: [(2, 'a')]

'''
(2).按(1)中的例子来说，我希望出队列的是a这个元素。那么该怎么做呢？这需要入队列时将数组取负号即可。
'''
from queue import PriorityQueue as PQ
pq = PQ()
pq.put((-2, 'a'))
pq.put((-1, 'b'))
pq.queue # output: [(-2, 'a'), (-1, 'b')]
pq.get() # output: (-2, 'a')
pq.queue # output: [(-1, 'b')]

'''
(3).入队列时可能会犯的错误
我们自定义一个类A，将两个优先级相同的不同A的实例加入队列中。
'''
from queue import PriorityQueue as PQ
pq = PQ()
class A:
    def __init__(self, val):
        self.val = val
pq.put((1, A(1)))
pq.put((1, A(2))) # error:  '<' not supported between instances of 'A' and 'A

'''
报错的原因是A的实例是不可比较的，在python3中当优先级相同的情况下，将会比较元组的第二值。
所以当你可能向元组中存入不可比较的值，或者当你希望通过入队的顺序控制出队的顺序，
你需要为元组第二个位置增加一个辅助变量，通常为一个自增的变量。
'''
from queue import PriorityQueue as PQ
pq = PQ()
class A:
    def __init__(self, val):
        self.val = val
index = 0
pq.put((1, index, A(1)))
index += 1
pq.put((1, index, A(2)))
#现在就不会报错了，而保证了入队的顺序与出队的顺序相同。

'''
#[queue.PriorityQueue的源码]
'''
class PriorityQueue(Queue):
    '''Variant of Queue that retrieves open entries in priority order (lowest first).

    Entries are typically tuples of the form:  (priority number, data).
    '''

    def _init(self, maxsize):
        self.queue = []

    def _qsize(self):
        return len(self.queue)

    def _put(self, item):
        heappush(self.queue, item)

    def _get(self):
        return heappop(self.queue)

'''
[实现自己的优先级队列类]:
'''
#1.最小优先级队列(min Priority Queue)
import heapq

class MinPriorityQueue:

    def __init__(self):
        self._index = 0
        self.queue = []

    def push(self, priority, val):
        heapq.heappush(self.queue, (priority, self._index, val))
        self._index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]
'''
#Testing results
>>> minq = MinPriorityQueue()
>>> minq.push(2,'prepare lunch ingredients')
>>> minq.push(1,'do yoga')
>>> minq.push(3,'bring breakfast')
>>> for i in range(3):
	print(minq.queue)
	print(minq.pop())

[(1, 1, 'do yoga'), (2, 0, 'prepare lunch ingredients'), (3, 2, 'bring breakfast')]
do yoga
[(2, 0, 'prepare lunch ingredients'), (3, 2, 'bring breakfast')]
prepare lunch ingredients
[(3, 2, 'bring breakfast')]
bring breakfast
'''

#2.最大优先级队列(max Priority Queue)
class MaxPriorityQueue(object):
    def __init__(self):
        self._queue = []        #创建一个空列表用于存放队列
        self._index = 0        #指针用于记录push的次序

    def push(self, item, priority):
        """队列由（priority, index, item)形式的元祖构成"""
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]    #返回拥有最高优先级的项

class Item(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item: {!r}'.format(self.name)

if __name__ == '__main__':
    q = MaxPriorityQueue()
    q.push(Item('foo'), 5)
    q.push(Item('bar'), 1)
    q.push(Item('spam'), 3)
    q.push(Item('grok'), 1)
    for i in range(4):
        print(q._queue)
        print(q.pop())

'''
[(-5, 0, Item: 'foo'), (-1, 1, Item: 'bar'), (-3, 2, Item: 'spam'), (-1, 3, Item: 'grok')]
Item: 'foo'
[(-3, 2, Item: 'spam'), (-1, 1, Item: 'bar'), (-1, 3, Item: 'grok')]
Item: 'spam'
[(-1, 1, Item: 'bar'), (-1, 3, Item: 'grok')]
Item: 'bar'
[(-1, 3, Item: 'grok')]
Item: 'grok'


[关键要点]
Python提供了几种优先队列实现可以使用。
queue.PriorityQueue是其中的首选，具有良好的面向对象的接口，从名称就能明白其用途。
如果想避免queue.PriorityQueue的锁开销，那么建议直接使用heapq模块。
'''
