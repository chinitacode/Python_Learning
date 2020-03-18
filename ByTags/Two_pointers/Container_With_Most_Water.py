'''
11. Container With Most Water [Medium]
Given n non-negative integers a1, a2, ..., an ,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container,
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49

[Method 1]: 双指针
Runtime: 132 ms, faster than 63.44% of Python3 online submissions for Container With Most Water.
Memory Usage: 14.4 MB, less than 71.58% of Python3 online submissions for Container With Most Water.
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        water = float('-inf')
        while i < j:
            # 因为水的体积是底*height，而height是取小的值，所以当i高的时候移动只会使得体积变小(height不变而底-1)
            width = j-i
            if height[i] < height[j]:
                h = height[i]
                i += 1
            else:
                h = height[j]
                j -= 1
            area = width*h
            if area > water: water = area
        return water
