'''
21.输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
 
提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000

[Method 1]: 暴利解法（不维持原顺序，TLE）：
从头到尾扫描这个数组，每碰到一个偶数就把这个这个偶数记下为temp，
然后把之后的元素全部往前提一位(O(n)),
再把temp插入到最后空出的偶数位上。
[Time]: O(n**2)因为每碰到一个偶数位就会往前移动O(n)个数字；
[Space]: O(1)
'''
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        i, offset, count = 0, 0, 0
        while count < len(nums):
            if not(nums[i] & 1):
                tmp = nums[i]
                for j in range(i, len(nums)-1-offset):
                    nums[j] = nums[j+1]
                nums[len(nums)-1-offset] = tmp
                offset += 1
            else:
                i += 1
            count += 1
        return nums

'''
[Method 2]: 开辟新数组+位运算(维持原次序，空间换时间)
[Time]: O(n)
[Space]: O(n)
执行用时 :248 ms,
内存消耗 :19.2 MB
'''
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd, even = [], []
        for num in nums:
            if num & 1:
                odd.append(num)
            else:
                even.append(num)
        return odd + even
'''
或者：
先创建一个新的长度相同的空数组，
遍历一次，统计奇数个数。
然后再遍历一次从前往后填坑。
'''
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd_cnt = 0
        res = [0] * len(nums)
        # 统计个数
        for n in nums:
            if n % 2 != 0:
                odd_cnt += 1
        # 填坑
        odd_i = 0
        even_i = odd_cnt
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                res[odd_i] = nums[i]
                odd_i += 1
            else:
                res[even_i] = nums[i]
                even_i += 1
        return res

'''
[Method 3]: 双指针（只保证奇偶分立两部分，不保证维持之前的顺序）
指针i, j分别首尾往中间遍历数组，只要i找到偶数j找到奇数就交换，直到i>=j
[Time]: O(n)
'''
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums)-1
        while i < j:
            if (not (nums[i] & 1) and (nums[j] & 1)):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif not (nums[i] & 1):
                j -= 1
            else:
                i += 1
        return nums
