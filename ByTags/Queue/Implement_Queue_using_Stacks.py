'''
232. Implement Queue using Stacks [Easy]

Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack --
which means only push to top, peek/pop from top, size,
and is empty operations are valid.
Depending on your language, stack may not be supported natively.
You may simulate a stack by using a list or deque (double-ended queue),
as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example,
no pop or peek operations will be called on an empty queue).

[Method 1]: 2 Stacks
用两个stack，stack1即insert_stack拿来装push的元素，stack2拿来pop元素,即pop_stack。
即，当要pop的时候，把stack1的元素1个个地pop出来放到stack2内，
然后pop掉stack2的栈顶元素。
之后要再push加元素，就push到stack1里面。
要pop元素时，只要stack2不为空，就pop掉stack2的栈顶元素，
若为空，就把stack1的元素pop出来加到stack2内，再pop。

[Time]: O(1) amortized,即分摊O(1)；
[Space]: O(n),多用了一个栈；
Runtime: 28 ms, faster than 81.81% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Implement Queue using Stacks.
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1, self.stack2 = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not(self.stack1 or self.stack2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
