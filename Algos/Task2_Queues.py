# import the linked list class
from Task1_2_LinkedLists import SLL

from Task2_Stack import ArrayStack
'''
【队列】
LIFO： Last in First out
A queue is a data structure with two main operations: enqueue and dequeue.
enqueue: append an element to the tail of the queue
dequeue: remove an element from the head of the queue
队列(queue)也是表，使用队列时插入和删除在不同的端进行。
队列的基本操作是Enqueue(入队)，在表的末端(tail)插入一个元素，
还有出列(Dequeue)，删除表开头的元素。
比起栈只需要保持记录栈顶top，队列需要保持记录top和rear。
1. 用数组实现一个顺序队列
2. 用链表实现一个链式队列
3. 使用堆栈实现一个队列
4. 实现一个循环队列
'''
#1.Queue implementation using List(not considering the capacity of the queue)
class ListQueue:
    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return self.queue == []

    def enqueue(self,x):
        self.queue.append(x)

    def dequeue(self):
        if self.queue:
            head = self.queue[0]
            self.queue.remove(head)
            return head
        else:
            raise IndexError('queue is empty')

    def size(self):
        return len(self.queue)

#2.Queue implementation using Dynamic Array(can resize the queue)
class ArrayQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        # len(self.queue) is the current capacity while len(self._size)
        self.queue = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError( 'Queue is empty' )
        return self.queue[self._front]

    def enqueue(self, e):
        if self._size == len(self.queue):
            self._resize(2 * len(self.queue))
        # find the index of the tail of the queue
        tail_pos = (self._front + self._size) % len(self.queue)
        self.queue[tail_pos] = e
        self._size += 1

    def dequeue(self):
        if self.is_empty( ):
            raise ValueError( 'Queue is empty' )
        removed = self.queue[self._front]
        self.queue[self._front] = None
        self._front = (self._front + 1) % len(self.queue)
        self._size -= 1
        return removed

    def resize(self, cap):
        old = self.queue
        self.queue = [None] * cap
        #Pass the old element from front to end to the new queue
        walk = self._front
        for k in range(self._size):
            self.queue[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def __str__(self):
        if self.is_empty():
            return '[]'
        s = ''
        tail_pos = (self._front + self._size - 1) % len(self.queue)
        for i in range(self._size):
            s += str(self.queue[(tail_pos + len(self.queue) - i) % len(self.queue)]) + ' '
        return '[ ' + s + ']'

#3.Queue implementation using Linked List
class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, value):
        new_node = SLL.Node(value)

        if self.tail is not None:
            self.tail.next = new_node

        else:
            self.head = new_node

        self.tail = new_node
        self.count += 1

    def dequeue(self):
        if not self.is_empty():
            # point head to next node
            tmp = self.head
            self.head = self.head.next
            #print("dequeue sucess")
            self.count -= 1
            return tmp
        else:
            raise ValueError("Empty QUEUE")

    def is_empty(self):
        return not self.count

    def peek(self):
        if self.is_empty():
            raise ValueError("Empty QUEUE")
        return self.head.value


    def __len__(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def __str__(self):
        if self.is_empty():
            return '[]'
        node = self.head
        s = ''
        while node:
            s += str(node.value) + " "
            node = node.next
        return '[' + s + ']'

'''
myqueue = LinkedQueue()

print ('size was: ', str(len(myqueue)))
print(myqueue, '\n')
myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
myqueue.enqueue(5)
print ('size was: ', str(len(myqueue)))
print(myqueue, '\n')
print(myqueue.dequeue().value)
print(myqueue.dequeue().value)
print ('size was: ', str(len(myqueue)))
print(myqueue, '\n')
myqueue.enqueue(6)
myqueue.enqueue(7)
print(myqueue, '\n')
myqueue.dequeue()
myqueue.dequeue()
print ('size was: ', str(len(myqueue)))
print(myqueue, '\n')
myqueue.dequeue()
myqueue.dequeue()
myqueue.dequeue()
print ('size was: ', str(len(myqueue)))
print(myqueue, '\n')
#myqueue.dequeue()
'''

#4.Queue implementation using Stack
class QueueWithTwoStacks:
    def __init__(self):
        self.insertStack = ArrayStack()
        self.popStack = ArrayStack()

    # O(1)
    def enqueue(self, e):
        self.insertStack.push(e)
        return e
    # O(self.insertStack.length) and O(1) =(amortization)=> O(1)
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Dequeue from an empty queue!')
        if not self.popStack.isEmpty():
            return self.popStack.pop()
        while not self.insertStack.isEmpty():
            self.popStack.push(self.insertStack.pop())
        return self.popStack.pop()

    def __len__(self):
        return self.insertStack.length + self.popStack.length

    def is_empty(self):
        return len(self) == 0

    def __str__(self):

        return str(self.insertStack) + str(self.popStack)

'''
mystack = QueueWithTwoStacks()
print(mystack)
e = mystack.enqueue(1)
print(e)
e = mystack.enqueue(2)
print(e)
e = mystack.enqueue(3)
print(e)
print(mystack)
e = mystack.dequeue()
print(e)
print(mystack)
e = mystack.enqueue(4)
print(e)
print(mystack)
e = mystack.enqueue(5)
print(e)
print(mystack)
e = mystack.dequeue()
print(e)
print(mystack)
'''
