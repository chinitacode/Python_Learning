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

#Or use while loop(slower)
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

# Vice Versa:
def findKthSmallest(nums, k):
    return findKthLargest(nums, len(nums) + 1 - k)
