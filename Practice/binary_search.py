'''
【二分查找】
实现一个有序数组的二分查找算法
实现模糊二分查找算法（比如大于等于给定值的第一个元素）
'''

'''
Return the index of any element that meet the condition
and the following two method return the index of the middle element

def binary_search(arr, num):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2 #(left + right)//2, 防止左边的和有可能溢出
        if num == arr[mid]:
            return mid
        if num < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_recur(arr, num):
    def bi_search(left, right):
        # Not found
        if left > right:
            return -1

        mid = left + (right - left)// 2
        if num == arr[mid]:
            return mid
        elif num < arr[mid]:
            return bi_search(left, mid - 1)
        else:
            return bi_search(mid + 1, right)
    return bi_search(0, len(arr) - 1)
'''

# Return the first index of a duplicate element that meet the condition
def binarysearch1(alist, item):
    if len(alist) == 0:
        return -1

    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == item:
            right = mid
        elif alist[mid] < item:
            left = mid
        else:
            right = mid

    if alist[left] == item:
        return left
    if alist[right] == item:
        return right
    return -1


def binarysearch2(alist, item):
    if len(alist) == 0:
        return -1

    left, right = 0, len(alist) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if alist[mid] == item:
            left = mid
        elif alist[mid] < item:
            left = mid
        else:
            right = mid

    if alist[right] == item:
        return right
    if alist[left] == item:
        return left
    return -1

# 153. Find Minimum in Rotated Sorted Array
def findMin(alist):
    if len(alist) == 0:
        return -1
    left, right = 0, len(alist) - 1
    while left + 1 < right:
        if (alist[left] < alist[right]):
            return alist[left];
        mid = left + (right - left) // 2
        if (alist[mid] >= alist[left]):
            left = mid + 1
        else:
            right = mid
    return alist[left] if alist[left] < alist[right] else alist[right]

def findMin2(nums):
    if len(nums) == 1:
        return nums[0]
    left, right = 0, len(nums) - 1
    # if the last element is greater than the first element then there is no rotation.
    if nums[right] > nums[left]:
        return nums[left]

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        else:
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
# 33. Search in Rotated Sorted Array
def search(nums, target):
    if len(nums) < 1:
        return -1
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[left] < nums[mid]:
            if nums[left] <= target and target <= nums[mid]:
                right = mid
            else:
                left = mid
        else:
            if nums[mid] <= target and target <= nums[right]:
                left = mid
            else:
                right = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1

# 81. Search in Rotated Sorted Array II
def search(nums, target):
    if len(nums) == 0:
        return False
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return True
        if nums[mid] == nums[right]: # get rid of the duplicate number
            right -= 1  # worst case O(n)
        elif nums[mid] > nums[right]: #left side is sorted
            if nums[left] <= target and target <= nums[mid]:
                right = mid
            else:
                left = mid
        else: # right side is sorted
            if nums[mid] <= target and target <= nums[right]:
                left = mid
            else:
                right = mid
    if nums[left] == target or nums[right] == target:
        return True
    return False

# 35. Search Insert Position
# 相当于要找到第一个大于等于target的数的index
# 相当于 bisect 模块的 bisect([arr], target)
def searchInsert(nums, target):
    if len(nums) < 1:
        return 0

    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            right = mid
        else:
            left = mid

    if nums[left] >= target:
        return left
    if nums[right] >= target:
        return right
    else:
        return right + 1
# 34. Find First and Last Position of Element in Sorted Array
def searchRange(nums, target):
    if len(nums) < 1:
        return [-1, -1]
    # search for start position(the first appeared num)
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid
    if nums[left] == target:
        start = left
    elif nums[right] == target:
        start = right
    else:
        return [-1, -1]

    # search for end position(the first appeared num)
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            left = mid
        if target < nums[mid]:
            right = mid
        else:
            left = mid
    if nums[right] == target:
        end = right
    elif nums[left] == target:
        end = left
    else:
        return [-1, -1]
    return [start, end]

# worst case: O(n)
def search_empty(nums, target):
    '''
    >>> search_empty(['', '', '', '', '', '', '', ''], 1)
    -1
    >>> search_empty(['', '', '', 1, '', '', 2, '', '', '', '', 3, '', '', ''], 2)
    6
    '''

    if len(nums) == 0:
        return -1
    left, right = 0, len(nums) - 1

    while left + 1 < right:
        while left < right and nums[right] == '':
            right -= 1
        if nums[right] == '':
            right -= 1
        if right < left:
            return -1

        mid = left + (right - left) // 2
        while nums[mid] == '' and mid < right:
            mid += 1
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1

#   Search 1st Position of element in Infinite Array
def search_first(nums, target):
    '''
    >>> search_first([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5], 4)
    21
    >>> search_first([0, 0, 0, 0, 0, 1], 1)
    5
    >>> search_first([-1,0,3,5,9,12], 2)
    -1
    >>> search_first([-1,0,3,5,9,12], 15)
    -1
    '''
    left, right = 0, 1
    while nums[right] < target:
        left = right
        right *= 2
        if right > len(nums):
            right = len(nums) - 1
            break

    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            right = mid
        elif nums[mid] < target:
            left = mid
        else:
            right = mid
    if nums[left] == target:
        return left
    if nums[right] == target:
        return right
    return -1

# 475. Heaters
from bisect import bisect

def findRadius(houses, heaters):
    heaters = [float('-inf')] + sorted(heaters) + [float('inf')]
    result = 0

    for h in houses:
        # find the position to the two heaters around the house
        pos = bisect(heaters, h) # return the inserting position of h in Heaters
        left = heaters[pos - 1]
        right = heaters[pos]
        result = max(result, min(h - left, right - h))
    return result

# 74. Search a 2D Matrix
def searchMatrix(matrix, target):
    if not matrix or not matrix[0]: return False
    m, n = len(matrix), len(matrix[0])
    row = 0
    while row < m - 1 and matrix[row][-1] < target:
        row += 1
    if matrix[row][0] <= target and target <= matrix[row][-1]:
        left, right = 0, n-1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                left = mid
            else:
                right = mid
        if matrix[row][left] == target or matrix[row][right] == target:
            return True
        return False

def searchMatrix2(matrix, target):
    '''
    subtract 1 as the bisect call "returns an insertion point which comes
    after (to the right of) any existing entries of x in a."
    '''
    if not matrix or not matrix[0]: return False
    i = bisect.bisect([row[0] for row in matrix], target) - 1
    j = bisect.bisect(matrix[i], target) - 1
    return matrix[i][j] == target

def searchMatrix3(matrix, target):
    return len(matrix) > 0 and len(matrix[0]) > 0 and matrix[bisect.bisect([row[0] for row in matrix], target)-1][bisect.bisect(matrix[bisect.bisect([row[0] for row in matrix], target)-1], target)-1] == target

#240. Search a 2D Matrix II
def search_Matrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m < 1 :
            return False
        n = len(matrix[0])
        if n < 1:
            return False
        row = 0
        while row < m - 1 and matrix[row][0] <= target:
            row += 1
        print(row)
        for r in range(row + 1):
            if matrix[r][0] <= target and target <= matrix[r][-1]:
                left, right = 0, n-1
                while left + 1 < right:
                    mid = left + (right - left) // 2
                    if matrix[r][mid] == target:
                        return True
                    if matrix[r][mid] < target:
                        left = mid
                    else:
                        right = mid
                if matrix[r][left] == target or matrix[r][right] == target:
                    return True

        return False

# 287. Find the Duplicate Number
def findDuplicate(nums):
    '''
    >>> findDuplicate([3,1,3,4,2])
    3
    >>> findDuplicate([1,3,4,2,2])
    2
    >>> findDuplicate([1, 3, 4, 2, 7, 6, 5, 6])
    6
    '''

    nums.sort()
    left, right = 0, len(nums) - 1
    while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] < mid + 1:
            right = mid
        else:
            left = mid
    if nums[left] == nums[right]:
        return nums[left]

# 378. Kth Smallest Element in a Sorted Matrix
# method 1: O(nlgnlg(matrix[-1][-1] - matrix[0][0]))
from bisect import bisect
def kthSmallest1(matrix, k):
    lo, hi = matrix[0][0], matrix[-1][-1]
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if sum(bisect(row, mid) for row in matrix) < k:
            lo = mid+1
        else:
            hi = mid
    return hi

# method 2: O(nlg(max - min))
def kthSmallest(matrix, k):

    L, R = matrix[0][0], matrix[-1][-1]
    while L < R:
        mid = L + (R - L) // 2
        temp = search_lower_than_mid(matrix, mid)
        if temp < k:
            L = mid + 1
        else:
            R = mid
    return L

def search_lower_than_mid(matrix, x):
    n, m = len(matrix), len(matrix[0])
    i, j = n - 1, 0
    cnt = 0
    while i >= 0 and j < m:
        if matrix[i][j] <= x:
            j += 1
            cnt += i + 1
        else:
            i -= 1
    return cnt

# 56. Merge Intervals
def merge(intervals):
    intervals.sort(key = lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][-1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][-1] = max(merged[-1][-1], interval[-1])
    return merged


# 57. Insert Interval
# 仍然是先把intervals排序，把newInterval插进去，然后再合并区间
from bisect import bisect

def insert(intervals, newInterval):
    intervals.sort(key = lambda x: x[0])
    pos = bisect([interval[0] for interval in intervals], newInterval[0])
    intervals = list(intervals[:pos]) + [newInterval] + list(intervals[pos:])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][-1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][-1] = max(merged[-1][-1], interval[-1])
    return merged

def insert2(intervals, newInterval):
    merged = []
    for i in intervals:
        if newInterval is None or i[-1] < newInterval[0]:
            merged += i,
        elif i[0] > newInterval[-1]:
            merged += newInterval,
            merged += i,
            newInterval = None
        else:
            newInterval[0] = min(newInterval[0], i[0])
            newInterval[-1] = max(newInterval[-1], i[-1])
    if newInterval is not None:
        merged += newInterval,
    return merged
