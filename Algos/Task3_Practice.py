'''
69. Sqrt(x) (Easy)
Method 1: Binary Search: O(lgn)
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid == x // mid:
                return mid
            if mid < x // mid:
                left = mid + 1
            else:
                right = mid - 1
        return right

'''
Method 2: Newton's Method
Runtime: 16 ms, faster than 92.83% of Python online submissions for Sqrt(x).
Memory Usage: 11.9 MB, less than 5.88% of Python online submissions for Sqrt(x).

Using Newton's method, the time complexity of calculating a root of a function f(x) with n-digit precision,
provided that a good initial approximation is known,
is O((log n) F(n)) where F(n) is the cost of calculating f(x)/f'(x), with n-digit precision.
'''
def my_Sqrt(x):
    r = x
    while r*r > x:
        r = (r + x//r) // 2
    return r

'''
Functional version:
'''
def average(x, y):
    return (x + y)/2

def improve(update, close, guess=1):
    while not close(guess):
        guess = update(guess)
    return guess

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

def sqrt(a):
    def sqrt_update(x):
        return average(x,a/x)
    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)

result = sqrt(256)


'''
239. Sliding Window Maximum (Hard)
1.Heap O(N logK)
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        hp = [-x for x in nums[:k]]
        heapq.heapify(hp)

        ans = [-hp[0]]
        wait_to_pop = collections.Counter()
        for i in range(k, len(nums)):
            out_x, in_x = nums[i-k], nums[i]
            wait_to_pop[out_x] += 1
            heapq.heappush(hp, -in_x)

            while wait_to_pop[-hp[0]] > 0:
                wait_to_pop[-hp[0]] -= 1
                heapq.heappop(hp)

            ans.append(-hp[0])

        return ans











'''
2. O(n) solution using deque
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

'''
3. Brute Force:
Python O(kn) one-liner:
'''

def maxSlidingWindow(self, nums, k):
    return nums and [max(nums[i:i+k]) for i in range(len(nums)-k+1)]
