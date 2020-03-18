'''
169. Majority Element [Easy]
Given an array of size n, find the majority element.
The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

[Method 1]: Hashmap
[Time]: O(n), key in dict: O(1)
Runtime: 152 ms
Memory Usage: 13.4 MB
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
                if count[num] > n // 2:
                    return num
            else:
                count[num] = 1
'''
# Or:
Runtime: 212 ms, faster than 22.41% of Python3 online submissions for Majority Element.
Memory Usage: 15 MB, less than 7.14% of Python3 online submissions for Majority Element.
'''
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > n:
                return num



'''
[Method 2]: Using Counter()
Runtime: 224 ms, faster than 9.21% of Python3 online submissions for Majority Element.
Memory Usage: 15.4 MB, less than 7.14% of Python3 online submissions for Majority Element.
'''
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        count = Counter(nums)
        for num in nums:
            if count[num] > n:
                return num

'''
[Method 4]: sorting
[Time]: O(nlgn)
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums)/2]

'''
[Method 5]: Divide and Conquer
如果我们知道数组左边一半和右边一半的众数，我们就可以用线性时间知道全局的众数是哪个。
[算法]
这里我们使用经典的分治算法递归求解，直到所有的子问题都是长度为 1 的数组。
由于传输子数组需要额外的时间和空间，所以我们实际上只传输子区间的左右指针 lo 和 hi 表示相应区间的左右下标。
长度为 1 的子数组中唯一的数显然是众数，直接返回即可。
如果回溯后某区间的长度大于 1 ，我们必须将左右子区间的值合并。
如果它们的众数相同，那么显然这一段区间的众数是它们相同的值。
否则，我们需要比较两个众数在整个区间内出现的次数来决定该区间的众数。
原问题的答案就是下标为 0 和 n 之间的众数这一子问题。

[Time]: O(nlgn),函数 majority_element_rec 会求解 2 个长度为 n//2 的子问题，
并做两遍长度为 n 的线性扫描。
因此，分治算法的时间复杂度可以表示为：T(n)=2T(n/2)+2n
[Space]: O(lgn)
Runtime: 336 ms, faster than 5.20% of Python3 online submissions for Majority Element.
Memory Usage: 15.5 MB, less than 7.14% of Python3 online submissions for Majority Element.
'''
class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)

#TLE
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        def helper(lo, hi):
            if lo == hi:
                return nums[lo]
            mid = (hi-lo)//2 + lo
            l = helper(lo, mid)
            r = helper(mid+1, hi)
            if l == r:
                return l
            return [r, l][nums.count(l) > n]
        return helper(0, len(nums)-1)

# Or Using Slicing (with extra space)
def majorityElement6(self, nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]
    a = self.majorityElement(nums[:len(nums)//2])
    b = self.majorityElement(nums[len(nums)//2:])
    if a == b:
        return a
    return [b, a][nums.count(a) > len(nums)//2]
'''
[Method 6]: Boyer-Moore 投票算法
如果我们把众数记为 +1，把其他数记为 −1，将它们全部加起来，显然和大于 0 ，
从结果本身我们可以看出众数比其他数多。
[Time]：O(n), Boyer-Moore 算法严格执行了 nn 次循环，所以时间复杂度是线性时间的。
[Space]：O(1), Boyer-Moore 只需要常数级别的额外空间。

'''
def majorityElement(nums):
    count, cand = 0, 0
    for num in nums:
        if num == cand:
            count += 1
        elif count == 0:
            cand, count = num, 1
        else:
            count -= 1
    return cand

'''
[Method 7]: Bit manipulation
'''
def majorityElement5(nums):
    bit = [0]*32
    for num in nums:
        for j in range(32):
            bit[j] += num >> j & 1
    res = 0
    for i, val in enumerate(bit):
        if val > len(nums)//2:
            # if the 31th bit if 1,
            # it means it's a negative number
            if i == 31:
                res = -((1<<31)-res)
            else:
                res |= 1 << i
    return res

# Or shorter:
def majorityElement(nums):
    return (sum((sum(n>>i&1 for n in nums) > len(nums)/2) << i
                for i in range(32)) + 2**31) % 2**32 - 2**31
