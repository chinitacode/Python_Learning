'''
【堆】Heap/Priority Queue
实现一个小顶堆、大顶堆、优先级队列
实现堆排序
利用优先级队列合并 K 个有序数组
求一组动态数据集合的最大 Top K
（选做）第三天堆排序学习（复习）



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
        Max = idx #记录父、左子、右子三个节点最大值的index
        #如果存在左child并且其值大于父节点值
        '''*注!*：根据完全二叉树的特性，要么就左右child一起存在，要么就只存在左child！'''
        if left < self._count and self._elements[left] < self._elements[Max]:
            #如果存在右child并且其值大于左child
            if right < self._count and self._elements[left] > self._elements[right]:
                Max = right
            Max = left
        if Max != idx:
            self._elements[idx], self._elements[Max] = self._elements[Max], self._elements[idx]
            self._downheap(Max)

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
'''
