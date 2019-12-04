'''
[Method 1]: Math
直接理想总和（高斯累加，（首项+尾项）**项数//2） 减去 数组总和。
[Time]: O(n);
[Space]: O(1)
Runtime: 132 ms, faster than 98.14% of Python3 online submissions for Missing Number.
Memory Usage: 13.9 MB, less than 96.77% of Python3 online submissions for Missing Number.
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums)+1)*len(nums)//2-sum(nums)

'''
[Method 2]: XOR
异或运算， 二进制位逐个比较，相同的为0， 不同的为1。
所以任一数字，异或自己 肯定等于 0。 此外异或运算满足 交换律 A^B^C = A^C^B
所以我们先从0到n进行异或，
把结果与nums里的元素再进行异或复原，
最终结果即为缺失数字。
Runtime: 144 ms, faster than 86.04% of Python3 online submissions for Missing Number.
Memory Usage: 14 MB, less than 90.32% of Python3 online submissions for Missing Number.
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)+1):
            xor ^= i
        for num in nums:
            xor ^= num
        return xor

#Or:
class Solution:
    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
