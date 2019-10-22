'''
283. Move Zeroes [Easy]

Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

[Analysis]
This question comes under a broad category of "Array Transformation".
This category is the meat of tech interviews.
Mostly because arrays are such a simple and easy to use data structure.
Traversal or representation doesn't require any boilerplate code
and most of your code will look like the Pseudocode itself.

The 2 requirements of the question are:
    Move all the 0's to the end of array.
    All the non-zero elements must retain their original order.

It's good to realize here that both the requirements are mutually exclusive,
i.e., we can solve the individual sub-problems and then combine them for the final solution.

[Method 1]: 冒泡排序 Two-pointer
稳定，如果a原来在b前面并且a = b = 0，则排序后a依然在b前面。
[Note]:
[0, 0, 1]
[Time]: O(n*n)
[Space]: O(1), in-place
Runtime: 648 ms, faster than 5.00% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.1 MB, less than 5.97% of Python3 online submissions for Move Zeroes.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0 # 0的个数
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i+1, len(nums)-count):
                    if nums[j] == 0: continue #如果两个都为0，则略过当前的数，把第一个0往后移了再回来处理。
                    nums[i], nums[j] = nums[j], nums[i]
                    i = j
                count += 1

'''
[Method 2]: 计算0的个数
所谓要把0移动到数组后面，其实就是把非0数给移动到数组前面，
而每个非0数需要移动的步数其实就是这个非0数前面0的个数。

例如题目中的case：
[0, 1, 0, 3, 2]
即1需要移动1步，3和2需要移动两步。在完成这三个数的移动后，将后面补0即可。

[Time]: O(n)
[Space]: O(1)
Runtime: 56 ms, faster than 85.76% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.2 MB, less than 5.97% of Python3 online submissions for Move Zeroes.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                nums[i-count], nums[i] = nums[i], nums[i-count]

'''
[Method 3]: 记录0的index(非0数可以往前移的index)
把所有0往后移，相当于把所有非零数往前移。
因为要求非0数要保持顺序，所以每往前移，移完后把index加1。
[Time]: O(n)
[Space]: O(1)
Runtime: 68 ms, faster than 28.54% of Python3 online submissions for Move Zeroes.
Memory Usage: 15.2 MB, less than 5.97% of Python3 online submissions for Move Zeroes.
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != idx:
                    nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
