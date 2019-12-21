'''
287. Find the Duplicate Number [Medium]
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
prove that at least one duplicate number must exist.
Assume that there is only one duplicate number,
find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

[注]：
按照 ：
1、哈希表判重(用set()或者Counter(),O(n)的时间和空间)，
2、O(nlgn)的排序（用quick sort可以in-place但是mutate了原数组）以后相邻元素相等即找到的重复(O(nlgn的时间和O(1)的空间))；
3、桶排序（鸽子洞原理，即“抽屉原理”）(O(n)的时间,O(1)的空间但是mutate了原数组)；
4、二分法。
然后分析一下这些方法的时间复杂度、空间复杂度，做一个简单比较，我觉得应该就很不错了。

[Method 1]: 快慢指针(利用linkedlistCycle的龟兔赛跑算法)
分为两步：

找到环
找到环的入口（即重复元素）

找环：
定义快慢指针slow=0,fast=0
进入循环：
slow每次走一步，即slow=nums[slow]
fast每次走两步，即fast=nums[nums[fast]]
当slow==fast时，退出循环。
当快慢指针相遇时，一定在环内。此时假设slow走了k步，则fast走了2k步。设环的周长为c，则有：
假设起点离环距离H，环长为c，则slow到环的入口时，fast一定走了2H, 在环内的H处，
实际上可以看成刚开始slow就在环的入口而fast在环的H处，两者相距H的距离。
然后最后slow和fast相遇，假设相遇在距离入口k距离的k点，则此时fast一定已经跑了一圈多的距离，

                          _____
                         /      \
                        /        H
           0_____H______E         \
                        \        /
                         k______/

根据其速度关系，有：
2(c-k) = c + (c-H-k)
得H = k

找环的入口：

因为H = k, 则如果把fast的指针重新定义为0，slow不动（留在k处），
然后fast和slow按每次走一步的速度继续走，最终会走完H(或者k距离)，最终在环的入口相遇。

当两指针相遇时，即fast == slow，返回slow

为何相遇时，找到的就是入口：
假设起点到环的入口(重复元素)，需要m步。此时slow走了n+m步，其中n是环的周长c的整数倍，
所以相当于slow走了m步到达入口，再走了n步。所以相遇时一定是环的入口。

复杂度分析
时间复杂度：O(n)
空间复杂度：O(1)
Runtime: 56 ms, faster than 48.04% of Python online submissions for Find the Duplicate Number.
Memory Usage: 13.6 MB, less than 45.24% of Python online submissions for Find the Duplicate Number.
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        fast = 0
        while True:
            slow, fast = nums[slow], nums[fast]
            if slow == fast:
                return slow


'''
[Method 2]: 二分法(分治，抽屉原理, 只适用于只有一个数重复的情况) O(nlogn)
这道题目主要应用了抽屉原理和分治的思想。

抽屉原理：n+1 个苹果放在 n 个抽屉里，那么至少有一个抽屉中会放两个苹果。

用在这个题目中就是，一共有 n+1 个数，每个数的取值范围是1到n，所以至少会有一个数出现两次。

然后我们采用分治的思想，将每个数的取值的区间[1, n]划分成[1, n/2]和[n/2+1, n]两个子区间，
然后分别统计两个区间中数的个数。
注意这里的区间是指 数的取值范围，而不是 数组下标。

划分之后，左右两个区间里一定至少存在一个区间，区间中数的个数大于区间长度。
这个可以用反证法来说明：如果两个区间中数的个数都小于等于区间长度，
那么整个区间中数的个数就小于等于n，和有n+1个数矛盾。

因此我们可以把问题划归到左右两个子区间中的一个，而且由于区间中数的个数大于区间长度，
根据抽屉原理，在这个子区间中一定存在某个数出现了两次。

依次类推，每次我们可以把区间长度缩小一半，直到区间长度为1时，我们就找到了答案。

复杂度分析
[时间复杂度]：每次会将区间长度缩小一半，一共会缩小 O(logn) 次。
每次统计两个子区间中的数时需要遍历整个数组，时间复杂度是 O(n)。
所以总时间复杂度是 O(nlogn)。
[空间复杂度]：代码中没有用到额外的数组，所以额外的空间复杂度是 O(1)。
Runtime: 68 ms, faster than 15.12% of Python online submissions for Find the Duplicate Number.
Memory Usage: 13.5 MB, less than 64.29% of Python online submissions for Find the Duplicate Number.
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return
        l,r = 1, len(nums)-1
        while l < r:
            mid = l + (r-l)//2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count <= mid:
                l = mid+1
            else:
                r = mid
        return l
