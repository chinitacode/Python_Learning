def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                

def bubble_sort2(nums):
    # We set is_sorted to False so the loop runs at least once
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                is_sorted = False
'''
Time Complexity:
In the worst case scenario (when the list is in reverse order),
this algorithm would have to swap every single item of the array.
Our swapped flag would be set to True on every iteration.
Therefore, if we have n elements in our list,
we would have n iterations per item
- thus Bubble Sort's time complexity is O(n^2).
'''


nums = [5,4,3,2,1]
nums2 = [6,7,8,2,8,2,1]
bubble_sort(nums)
bubble_sort(nums2)
print(nums)
print(nums2)

nums = [5,4,3,2,1]
nums2 = [6,7,8,2,8,2,1]
bubble_sort2(nums)
bubble_sort2(nums2)
print(nums)
print(nums2)

'''
#永远O（n^2）
first find the smallest element in the unsorted sublist
and place it at the end of the sorted sublist.
'''
def selection_sort(nums):
    for i in range(len(nums) - 1):
        min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]

    return nums

def insertion_sort(nums):
    for cursor in range(1, len(nums)):
        pos = cursor
        while pos > 0 and nums[pos - 1] > nums[pos]:
            nums[pos - 1], nums[pos] = nums[pos], nums[pos - 1]
            pos -= 1
    return nums

# O(n)
'''
Count sort is a linear time sorting algorithm that
sort in O(n+k) time when elements are in range from 1 to k.
'''
def count_sort(items):
    # find the minimal and maximum values of the input array
    # O(n)
    mmax, mmin = items[0], items[0]
    for i in range(1, len(items)):
        if (items[i] > mmax): mmax = items[i]
        elif (items[i] < mmin): mmin = items[i]
    print(mmin, mmax)
    
    # find the number of buckets
    nums = mmax - mmin + 1
    counts = [0] * nums
    
    # asign number of duplicates to those corresponding bucket
    # O(n)
    for i in range (len(items)):
        counts[items[i] - mmin] = counts[items[i] - mmin] + 1

    # sort the input array by asigning numbers to its pos
    # O(n), inspite of 2 for-loops, cuz they just loop through all n number
    pos = 0
    for i in range(nums):
        for j in range(counts[i]):
            items[pos] = i + mmin
            # pos is only changed when a number is asigned to the item
            pos += 1

    return items

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left_nums = quick_sort([x for x in nums[1:] if x < pivot])
    right_nums = quick_sort([x for x in nums[1:] if x >= pivot])
    return left_nums + [pivot] + right_nums

def quick_sort2(nums):
    def _quick_sort(low, high):
        if low <= high:
            pivot = nums[low - 1]
            i, j = low, high
            while True:
                while nums[i] < pivot and i < high:
                    i += 1
                while nums[j] >= pivot and j > low - 1:
                    j -= 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    nums[low - 1], nums[j] = nums[j], nums[low - 1]
                    break
       
            _quick_sort(low, j - 1)
            _quick_sort(j + 2, high)
    _quick_sort(1, len(nums) - 1)
    
random_list_of_nums = [5, 8, 10, 8, 9, 10, 8]
quick_sort2(random_list_of_nums)
print(random_list_of_nums)


def merge_sort(arr):
    if len(arr) > 1:
        #Finding the mid of the array 
        mid = len(arr) // 2
        # Dividing the array elements into 2 halves
        L = arr[:mid]
        R = arr[mid:]
        
        # Sorting the first half 
        merge_sort(L)
        # Sorting the second half 
        merge_sort(R)

        i = j = k = 0
        
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        
