'''
338. Counting Bits [Medium]
Given a non negative integer number num.
For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's
in their binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]

Example 2:
Input: 5
Output: [0,1,1,2,1,2]

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss?
Do it without using any builtin function like __builtin_popcount in c++ or in any other language.


[Method 1]: 遍历每个数，数每个数二进为1的个数。
[Time]: O(nlgn)
[Space]: O(1)
Runtime: 228 ms, faster than 9.08% of Python3 online submissions for Counting Bits.
Memory Usage: 19.9 MB, less than 5.00% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = []
        for i in range(num+1):
            count = 0
            while i != 0:
                count += i%2
                i //= 2
            res.append(count)
        return res


'''
[Method 2]: DP （+最高有效位）
Thinking:

First check the input parameter,
that the input number is non negative.

Then The first idea to come up with is find the pattern or rules for the result.
Therefore, we can get following pattern

Index : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

num :   0 1 1 2 1 2 2 3 1 2  2  3  2  3  3  4

Do you find the pattern?

Obviously, this is overlap sub problem, and we can come up the DP solution.
For now, we need find the function to implement DP.

dp[0] = 0;

dp[1] = dp[0] + 1;

dp[2] = dp[0] + 1;

dp[3] = dp[1] +1;

dp[4] = dp[0] + 1;

dp[5] = dp[1] + 1;

dp[6] = dp[2] + 1;

dp[7] = dp[3] + 1;

dp[8] = dp[0] + 1;
...

This is the function we get,
now we need find the other pattern for the function to get the general function.
After we analyze the above function, we can get:

dp[0] = 0;

dp[1] = dp[1-1] + 1;

dp[2] = dp[2-2] + 1;

dp[3] = dp[3-2] +1;

dp[4] = dp[4-4] + 1;

dp[5] = dp[5-4] + 1;

dp[6] = dp[6-4] + 1;

dp[7] = dp[7-4] + 1;

dp[8] = dp[8-8] + 1;
..

Obviously, we can find the pattern for above example,
so now we get the following general function:
dp[index] = dp[index - offset] + 1;
[Time]: O(n);
[Space]: O(n)
Runtime: 116 ms, faster than 61.37% of Python3 online submissions for Counting Bits.
Memory Usage: 20 MB, less than 5.00% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        offset = 1 #offset为最高有效位
        for i in range(1, num+1):
            if offset*2 == i:
                offset *= 2
            dp[i] = dp[i-offset] + 1
        return dp


'''
[Method 3]: DP + Bit Manipulation（+最低有效位）
i//2 等于 i>>1；
i%2 ==1 等于 i & 1==1, 但用位运算速度快很多。
[Time]: O(n);
[Space]: O(n)
Runtime: 92 ms, faster than 87.37% of Python3 online submissions for Counting Bits.
Memory Usage: 20 MB, less than 5.00% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        for i in range(1, num+1):
            dp[i] = dp[i>>1]
            if i&1 == 1:
                dp[i] += 1
        return dp

'''
#Or:
Runtime: 116 ms, faster than 30.61% of Python3 online submissions for Counting Bits.
Memory Usage: 20.3 MB, less than 5.00% of Python3 online submissions for Counting Bits.
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        for i in range(1, num+1):
            if i&1 == 0:
                dp[i] = dp[i>>1]
            else:
                dp[i] = dp[i-1] + 1
        return dp

'''
#合并即：
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]*(num+1)
        for i in range(1, num+1):
            dp[i] = dp[i>>1] + (i&1)
        return dp
