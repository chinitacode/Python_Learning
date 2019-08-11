'''
155. Min Stack  Easy

Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

#1. push self-defined data structure '(v, min)' into stack recording current minimum value each time
Time: O(1)    Space: O(n)
Runtime: 48 ms, faster than 94.53% of Python online submissions for Min Stack.
Memory Usage: 18 MB, less than 6.67% of Python online submissions for Min Stack.
'''
import sys

class NodeWithMin:
    def __init__(self, v, min):
        self.value = v
        self.min = min

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        newMin = min(x, self.getMin())
        self.stack.append(NodeWithMin(x, newMin))

    def pop(self):
        """
        :rtype: None
        """
        return self.stack.pop().value

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1].value

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack == []:
            return sys.maxsize
        return self.stack[-1].min

'''
#2. two-stack method (60ms, beats 99%)
Time: O(1)    Space: O(n)
'''
class MinStack:
    # To be able to retrieve the minimum value in O(1),
    # we need another stack to record the minimum value
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # Update stack_min if it's empty or x <= its last element, and put it at its end
        if not self.stack_min or x <= self.stack_min[-1]:
            self.stack_min.append(x)

    def pop(self) -> None:
        # Record the top value of the stack which is to be popped
        prev_top = self.stack.pop()
        # Pop stack_min if prev_top == its last element
        if prev_top == self.stack_min[-1]:
            self.stack_min.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.stack_min[-1]

'''
#3. Method: define a variable minEle that stores the current minimum element in the stack
# The key is push “2x – minEle” into the stack instead of x
# so that previous minimum element can be retrieved using current minEle and its value stored in stack
# Source: https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
# 76ms, beats 53%
'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack :
            self.stack.append(x)
            self.min = x
        elif x >= self.min:
            self.stack.append(x)
        else:
            self.stack.append(2*x - self.min)
            self.min = x

    def pop(self) -> None:
        if not self.stack:
            return None
        else:
            popped = self.stack.pop()
            if popped < self.min: # it means number getting removed is min
                self.min = 2 * self.min - popped
                return self.min
            else:
                return popped

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            peeked = self.stack[-1]
            if peeked < self.min:
                return self.min
            else:
                return peeked

    def getMin(self) -> int:
        return self.min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
