'''
用python list构建一个最小堆

'''
class MinHeap():
    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        self._elements = [None]*maxsize
        self._count = 0

    def __len__(self):
        return self._count

    # O(logn), logn为完全二叉树的高度
    def insert(self, value):
        # 检查堆满了没有：
        if self._count >= self.maxsize:
            raise Exception('Heap is full, cannot insert new element!')
        self._elements[self._count] = value
        self._count += 1
        self._upheap(self._count - 1) #维持堆的特性

    def _upheap(self, idx):
        # base case: 堆顶元素停止递归
        if idx > 0:
            parent = (idx -1)//2
            if self._elements[idx] < self._elements[parent]:
                self._elements[idx], self._elements[parent] = self._elements[parent], self._elements[idx]
                self._upheap(parent) #继续对父节点递归 upheap

    # O(logn), logn为完全二叉树的高度
    def extract(self):
        if self._count <= 0:
            raise Exception('Heap is empty, cannot extract any element!')
        top = self._elements[0]
        self._count -= 1 #因为只会在self._count内遍历，所以不需要再手动将最后一位设置为None
        #把最右下角的节点换到堆顶
        self._elements[0] = self._elements[self._count]
        self._downheap(0)
        return top

    def _downheap(self, idx):
        left, right = 2*idx + 1, 2*idx + 2
        Min = idx #记录父、左子、右子三个节点最小值的index
        #如果存在左child并且其值小于父节点值
        if left < self._count and self._elements[left] < self._elements[Min]:
            if right < self._count and self._elements[right] < self._elements[left]:
                Min = right
            Min = left
        if Min != idx: #base case: 如果 Min = idx，即parent节点，则没有child节点，结束递归
            self._elements[idx], self._elements[Min] = self._elements[Min], self._elements[idx]
            self._downheap(Min)

    def __str__(self):
        return str(self._elements[:self._count])

def test_minheap(n):
    h = MinHeap(n)
    for i in reversed(range(n)):
        h.insert(i)
    print(h)
    for i in range(n):
        assert i == h.extract()
        print(h)

if __name__ == '__main__':
    test_minheap(5)
