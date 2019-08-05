'''
【链表】
实现单链表、循环链表、双向链表，支持增删操作
实现单链表反转
实现两个有序的链表合并为一个有序链表
实现求链表的中间结点

'''

lass Link:
    class Node:
        def __init__(self, value = None, next = None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = self.Node() #Create a dummy node
        self.size = 0

    def is_empty(self):
        return not self.size
    # O(1)
    def add_first(self, value):
        #Create a new node with the value,
        # make its rest point to the next of the original linked list
        node = self.Node(value, self.head.next)
        # Reset the dummy node as the head
        self.head.next = node
        self.size += 1

    #O(n)
    def add_last(self, value):
        new_node = self.Node(value)
        # Create a variable to loop through until reaching the tail node
        node = self.head
        while node.next != None:
            node = node.next
        node.next = new_node
        self.size += 1

    # O(1)
    def remove_first(self):
        assert self.size > 0, 'The linked list is empty!'
        self.head.next = self.head.next.next
        self.size -= 1

    # O(n)
    def remove_last(self):
        assert self.size > 0, 'The linked list is empty!'
        node = self.head
        while node.next.next != None:
            node = node.next
        node.next = None
        self.size -= 1

    #O(n)
    def insert(self, value, index):
        if index < 0 or index > self.size:
            raise Outbound('list index out of range')
        new_node = self.Node(value)
        if self.is_empty():
            self.head.next = new_node
        else:
            node = self.head
            for i in range(index):
                node = node.next
            new_node.next = node.next
            node.next = new_node
        self.size += 1

    #O(n)
    def remove(self, index):
        if self.is_empty():
            raise Empty('LinkedList is empty')
        if index < 0 or index >= self.size:
            raise Outbound( 'index is out of bound' )
        node = self.head
        for i in range(index):
            node = node.next
        node.next = node.next.next
        self.size -= 1

    def search(self, value):
        pass

    #O(n)
    def __str__(self):
        if self.size == 0:
            return '<>'
        node = self.head
        s = ''
        while node.next != None:
            node = node.next
            if node.next != None:
                s += '<' + str(node.value) + ', '
            else:
                s += '<' + str(node.value) + '>' * self.size
        return  s

    #O(n)
    def __repr__(self):
        if self.size == 0:
            return 'Link()'
        node = self.head
        s = ''
        while node.next != None:
            node = node.next
            if node.next != None:
                s += 'Link(' + str(node.value) + ', '
            else:
                s += 'Link(' + str(node.value) + ')' * self.size
        return  s

    def __len__(self):
        return self.size


# Singly Linked List单向链表
class SLinked(Link):
    def __init__(self, *args):
        super().__init__()
        for arg in args:
            self.add_last(arg)



# Doubly Linked List双向链表
class DLinked(Link):
    class Node(Link.Node):
        def __init__(self, value = None, next = None, prev = None):
            super().__init__(value = None, next = None)
            self.prev = prev

    def __init__(self,  *args):
        super().__init__()
        self.tail = self.Node()
        for arg in args:
            self.add_last(arg)

    def add_first(self, value):
        node = self.Node(value, self.head.next, None)
        self.head.next = node
        self.size += 1

   # def add_last(self, value):
