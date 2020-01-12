def find_consecutive_ones(nums):
    local = maximum = 0
    for i in nums:
        local = local + 1 if i == 1 else 0
        maximum = max(maximum, local)
    return maximum

l1 = [1,1,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,1]
