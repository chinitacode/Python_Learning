# 50. Pow(x, n)
# Recursive:
def myPow(x, n):
        if n == 0:
            return 1.0
        if n > 0:
            if n % 2 == 0:
                return self.myPow(x*x, n>>1)
            else:
                return x * self.myPow(x*x, n>>1)
        else:
            return 1 / self.myPow(x, -n)

# Iterative:
def myPow2(x, n):
        if n < 0:
            x = 1/x
            n = -n
        result, curr_product = 1, x
        while n > 0:
            # n will always be reduced to 1 in the end,
            #Then the result needs to be updated
            if n % 2:
                result = result * curr_product
            curr_product *= curr_product
            n //= 2
        return result
# 162. Find Peak Element


# Binary Search:
def findPeakElement1(nums):
    nums = [-float('inf')] + nums + [-float('inf')]
        l, r = 0, len(nums)-1
        while l <= r:
            # 终止条件在l==r后，使得m = l,进行最终判断
            m = l + (r-l)//2
            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                #因为收尾添加了inf元素，最后输出的index要减1
                return m - 1
            if nums[m-1] < nums[m+1]:
                l = m + 1
            else:
                r = m - 1

def findPeakElement2(nums):
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left)//2
            if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            if nums[mid - 1] > nums[mid] and nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        if nums[left] > nums[right]:
            return left
        return right

# 215. Kth Largest Element in an Array
# Method 1: quick sort + random seed, O(n), the best solution
import random
def findKthLargest(self, nums, k):
    x = random.randint(0, len(nums) - 1)
    nums[0], nums[x] = nums[x], nums[0]

    r = [num for num in nums[1:] if num > nums[0]]
    if len(r) == k - 1: return nums[0]
    if len(r) > k - 1: return self.findKthLargest(r, k)

    l = [num for num in nums[1:] if num <= nums[0]]
    return self.findKthLargest(l, k - len(r) - 1)

# Method 2 (quick_sort, random seed, divide and conquer)
def partition(nums, l, r):
    # random seed is the most crucial step
    x = random.randint(l, r)
    nums[l], nums[x] = nums[x], nums[l]
    pivot_idx = l
    for i in range(l+1, r+1):
        if nums[i] >= nums[l]:
            pivot_idx += 1
            nums[i], nums[pivot_idx] = nums[pivot_idx], nums[i]
    nums[l], nums[pivot_idx] = nums[pivot_idx], nums[l]
    return pivot_idx

# Use while loop
def partition2(nums, l, r):
    # choose the right-most element as pivot
    pivot_idx = l
    while l < r:
        if nums[l] >= nums[r]:
            # put the element no smaller than pivot to the start of nums
            nums[l], nums[pivot_idx] = nums[pivot_idx], nums[l]
            pivot_idx += 1
        l += 1
    nums[r], nums[pivot_idx] = nums[pivot_idx], nums[r]
    return pivot_idx

def findKthLargest(nums, k):
    pivot_idx = self.partition(nums, 0, len(nums)-1)
    if pivot_idx + 1 == k:
        return nums[pivot_idx]
    if pivot_idx + 1 > k:
        return self.findKthLargest(nums[:pivot_idx], k)
    else:
        return self.findKthLargest(nums[pivot_idx + 1:], k - pivot_idx - 1)

def findKthSmallest(nums, k):
    return findKthLargest(nums, len(nums) + 1 - k)


# 349. Intersection of Two Arrays
# Method 1: Use set()
def intersection1(nums1, nums2):
    return list(set.intersection(set(nums2), set(nums1)))

#Method 3: Sort and Binary Search:
# O((m+n)lg(min(m,n))
def intersection2(nums1, nums2):
    if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    nums2.sort() #O(nlgn)
    result = []
    for num in nums1: #O(m)
        left, right = 0, n-1
        while left <= right: #O(lgn)
            mid = left + (right - left)//2
            if num == nums2[mid]:
                if num not in result:
                    result.append(num)
                break
            if num < nums2[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return result

#Method 3: When the two arrays have similar size,
# Sort and use two pointers(piggybacking on Merge Sort)
# O(nlgn + n) => O(nlgn)
def intersection2(nums1, nums2):
    nums1.sort()
    nums2.sort()
    result = []
    i, j = 0, 0
    m, n = len(nums1), len(nums2)
    while i < m and j < n:
        if nums1[i] == nums2[j]:
            if not result or nums1[i] != result[-1]:
                result.append(nums1[i])
            i += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result

# 350. Intersection of Two Arrays II
# if nums1=[1, 2, 2, 1], nums2 = [2], return only [2] (means that both i and j shoule increase by 1)
# Sort and binary Search, O((m+n)lgn)
def intersection_ii1(nums1, nums2):
    if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    nums2.sort() #O(nlgn)
    counts, result = {}, []
    for num in nums2: # O(n)
        counts[num] = counts.get(num, 0) + 1
    for num in nums1: #O(m)
        left, right = 0, n-1
        while left <= right: #O(lgn)
            mid = left + (right - left)//2
            if num == nums2[mid]:
                if counts[num]:
                    result.append(num)
                    counts[num] -= 1
                break
            if num < nums2[mid]:
                right = mid - 1
            else:
                left = mid + 1
    return result

#Sort and use two pointers(piggybacking on Merge Sort)
# O(max(m,n)lg(max(m,n)))
def intersection_ii2(nums1, nums2):
    nums1.sort()
    nums2.sort()
    result = []
    i, j = 0, 0
    m, n = len(nums1), len(nums2)
    while i < m and j < n:
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            j += 1
            i += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result

# with small modification:
'''
since both array are sorted, the next value will be larger than the current value
and therefore will be after the previously found location,
so we do not need to search in range [0,end], but [prev_loc, end].
O(min(m,n)*log(max(m,n)). 
If n << m, this is faster than the solution with two pointers.
'''
from bisect import bisect_left
def intersection_ii2(nums1, nums2):
    nums1.sort(); nums2.sort()
    if len(nums1) > len(nums2):
         shorter, longer = nums2, nums1
    else:
         shorter, longer = nums1, nums2
    start = 0; end = len(longer)
    res = []
    for n in shorter:
        start = bisect_left(longer, n, start, end)
        if start != end and longer[start] == n:
            res.append(longer[start])
            start += 1
    return res
