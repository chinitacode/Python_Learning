'''
42. Trapping Rain Water [Hard]
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.
Thanks Marcos for contributing this image!

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


[Method 1]: Brute Force + 按行求 (TLE)
就是先求高度为 1 的水，再求高度为 2 的水，再求高度为 3 的水......。
整个思路就是，求第 i 层的水，遍历每个位置，如果当前的高度小于 i，
并且两边有高度大于等于 i 的，说明这个地方一定有水，水就可以加 1。

如果求高度为 i 的水，首先用一个变量 temp 保存当前累积的水，初始化为 0。
从左到右遍历墙的高度，遇到高度大于等于 i 的时候，开始更新 temp。
更新原则是遇到高度小于 i 的就把 temp 加 1，
遇到高度大于等于 i 的，就把 temp 加到最终的答案 ans 里，并且 temp 置零，然后继续循环。

[Time: ]如果最大的数是 m，个数是 n，那么就是 O(m*n)。
[Space]: O(1)。

[Note]:
若其中某个高度特别高，则会做很多无用的遍历, 所以TLE, 不能被AC。


[Method 2]: Brute Force + 按列表求
求每一列的水，我们只需要关注当前列，以及左边最高的墙，右边最高的墙就够了。
装水的多少，当然根据木桶效应，我们只需要看左边最高的墙和右边最高的墙中较矮的一个就够了。
所以，根据较矮的那个墙和当前列的墙的高度可以分为2种情况:
1.较矮的墙高于当前列：注水；
2.较矮的墙低于或者等于当前列：不注水。
[Time]: O(n*n)，两层遍历，最外层遍历每一列，最内层则分别向左向右求最高左墙和最高右墙。
[Space]: O(1)
Runtime: 2132 ms, faster than 5.02% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.6 MB, less than 6.98% of Python3 online submissions for Trapping Rain Water.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(1, len(height)-1):
            wid = min(max(height[:i]), max(height[i+1:]))
            water += (wid - height[i]) if height[i] < wid else 0
        return water

'''
[Method 3]: DP
我们注意到，解法二中。对于每一列，我们求它左边最高的墙和右边最高的墙，
都是重新遍历一遍所有高度，这里我们可以优化一下。

首先用两个数组，max_left [i] 代表第 i 列左边最高的墙的高度，
max_right[i] 代表第 i 列右边最高的墙的高度。（一定要注意下，第 i 列左（右）边最高的墙，是不包括自身的）
即：
max_left [i] = Max(max_left [i-1],height[i-1])；
max_right[i] = Max(max_right[i+1],height[i+1])。
这样，我们再利用解法二的算法，就不用在 for 循环里每次重新遍历一次求 max_left 和 max_right 了。
[Time]: O(n)；
[Space]: O(n)
Runtime: 68 ms, faster than 31.40% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.6 MB, less than 6.98% of Python3 online submissions for Trapping Rain Water.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        max_left, max_right = [0] * len(height), [0] * len(height)
        for i,j in zip(range(1, len(height)-1), range(len(height)-2, -1, -1)):
            max_left[i] = max(max_left[i-1], height[i-1])
            max_right[j] = max(max_right[j+1], height[j+1])
        for i in range(1, len(height)-1):
            wid = min(max_left[i], max_right[i])
            water += (wid - height[i]) if height[i] < wid else 0
        return water



'''
[Method 4]: Two-Pointer
动态规划中，我们常常可以对空间复杂度进行进一步的优化。
例如这道题中可以看到，max_left [ i ] 和 max_right [ i ] 数组中的元素我们其实只用一次，
而且每列的注水只与min(max_left[i], max_right[i]) 和height[i]有关。
只要right_max[i]>left_max[i] （元素 0 到元素 6），积水高度将由 left_max 决定，
类似地left_max[i]>right_max[i]（元素 8 到元素 11）
所以我们可以认为如果一端有更高的条形块（例如右端），积水的高度依赖于当前方向的高度（从左到右）。
当我们发现另一侧（右侧）的条形块高度不是最高的，我们则开始从相反的方向遍历（从右到左）。

所以我们可以不用数组max_left和max_right，因为我们只需要知道左右墙哪边低，则min就是哪边。
然后判断当前列的高度与min的高低，低则注水，否则不注水。
我们从1和len(height)-2的index处设l，r左右两个指针，max_left和max_right都初始为0。
对于l,有max_left = max(max_left, height[l-1])
对于r,有max_right = max(max_right, height[r+1])
因为max_left和max_right都初始为0，则如果height[l-1] < height[r+1], 有max_left < max_right。

[Time]: O(n)
[Space]: O(1)
Runtime: 64 ms, faster than 51.27% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.6 MB, less than 6.98% of Python3 online submissions for Trapping Rain Water.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        max_left, max_right = 0, 0
        l, r = 1, len(height)-2
        for i in range(1, len(height)-1):
            if height[l-1] < height[r+1]:
                max_left = max(max_left, height[l-1])
                Min = max_left
                if Min > height[l]:
                    water += Min - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r+1])
                Min = max_right
                if Min > height[r]:
                    water += Min - height[r]
                r -= 1
        return water


'''
[Method 5]: Stack

用栈来跟踪可能储水的最长的条形块。使用栈就可以在一次遍历内完成计算。
我们在遍历数组时维护一个栈。
如果当前的条形块小于或等于栈顶的条形块，我们将条形块的索引入栈，
意思是当前的条形块被栈中的前一个条形块界定。
如果我们发现一个条形块长于栈顶，我们可以确定栈顶的条形块被当前条形块和栈的前一个条形块界定，
因此我们可以弹出栈顶元素并且累加答案到ans。

[算法]
使用栈来存储条形块的索引下标。
遍历数组：
当栈非空且height[current] > height[stack.top()]
意味着栈中元素可以被弹出, 弹出栈顶元素top。
计算当前元素和栈顶元素的距离，准备进行填充操作
distance=current−stack.top()−1
找出界定高度
bounded_height = min(height[current], height[stack.top()])−height[top]
往答案中累加积水量ans += distance×bounded_height
将当前索引下标入栈,
将current移动到下个位置。
[Time]: O(n)。单次遍历 O(n)，每个条形块最多访问两次（由于栈的弹入和弹出），并且弹入和弹出栈都是O(1)。
[Space]: O(n)。 栈最多在阶梯型或平坦型条形块结构中占用O(n) 的空间。
Runtime: 60 ms, faster than 76.13% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 14.6 MB, less than 6.98% of Python3 online submissions for Trapping Rain Water.
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        stack = []
        for curr in range(len(height)):
            while stack and height[curr] > height[stack[-1]]:
                top = stack.pop()
                if not stack: break
                length = curr - stack[-1] - 1
                #高度差，即注水矩形的有效宽度
                bounded = min(height[curr], height[stack[-1]]) - height[top] #减去中间的墙的高度
                water += length*bounded
            stack.append(curr)
        return water
