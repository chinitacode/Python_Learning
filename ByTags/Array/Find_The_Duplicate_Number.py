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
二分法(只适用于只有一个数重复的情况)
按题目表达，设数组长度为n，则数组中元素∈[1,n−1]，且只有一个重复元素。
一个直观的想法，设一个数字k∈[1,n−1]，统计数组中小于等于kk的数字的个数count：

若count<=k，说明重复数字一定在(k,n-1]的范围内。
若count>k，说明重复数字一定在[0,k]的范围内。
利用这个性质，我们使用二分查找逐渐缩小重复数字所在的范围。

初试化左右数字边界left=1,right=n-1
循环条件left<right:
mid=(left+right)//2
按照性质，统计数组中小于等于mid的元素个数count
若 count<=mid，说明重复数字一定在(mid,right]的范围内。令left=mid+1
若count>mid，说明重复数字一定在[left,mid]的范围内。令right=mid。
返回left

[复杂度分析]
时间复杂度：OO(nlog(n))，二分法执行了log(n)次遍历n，因此复杂度为O(nlog(n))。
空间复杂度：O(1)
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
