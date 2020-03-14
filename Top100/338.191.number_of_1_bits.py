'''
191. Number of 1 Bits [Easy]

Write a function that takes an unsigned integer
and return the number of '1' bits it has (also known as the Hamming weight).


Example 1:
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Note:
Note that in some languages such as Java,
there is no unsigned integer type.
In this case,
the input will be given as signed integer type and should not affect your implementation,
as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 3 above the input represents the signed integer -3.

Follow up:
If this function is called many times, how would you optimize it?


[Method 1]: Bit Operation 左移 + using logical AND operation
我们使用 位掩码 来检查数字的第i位。
一开始，掩码 m=1 因为1的二进制表示是：
0000 0000 0000 0000 0000 0000 0000 0001
显然，任何数字跟掩码 1 进行逻辑与运算，都可以让我们获得这个数字的最低位。
检查下一位时，我们将掩码左移一位。
0000 0000 0000 0000 0000 0000 0000 0010
并重复此过程。
'''
#TLE
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits, mask = 0, 1
        for i in range(n):
            if n & mask != 0:
                bits += 1
            mask <<= 1
        return bits
'''
如果input integer最多32位则可以通过。
Runtime: 24 ms, faster than 20.82% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.7 MB, less than 75.00% of Python online submissions for Number of 1 Bits.
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits, mask = 0, 1
        for i in range(32):
            if n & mask:
                bits += 1
            mask <<= 1
        return bits


'''
[Method 2]: Bit Operation 右移n + using logical AND operation
和解法一类似，但是这次是用n来与1做与运算，每运算完一次则把n右移1位（即抛掉最低位），
继续与运算，看是否为1。
[Time]: O(logn)，即n的位数
Runtime: 28 ms, faster than 5.68% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.9 MB, less than 10.00% of Python online submissions for Number of 1 Bits.
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 0
        while n != 0:
            bits += (n&1)
            n >>= 1
        return bits

'''
#等于：
Runtime: 24 ms, faster than 20.82% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.8 MB, less than 57.50% of Python online submissions for Number of 1 Bits.
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 0
        while n != 0:
            bits += (n%2)
            n //= 2
        return bits


'''
[Method 3]:
我们可以把前面的算法进行优化。我们不再检查数字的每一个位，而是不断把数字最后一个 1 反转，
并把答案加一。当数字变成 0 的时候，我们就知道它没有 1 的位了，此时返回答案。
这里关键的想法是对于任意数字 n ，将 n 和 n - 1 做与运算，会把最后一个 1 的位变成 0 。
为什么？考虑 n 和 n - 1 的二进制表示。
n:   1100100
         ^
n-1: 1100011
         ^
=>   1100000

在二进制表示中，数字 n 中最低位的 1 总是对应 n - 1 中的 0 。
因此，将 n 和 n - 1 与运算总是能把 n 中最低位的 1 变成 0 ，并保持其他位不变。
使用这个小技巧，代码变得非常简单。
[Time]：O(logn)。运行时间与 n 中位为 1 的有关。
在最坏情况下， n 中所有位都是 1, 即O(logn) 。
[Space]：O(1)。没有使用额外空间。
Runtime: 20 ms, faster than 51.48% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.9 MB, less than 5.00% of Python online submissions for Number of 1 Bits.
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 0
        while n != 0:
            bits += 1
            n = n&(n-1)
        return bits
