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
'''
