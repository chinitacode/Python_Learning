'''
# Practice with Stack:
20. Valid Parentheses (easy)
32. Longest Valid Parentheses (hard)
150. Evaluate Reverse Polish Notation (medium)

# Practice with Queue:
622. Design Circular Queue (Medium)
641. Design Circular Deque (Medium)
239. Sliding Window Maximum (Hard)

# Practice with Recursion:
70. Climbing Stairs (Easy)

# 20. Valid Parentheses
'''
class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

#Or:
def isValid(s):
    stack = []
    for c in s:
        if (c == '(' or c == '[' or c == '{'):
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            if (   (c == ')' and stack[-1] == '(')
                or (c == ']' and stack[-1] == '[')
                or (c == '}' and stack[-1] == '{')):
                stack.pop()
            else:
                return False
    return len(stack) == 0


'''
# 32. Longest Valid Parentheses
  O(n)
Runtime: 40 ms, faster than 59.26% of Python online submissions for Longest Valid Parentheses.
Memory Usage: 12.1 MB, less than 100.00% of Python online submissions for Longest Valid Parentheses.

1. Scan the string from beginning to end by its index.
2. If current character is '(', push its index to the stack.
   If current character is ')' and the character at the index of the top of stack is '(',
   we just find a matching pair so pop from the stack and update result as the
   distance between the current index i and the index of stack[-1].
   Otherwise, we push the index of ')' to the stack.
3. After the scan is done, the stack will only
   contain the indices of characters which cannot be matched. Then
   return result.
4. If the stack is empty, the whole input
   string is valid. Otherwise, we can scan the stack to get longest
   valid substring as described in step 3.
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack == [] or s[stack[-1]] != '(':
                stack.append(i)
            else:
                stack.pop()
                result = max(result, i - stack[-1]) if stack != [] else i + 1
        return result

'''
# Or: To make sure the stack is not empty,
      first put in a tuple (-1, ')')
      as it will never be poped out and -1 can be used to calculate result.

Runtime: 32 ms, faster than 92.42% of Python online submissions for Longest Valid Parentheses.
Memory Usage: 13.4 MB, less than 14.29% of Python online submissions for Longest Valid Parentheses.
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, result = [(-1, ')')], 0
        for i, paren in enumerate(s):
            if paren == ')' and stack[-1][1] == '(':
                stack.pop()
                result = max(result, i - stack[-1][0])
            else:
                stack += (i, paren),
        return result


'''
Or: add 0 to stack is c is '(',
    only add 2 to stack[-1], update longest when a pair of parenthesis is canceled out,
    else reset stack = [0] to avoid the length of another slice of parentheses got added to longest
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        longest = 0

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                # if stack is not really empty
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    # separate slices of parentheses with distance in between
                    stack = [0]

        return longest

'''
# 150. Evaluate Reverse Polish Notation (medium)
'''




'''
# 622. Design Circular Queue (Medium)
  Method1: Use List(Array)
'''
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.front = 0
        self.rear = -1
        self.length = 0
        self.stack = [None] * self.size



    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.stack[self.rear] = value
        self.length += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.stack[self.front] = None
        self.front = (self.front + 1) % self.size
        self.length -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.stack[self.front]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.stack[self.rear]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.length == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.length == self.size
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
'''
# Method2: Use Doubly Linked List
'''
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = k
        self.front = Node()
        self.rear = Node()
        self.front.next = self.rear
        self.rear.prev = self.front
        self.length = 0


    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        new_node = Node(self.rear.prev, value, self.rear)
        self.rear.prev.next = new_node
        self.rear.prev = new_node
        self.length += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.front.next.next.prev = self.front
        self.front.next = self.front.next.next
        self.length -= 1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.front.next.value

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.rear.prev.value

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.length == 0

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.length == self.size
class Node:
    def __init__(self, prev = None, value = None, next = None):
        self.prev = prev
        self.value = value
        self.next = next

'''
239. Sliding Window Maximum (Hard)
O(n) solution using deque

Keep indexes of good candidates in deque d.
The indexes in d are from the current window, they're increasing,
and their corresponding nums are decreasing.
Then the first deque element is the index of the largest window value.

For each index i:
Pop (from the end) indexes of smaller elements (they'll be useless).
Append the current index.
Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window).
If our window has reached size k, append the current window maximum to the output.
'''
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        result = []
        for i in range(len(nums)):
            # pop it if the first/left (max) element is out of the current window
            if q and i - q[0] == k:
                q.popleft()

            # Can only pop element of deque when it's not empty
            while q:
                # pop useles elements from last/right of the queue
                if nums[q[-1]] < nums[i]:
                    q.pop()
                # if the right side ele is less than q[-1], break the while loop
                else:
                    break
            # Not adding index of ele less than q[-1]
            q.append(i)
            # Start adding result when it's a full window
            if i >= k-1: # i == k-1 is the beginning of a full window
                result.append(nums[q[0]])

        return result
# Or:
def maxSlidingWindow(self, nums, k):
    d = collections.deque()
    out = []
    for i, n in enumerate(nums):
        while d and nums[d[-1]] < n:
            d.pop()
        d += i,
        if d[0] == i - k:
            d.popleft()
        if i >= k - 1:
            out += nums[d[0]],
    return out
'''
Last three lines could be this, but for relatively large k it would waste space:

        out += nums[d[0]],
    return out[k-1:]


Documentation about Deque:
https://docs.python.org/2/library/collections.html#collections.deque
https://www.geeksforgeeks.org/deque-in-python/
https://pymotw.com/2/collections/deque.html
'''
