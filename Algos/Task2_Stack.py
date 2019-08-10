# import the linked list class
from Task1_2_LinkedLists import SLL

'''
【栈】
FILO： First in Last out
A stack is a data structure with two main operations: push and pop.
Push: append an element on top of the stack
Pop: remove an element from the top of the stack
栈(Stack)是限制插入和删除操作只能在一个位置进行的表，该位置是表的末端，称为栈的顶(top)。
栈的基本操作有PUSH(入栈)和POP(出栈)。栈又被称为LIFO(后入先出)表。
1.用数组实现一个顺序栈
2.用链表实现一个链式栈
3.编程模拟实现一个浏览器的前进、后退功能（选做）

  * Difference bewteen stacks using array and using linked list:
Top of stack(栈顶) is different. For arrays, the top is at its end, e.g. stack[-1];
for linked list, the top is at its head, e.g. stack.head

  * Basic functions:
Stack(): creates a new empty stack. Does not need parameters.
push(item): adds a new item to the top of the stack. It needs the item and returns nothing.
pop(): removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.
peek(): returns the top item from the stack but does not modify the stack. Does not need parameters.
isEmpty(): checks whether the stack is empty. Does not need parameters and returns a boolean value.
size(): returns the number of items on the stack. Does not need parameters and returns an integer.
'''
#1.Stack implementation using List
class ListStack():
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return self.stack==[]
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            raise IndexError('pop from empty stack')
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)

'''
#2. Stack implementation using Array

  * Python Lists have made it so easy to implement Stack.
However, if we want to implement Stack language agnostically,
we have to assume that lists are like arrays (fixed in size)
and use a length pointer to keep a tab on the status of the stack.
'''
class ArrayStack():
    def __init__(self):
        self.stack=[]
        self.capacity = 10
        self.length = 0
    def isEmpty(self):
        return not self.length
    def push(self, item):
        if self.length == self.capacity:
            raise indexError('Stack is full')
        self.stack.append(item)
        self.length += 1
    def pop(self):
        if self.isEmpty():
            raise IndexError('pop from empty stack')
        self.length -= 1
        return self.stack.pop()
    def peek(self):
        return self.stack[-1]
    def __len__(self):
        return self.length
    def __str__(self):
        s = ''
        for i in range(len(self.stack)):
            s += str(self.stack[-(i + 1)]) + ' '
        return '[ ' + s + ']'

#3. Stack implementation using Linked List
class LinkedStack():
    def __init__(self):
        self.stack = SLL()
    def isEmpty(self):
        return not self.stack.size
    def push(self, item):
        self.stack.add_first(item)
    def pop(self):
        return self.stack.remove_first().value
    def peek(self):
        return self.stack.__getitem__(0).value
    def __len__(self):
        return self.stack.size
    def __str__(self):
        return self.stack.__str__()

'''
mystack = LinkedStack()
print ('size was: ', str(len(mystack)))
print(mystack)
mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.push(5)
print ('size was: ', str(len(mystack)))
print(mystack)
print(mystack.peek())
mystack.pop()
mystack.pop()
print ('size was: ', str(len(mystack)))
print(mystack)
print(mystack.peek())
mystack.pop()
mystack.pop()
mystack.pop()
#mystack.pop()
'''
