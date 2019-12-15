'''
225. Implement Stack using Queues [Easy]
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue --
which means only push to back, peek/pop from front, size,
and is empty operations are valid.
Depending on your language, queue may not be supported natively.
You may simulate a queue by using a list or deque (double-ended queue),
as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example,
no pop or top operations will be called on an empty stack).

[Method 1]：单队列
每次pop的时候都把前面n-1个元素一个个地pop掉后加入queue尾部，即Pop()操作用时O(n)
[Time]: pop()和peek()都是O(n)
[Space]: O(1)
Runtime: 28 ms, faster than 79.57% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement Stack using Queues.
'''
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        n = len(self.stack)
        while n > 1:
            self.stack.append(self.stack.popleft())
            n -= 1
        return self.stack.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        n = len(self.stack)
        while n > 1:
            self.stack.append(self.stack.popleft())
            n -= 1
        peek = self.stack.popleft()
        self.stack.append(peek)
        return peek

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.stack)

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

'''
[Method 2 [BEST]]: 单队列，每次push的时候重排元素。
每次push时先加入新元素，再把新元素前面的元素一个个pop掉后加入队列的尾端。
[Time]: push需要O(n), 但是peek()和pop()就只需要O(1);
[Space]: O(1);
Runtime: 16 ms, faster than 99.80% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Implement Stack using Queues.
'''
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        n = len(self.q)
        while n > 1:
            self.q.append(self.q.popleft())
            n -= 1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.q)
