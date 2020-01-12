def find(nums):
    result = []
    temp = 0
    for i in range(len(nums)):
        temp = temp | (1 << nums[i] - 1)
        
    for j in range(1, len(nums) + 1):
        if temp | (1 << j - 1) != temp:
            result.append(j)
            
    return result


def findDisappearedNumbers2(nums):
    # For each number i in nums,
    # we mark the number that i points as negative.
    # Then we filter the list, get all the indexes
    # who points to a positive number
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        nums[index] = - abs(nums[index])

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]
