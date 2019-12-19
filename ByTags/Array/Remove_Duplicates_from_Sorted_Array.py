'''
26. Remove Duplicates from Sorted Array [Easy]
Given a sorted array nums, remove the duplicates in-place
such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.（也就是说，修改后的nums的前returned length的值都为排好序的不重复的数字。）

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5,
with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference,
which means modification to the input array will be known to the caller as well.

Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
'''

'''
O(n^2)
Runtime: 104 ms, faster than 40.72% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.4 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        count = 1
        i = len(nums) - 1
        while i > 0:
            if nums[i] == nums[i-1]:
                #worst case: O(n)
                nums.pop(i)
            else:
                count += 1
            i -= 1
        return count


'''
Two Pointers
O(n)
[Analysis]
in-place mutation of the first non-duplicate elements
Since the array is already sorted, we can keep two pointers i and j, where j is the slow-runner while i is the fast-runner.
As long as nums[i] = nums[j], we increment i to skip the duplicate.
When we encounter nums[i] != nums[j], the duplicate run has ended so we must copy its value to nums[j + 1].
 j is then incremented and we repeat the same process again until i reaches the end of array.

Runtime: 96 ms, faster than 76.89% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.5 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.

[思路]
非末端pop的删除操作会导致O(n)的时间复杂度，又要求O(1的)空间，
所以我们可以把每种数字的第一个数的index（初始为0）记下来，为newTail，然后从数组的第二个数开始与这个数（即A[newTail]）比较，
看是否相等。如果不等，我们更新这个index的下一位（即1），并使其值为第二种数字，如此for循环到最后一个元素。
最终返回最后一个不重复数字的index加上1，即为整个数组里不重复数字的总数。

e.g.
[1,1,1,2,3,3,4,5,5,6,6,6,7,7,7] ==>
[1, 2, 3, 4, 5, 6, 7, 5, 5, 6, 6, 6, 7, 7, 7]
'''
class Solution:
    def removeDuplicates(self, A):
        if not A:
            return 0
        #记录了每个不同数字的第一个数的index，最后加1就为不重复数字的总数
        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1

'''
O(n)
Runtime: 88 ms, faster than 97.92% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.9 MB, less than 5.74% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''
from collections import OrderedDict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] =  OrderedDict.fromkeys(nums)

'''
[Note]
1.Using nums[:] will not allocate new memory, it's in-place mutation,
so it will change the values already used by nums
rather than just reassigning the name nums to the newly created list.
nums[:]只是以in-place的方式修改其元素，但是nums = nums[:]则是重新赋值

Test this in python interpreter:

***nums = nums[:]是重新赋值***
>>> a = [1,2,3,4,5]
>>> b = a
>>> b
[1, 2, 3, 4, 5]
>>> a = a[:]
>>> a.pop()
5
>>> a
[1, 2, 3, 4]
>>> b
[1, 2, 3, 4, 5]
>>>

***nums[:]只是以in-place的方式修改其元素***
>>> b
[1, 2, 3, 4, 5]
>>> c = b
>>> c
[1, 2, 3, 4, 5]
>>> b[:] = [1,2,3]
>>> b
[1, 2, 3]
>>> c
[1, 2, 3]
>>>

2.OrderedDict will maintain the sorted order of nums while set() wouldn't
'''
