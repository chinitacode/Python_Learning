def largest_twice(nums):
    largest = second = 0

    for i in range(len(nums)):
        if largest < nums[i]:
            second, largest = largest, nums[i]
            index = i

        elif second < nums[i]:
            second = nums[i]

    return index if largest >= second * 2 else -1

nums = [1, 2,3,8,3,2,1]
