'''
191.Number of 1 Bits [Easy]

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).



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
Note that in some languages such as Java, there is no unsigned integer type.
In this case, the input will be given as signed integer type and should not affect your implementation,
as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation.
Therefore, in Example 3 above the input represents the signed integer -3.

Follow up:

If this function is called many times, how would you optimize it?

二进制中1的个数

输入一个32位整数，输出该数二进制表示中1的个数。

注意：
负数在计算机中用其绝对值的补码来表示。

样例1
输入：9
输出：2
解释：9的二进制表示是1001，一共有2个1。

样例2
输入：-2
输出：31
解释：-2在计算机里会被表示成11111111111111111111111111111110，
      一共有31个1。


[注意]：
对于正数（00000001）原码来说，首位表示符号位，反码、补码都是本身

对于负数（100000001）原码来说，反码是对原码除了符号位之外作取反运算即（111111110），补码是对反码作+1运算即（111111111）

因为题意是指定32位整数，所以对负数取补码的过程就是先用2**32-1和num的绝对值异或来取反，再加上1


[可能会引起死循环的方法]：

'''
# 每次把n与1相与来判断 n最低位是否为1，再把 n 右移一位来判断下一个最低位，直到 n 被右移为0
class Solution:
    def NumberOf1(self, n):
        count = 0
        while n:
            if n&1:
                count += 1
            print(n)
            n = n >> 1
        return count

'''
如果n为正还好，但若n为负数，因为负数在计算机里是以补码的方式存储的，即负数的原码的最高位为符号位1，
比如十进制-1的原码（假设用8位来存储数字）为10000001，那么反码为11111110，加上1就为其补码11111111。
那么将它右移后得01111111，因为是负数，所以移位后的最高位仍然会被设置为1，则移位后得到的数字仍是11111111，
即仍然代表十进制-1，所以-1 >> 1 得到 -1不变，因此n永远不会为0，则while就是个死循环。

此外，在python中，
由“n与(n-1)做与操作恰好去掉n的最右位1”，如果将n&(n-1), 仍会保留最高位为1，例如(-1)&(-2)得到-2， (-2)&(-3)得到-4, 然后
-8，-16，-32，-64，-128，-256，-512，-1024，-2048，-4096......-4294967296，
这样子的负数一直相与下去会得到越来越小的负数，因为python没有限制数字的存储位数，
所以对于32位能表示的最大正整数2^32-1,即4294967295，最小负整数为-4294967295，
所以当n取到-4294967296时，二进制表示为-0b100000000000000000000000000000000，
即尽管其余32位都为0，第33位（最高位）仍为1来代表负数，所以十进制数n始终不可能取0，while也是死循环。

因此我们可以不用十进制n来判断，而是用0xffffffff（即32位全为1）来与n相与，看最终是否32位都为0，如果都为0则跳出循环。
如下，当n为-1时，其补码为32个1，则一共循环了32次，count也是32.
'''
class Solution:
    def NumberOf1(self, n):
        count = 0
        while n & 0xffffffff != 0:
            count += 1
            n = n & (n - 1)
            print(n)
        return count

'''
-2
-4
-8
-16
-32
-64
-128
-256
-512
-1024
-2048
-4096
-8192
-16384
-32768
-65536
-131072
-262144
-524288
-1048576
-2097152
-4194304
-8388608
-16777216
-33554432
-67108864
-134217728
-268435456
-536870912
-1073741824
-2147483648
-4294967296
32

但是在c/c++里就可以用十进制n来作为循环的判断条件：
class Solution {
public:
     int  NumberOf1(int n) {
         int count = 0;
         while(n)
         {
             ++ count;
             n = n & (n-1);
         }
         return count;


     }
};


[常规解法]：因为是32位计数，所以循环32次判断n中1的个数
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        # 标志位一路左移，做“与”操作
        flag = 1
        count = 0
        for _ in range(32):
            if flag & n: count += 1
            flag = flag << 1
        return count

#Or:
class Solution:
    def NumberOf1(self, n):
        # write code here
        # 复数的补码前面自动填充1
        # 方法一
        return sum([(n>>i & 1) for i in range(0,32)])
