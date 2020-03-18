'''
658. Find K Closest Elements [Medium]

Given a sorted array, two integers k and x,
find the k closest elements to x in the array.
The result should also be sorted in ascending order.
If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]

Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104
UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers).
Please reload the code definition to get the latest changes.

[Method 1]: 双指针
[Time]: O(n)
[Space]: O(1)
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr,x) # 找到第一个大于等于x的数的索引
        i = j = idx
        while j-i < k:
            if i == 0:
                return arr[:k]
            if j == len(arr):
                return arr[-k:]
            if x - arr[i-1] <= arr[j] - x:
                i -= 1
            else:
                j += 1
        return arr[i:j]
