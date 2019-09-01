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
'''

'''
Method: Two-pointer
O(n)
Code1:
Runtime: 132 ms, faster than 96.28% of Python3 online submissions for Container With Most Water.
Memory Usage: 15.2 MB, less than 5.26% of Python3 online submissions for Container With Most Water.
[Analysis]
If height[L] < height[R], move L, else move R.
Say height[0] < height[5], area of (0, 4), (0, 3), (0, 2), (0, 1) will be smaller than (0, 5),
so no need to try them.
'''
def maxArea(self, height):
    L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
    for w in range(width, 0, -1):
        if height[L] < height[R]:
            res, L = max(res, height[L] * w), L + 1
        else:
            res, R = max(res, height[R] * w), R - 1
    return res

'''
code2:
Runtime: 124 ms, faster than 99.85% of Python3 online submissions for Container With Most Water.
Memory Usage: 15.3 MB, less than 5.26% of Python3 online submissions for Container With Most Water.
Next challenges:
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxSum = 0
        while(i < j):
            width = j-i
            if height[i] < height[j]:
                length = height[i]
                i += 1
            else:
                length = height[j]
                j -= 1
            current_sum = length * width
            if maxSum < current_sum:
                maxSum = current_sum
        return maxSum

'''
code3:
Runtime: 116 ms, faster than 100.00% of Python3 online submissions for Container With Most Water.
Memory Usage: 15.4 MB, less than 5.26% of Python3 online submissions for Container With Most Water.
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        #O(n)
        maxh, ans, i, j = max(height), 0, 0, len(height)-1

        #loop through width k by decreasing from the longthest width
        for k in range(len(height)-1, 0, -1):
            if ans // k > maxh:
                break
            if height[i] < height[j]:
                if height[i] * k > ans:
                    ans = height[i] * k
                i += 1
            else:
                if height[j] * k > ans:
                    ans = height[j] * k
                j -= 1
        return ans
