def permute(nums):
    res = [[]]
    #iterate through the element in nums, each time insert one element:
    for n in nums:
        #create an empty list to store the temporary element permutated
        tmp = []
        # insert the new number based on the previous element permutated
        for e in res:
            for i in range(len(e) + 1):
                #insert n at the position of i of element e by creating a
                # new element and append it to tmp
                tmp.append(e[:i] + [n] + e[i:])
        # update res
        res = tmp
    return res


def perm2(result, tmp, nums):
    if (len(nums)==0):
        result.append(tmp)
    for i in range(len(nums)):
        perm2(result, tmp+[nums[i]], nums[:i]+nums[i+1:])
    return result

nums = [1, 2, 3]
result = []
tmp = []
perm2(result, tmp, nums)
#print(result)


def perm(nums):
    if len(nums) == 0:
        return [[]]
    result = []
    tmp = perm(nums[:-1])
    for e in tmp:
        for i in range(len(e) + 1):
            #insert the last num of nums
            lst = e[:i] + [nums[-1]] + e[i:]
            result.append(lst)

    return result

#permutation unique:
def permU(nums):
    if len(nums) == 0:
        return [[]]
    result = []
    tmp = permU(nums[:-1])
    for e in tmp:
        for i in range(len(e) + 1):
            #insert the last num of nums
            lst = e[:i] + [nums[-1]] + e[i:]
            result.append(lst)
            #handles duplication
            #!Alert: Don't use 'in' to check dupliction,
            #which just increase the runtime drastically!
            if i < len(e) and e[i] == nums[-1]:
                break
    return result
