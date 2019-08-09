'''
【链表】
实现单链表、循环链表、双向链表，支持增删操作
实现单链表反转
实现两个有序的链表合并为一个有序链表
实现求链表的中间结点

'''


class Link:
    class Node:
        def __init__(self, value = None, next = None):
            self.value = value
            self.next = next

    def __init__(self):
        self.head = self.Node() #Create a dummy node
        self.size = 0

    def is_empty(self):
        return not self.size

    def __setitem__(self, index, value):
        node = self.__getitem__(index)
        node.value = value

    # Return a node
    def __getitem__(self, index):
        if index < -self.size or index >= self.size:
            raise ValueError( 'index is out of bound' )
        if index < 0:
            index = self.size + index
        if not self.head.next:
            raise ValueError( 'LinkedList is empty' )
        node = self.head.next
        for i in range(index):
            node = node.next
        return node

    # O(1)
    def add_first(self, value):
        #Create a new node with the value,
        # make its rest point to the next of the original linked list
        if isinstance(value, self.Node):
            new_node = value
        else:
            new_node = self.Node(value, self.head.next)
        # Reset the dummy node as the head
        self.head.next = new_node
        self.size += 1

    #O(n)
    def add_last(self, value):
        if isinstance(value, self.Node):
            new_node = value
        else:
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
        removed = self.head.next
        self.head.next = self.head.next.next
        removed.next = None
        self.size -= 1
        return removed

    # O(n)
    def remove_last(self):
        assert self.size > 0, 'The linked list is empty!'
        node = self.head
        while node.next.next != None:
            node = node.next
        popped = node.next
        node.next = None
        self.size -= 1
        return popped


    #O(n)
    def insert(self, index, value):
        if index < -self.size or index >= self.size:
            raise ValueError( 'index is out of bound' )
        if index < 0:
            index = self.size + index
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
        assert self.size > 0, 'The linked list is empty!'
        if index < -self.size or index >= self.size:
            raise ValueError( 'index is out of bound' )
        if index < 0:
            index = self.size + index
        node = self.head
        for i in range(index):
            node = node.next
        node.next = node.next.next
        self.size -= 1

    #O(n)
    def search(self, val):
        assert self.size > 0, 'The linked list is empty!'
        node = self.head.next
        index = 0
        while node.next != None:
            if node.value == val:
                return index
            node = node.next
            index += 1
        return -1

    # O(n) Two-pointer Method, one traverses only one node at a time while the other traverses two nodes
    # and stop when the other reached the end
    def get_mid(self):
        assert self.size > 0, 'The linked list is empty!'
        slow, fast = self.head.next, self.head.next
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sort(self, reverse = False):
        pass

    def reverse(self):
        pass

    #O(n)
    def __str__(self):
        if self.head.next == None:
            return '<>'
        count = 0
        node = self.head
        s = ''
        while node.next != None:
            node = node.next
            count += 1
            if node.next != None:
                s += '<' + str(node.value) + ', '
            else:
                s += '<' + str(node.value) + '>' * count
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
                s += 'SLL(' + str(node.value) + ', '
            else:
                s += 'SLL(' + str(node.value) + ')' * self.size
        return  s

    def __len__(self):
        return self.size

# Singly Linked List单向链表
class SLL(Link):
    def __init__(self, *args):
        super().__init__()
        for arg in args:
            self.add_last(arg)



# Doubly Linked List双向链表
class DLL(Link):
    class Node(Link.Node):
        def __init__(self, value = None, next = None, prev = None):
            super().__init__(value, next)
            self.prev = prev

    def __init__(self,  *args):
        super().__init__()
        self.tail = self.Node(None, None, self.head)
        self.head.next = self.tail
        for arg in args:
            self.add_last(arg)
    # O(1)
    def add_first(self, value):
        new_node = self.Node(value, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1

    # O(1)
    def add_last(self, value):
        new_node = self.Node(value, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.size += 1

    def insert(self, index, value):
        if index < -self.size or index > self.size:
            raise ValueError( 'index is out of bound' )
        if index < 0:
            index = self.size + index
        if index == 0:
            self.add_first(value)
        elif index == self.size:
            self.add_last(value)
        else:
            next_node = self.__getitem__(index)
            new_node = self.node(value, next_node, next_node.prev)
            next_node.prev.next = new_node
            next_node.prev = new_node
            self.size += 1

    def remove_first(self):
        assert self.size > 0, 'The linked list is empty!'
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        self.size -= 1

    def pop(self):
        assert self.size > 0, 'The linked list is empty!'
        popped = self.tail.prev
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1
        popped.prev = None
        popped.next = None
        return popped

    def remove(self, index):
        if index < -self.size or index >= self.size:
            raise ValueError( 'index is out of bound' )
        if index < 0:
            index = self.size + index
        if index == 0:
            self.remove_first()
        elif index == self.size - 1:
            self.pop()
        else:
            node = self.__getitem__(index)
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1

    def get_mid(self):
        assert self.size > 0, 'The linked list is empty!'
        index = 0
        left, right = self.head.next, self.tail.prev
        while left != right and left.next != right:
            left = left.next
            right = right.prev
            index += 1
        return left


    def __repr__(self):
        if self.size == 0:
            return 'Link()'
        node = self.head.next
        s = ''
        while node.next != None:
            if node.next.next != None:
                s += 'Link(' + str(node.value) + ', '
            else:
                s += 'Link(' + str(node.value)
            node = node.next
        s += ')' * self.size

        return  s

    def __str__(self):
        if self.size == 0:
            return '<>'
        node = self.head.next
        s = ''
        while node.next != None:
            if node.next.next != None:
                s += '<' + str(node.value) + ', '
            else:
                s += '<' + str(node.value)
            node = node.next
        s += '>' * self.size

        return  s


        return  s
