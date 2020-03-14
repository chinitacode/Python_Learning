'''
485. 最大连续1的个数 [简单]

给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。

[Method 1]
执行用时 : 844 ms, 在所有 Python3 提交中击败了 5.00% 的用户
内存消耗 :13.7 MB, 在所有 Python3 提交中击败了 14.08% 的用户
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Max = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                Max = max(Max, count)
            else:
                count = 0
        return Max

'''
可以优化为for循环中减少一个判断条件：
执行用时 : 404 ms, 在所有 Python3 提交中击败了 81.00% 的用户
内存消耗 :13.7 MB, 在所有 Python3 提交中击败了 14.08% 的用户
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Max = 0
        count = 0
        for num in nums:
            count = count*num + num  # if num == 0, count = 0 else count += 1
            if count > Max:
                Max = count
        return Max



'''
[Method 2]:
在 Python 中可以使用 map 和 join 来解决此问题。
使用 splits 函数在 0 处分割将数组转换成字符串。
在获取子串的最大长度就是最大连续 1 的长度。
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(len, ''.join(map(str,nums)).split('0')))
