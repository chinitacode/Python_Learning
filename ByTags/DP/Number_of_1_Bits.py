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

'''
