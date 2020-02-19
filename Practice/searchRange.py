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


def search_range(alist, target):
    if len(alist) == 0:
        return (-1, -1)  
    
    lbound, rbound = -1, -1

    # search for left bound 
    left, right = 0, len(alist) - 1
    while left + 1 < right: 
        mid = left + (right - left) // 2
        if alist[mid] == target:
            right = mid
        elif (alist[mid] < target):
            left = mid
        else:
            right = mid
            
    if alist[left] == target:
        lbound = left
    elif alist[right] == target:
        lbound = right
    else:
        return (-1, -1)

    # search for right bound 
    left, right = 0, len(alist) - 1        
    while left + 1 < right: 
        mid = left + (right - left) // 2
        if alist[mid] == target:
            left = mid
        elif (alist[mid] < target):
            left = mid
        else:
            right = mid
            
    if alist[right] == target:
        rbound = right
    elif alist[left] == target:
        rbound = left
    else:
        return (-1, -1)        
        
    return (lbound, rbound)
