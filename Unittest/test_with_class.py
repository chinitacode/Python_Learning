import unittest

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []
        self.size = 0

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.push_stack.append(x)
        self.size += 1

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.size == 0:
            raise IndexError('The queue is empty!')
        self.size -= 1
        if self.pop_stack:
            return self.pop_stack.pop()
        while len(self.push_stack) > 1:
            self.pop_stack.append(self.push_stack.pop())
        return self.push_stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.size == 0:
            raise IndexError('The queue is empty!')
        if not self.pop_stack:
            while len(self.push_stack) > 0:
                self.pop_stack.append(self.push_stack.pop())
        return self.pop_stack[-1]



    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.size == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = MyQueue()
        self.q.push(1)
        self.q.push(2)

    def test_empty(self):
        new_q = MyQueue()
        self.assertEqual(new_q.size, 0)
        self.assertEqual(new_q.empty(), True)
        self.assertRaises(IndexError,new_q.pop)

    def test_push(self):
        self.assertEqual(self.q.size, 2)
        self.q.push(3) #不影响其他函数，只在本函数内部修改self.q
        self.assertEqual(self.q.size, 3)

    def test_pop(self):
        self.assertEqual(self.q.pop(), 1)
        self.assertEqual(self.q.size, 1)
        self.assertEqual(self.q.peek(), 2)
        self.assertEqual(self.q.pop(), 2)
        self.assertEqual(self.q.empty(), True)

if __name__ == '__main__':
    unittest.main()
