'''
反转列表或者反转字符串

[Method 1]: Stack
利用其先进后出的特性，不过空间复杂度就大了

[Method 2]: 双指针
[code 1]:
'''
def reverse1(nums):
    i, j = 0, len(nums)-1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    print(nums)

'''
[code 2]表面上用for循环，实际上仍然是双指针，因为j = len(nums) - i - 1
'''
def reverse2(nums):
    n = len(nums)
    for i in range(n//2):
        nums[i], nums[n-i-1] = nums[n-i-1] = nums[i]
    print(nums)
