'''
41. First Missing Positive [Hard]
Given an unsorted integer array,
find the smallest missing positive integer.
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.

[Method 1]: 抽屉原理
思路沿用题目448。
1.先把所有不在1到N之间的数设置为0，即所有消失的数。
2.将每个存在的（不为零的）数看为index，即对应的index有数存在，得分两种情况处理：
    1.对应index不为零，则设置为负；
    2.为零, 为了使其不干扰别的index，设置为指向该index的负数，表明自身被占用。
3.最后一遍循环，返回第一个非负数应对应的正数。
4.若没有非负数，则说明数组是满的，返回 N+1。
[Time] : O(3n) = O(n)
[Space]: O(1)
Runtime: 44 ms, faster than 61.42% of Python3 online submissions for First Missing Positive.
Memory Usage: 13.7 MB, less than 8.70% of Python3 online submissions for First Missing Positive.
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0 or nums[i] > n:
                nums[i] = 0
        for i in range(n):
            num = nums[i]
            if num != 0:
                index = abs(num) - 1
                if nums[index] == 0:
                    nums[index] = -abs(num)
                else:
                    nums[index] = -abs(nums[index])
        for j in range(n):
            if nums[j] >= 0:
                return j+1
        return n+1

'''
[Method 2]: 桶排序
通过转换把数字返回自己应当的位置上。
[Time]: O(2n) = O(n)
[Space]: O(1)
Runtime: 60 ms, faster than 6.72% of Python3 online submissions for First Missing Positive.
Memory Usage: 13.9 MB, less than 8.70% of Python3 online submissions for First Missing Positive.
'''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            # 1次至少放对1个数，如果被交换的数在1~N范围内，则再交换一次，最多需要换N-1次
            # 如[-1,4,3,-2], i = 1时，先4与-2交换，变成[-1,-2,3,4], 交换后-2不在1~N范围内，则任其放在那，继续i += 1;
            # 或者如[3,4,2,2], i = 0时，先3与2换，再2与4换，再4与2换，最后2和2相等，不换，共3次。
            # nums[i] != nums[nums[i] - 1]是必须，如果遇到[1,1]
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # ！！！ 这里先把i赋值给index
                index = nums[i] - 1
                # 因为此处nums[i]被改变了，若把index换成 nums[i] - 1，
                # 则 nums[i] - 1也已经发生了改变，并非之前我们希望的index。
                # 不过可以换一下顺序，则没问题：
                # nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                nums[i], nums[index] = nums[index], nums[i]

        for j in range(n):
            if nums[j] != j+1:
                return j+1
        return n+1
