'''
Method 1: Bit operation #O(1)
If n is the power of two:
n = 2 ^ 0 = 1 = 0b0000...00000001, and (n - 1) = 0 = 0b0000...0000.
n = 2 ^ 1 = 2 = 0b0000...00000010, and (n - 1) = 1 = 0b0000...0001.
n = 2 ^ 2 = 4 = 0b0000...00000100, and (n - 1) = 3 = 0b0000...0011.
n = 2 ^ 3 = 8 = 0b0000...00001000, and (n - 1) = 7 = 0b0000...0111.
we have n & (n-1) == 0b0000...0000 == 0

Otherwise, n & (n-1) != 0.

For example, n =14 = 0b0000...1110, and (n - 1) = 13 = 0b0000...1101.
'''
def isPowerOfTwo(n):
    return n > 0 and (n & (n-1)) == 0


'''
Method 2: Iteration #O(lgn)
Runtime: 12 ms, faster than 95.63% of Python online submissions for Power of Two.
Memory Usage: 11.7 MB, less than 100.00% of Python online submissions for Power of Two.
'''
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        while n%2 == 0:
            n >>= 1
            if n == 1:
                return True
        return False

#Or:
def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n%2 == 0):
        n/=2
    return n == 1

'''
Method 3: Recursion
O(lgn)
'''
def isPowerOfTwo(n):
    return n > 0 and (n == 1 or (n%2 == 0 and isPowerOfTwo(n//2)))

'''
Method 4: Math derivation O(1)
Because the range of an integer = -2147483648 (-2^31) ~ 2147483647 (2^31-1),
the max possible power of two = 2^30 = 1073741824.
(1) If n is the power of two, let n = 2^k, where k is an integer.
We have 2^30 = (2^k) * 2^(30-k), which means (2^30 % 2^k) == 0.
(2) If n is not the power of two, let n = j*(2^k), where k is an integer and j is an odd number.
We have (2^30 % j*(2^k)) == (2^(30-k) % j) != 0.

return n > 0 && (1073741824 % n == 0);


Method 5: Bit count  O(1)
Very intuitive. If n is the power of 2, the bit count of n is 1.
Note that 0b1000...000 is -2147483648, which is not the power of two, but the bit count is 1.
return n > 0 && Integer.bitCount(n) == 1;
The time complexity of bitCount() can be done by a fixed number of operations.
More info in https://stackoverflow.com/questions/109023.

Method 6: Look-up table
There are only 31 numbers in total for an 32-bit integer.

return new HashSet<>(Arrays.asList(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608,16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824)).contains(n);
'''
