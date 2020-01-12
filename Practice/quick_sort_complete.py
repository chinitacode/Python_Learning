def quick_sort(array, l, r):
    if l >= r:
        return
    stack = []
    stack.append(l)
    stack.append(r)
    while stack:
        low = stack.pop(0)
        high = stack.pop(0)
        if high - low <= 0:
            continue
        x = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= x:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        stack.extend([low, i, i + 2, high])

nums = [5, 8, 4, 9, 2, 10, 8]
quick_sort(nums, 0, len(nums)-1)
print(nums)

