'''
75. Sort Colors [Medium]

Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's,
then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with a one-pass algorithm using only constant space?


[Method 1]: Counting Sort
First, iterate the array counting number of 0's, 1's, and 2's,
then overwrite array with total number of 0's, then 1's and followed by 2's.
[Time]: O(2N) = O(N)
[Space]: O(range),range其实为2-0+1=3
Runtime: 32 ms, faster than 59.34% of Python3 online submissions for Sort Colors.
Memory Usage: 13 MB, less than 95.31% of Python3 online submissions for Sort Colors.
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0]*3
        for num in nums:
            counter[num] += 1
        k = 0
        for i in range(3):
            while counter[i]:
                nums[k] = i
                counter[i] -= 1
                k += 1


'''
[Method 2]: 双指针(实际上是三指针)
原理和快排的partition相似。用i来对nums进行遍历
l指示最后一个0的下一位，r指示第一个2的前一位。
[Time]: O(n), 一次遍历
[Space]: O(1)
Runtime: 32 ms, faster than 59.34% of Python3 online submissions for Sort Colors.
Memory Usage: 13 MB, less than 95.31% of Python3 online submissions for Sort Colors.
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,l,r = 0,0,len(nums)-1
        while i <= r: # 因为r后面的都是排好序的，所以当i到r时最后再检测一次
            if nums[i] == 2:
                nums[i],nums[r] = nums[r],nums[i]
                r -= 1 # 此时不需要移动i，因为交换后的nums[i]的值还不知道
            elif nums[i] == 0:
                nums[i],nums[l] = nums[l],nums[i]
                l += 1
                i += 1 # i需要移动因为交换后的i是从l来的，l是我们默认的最后一个0的下一位，即1
            else:
                i += 1 # 即nums[i]为1，默认放中间
