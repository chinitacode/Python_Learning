
# Use recursion:
def subset(nums):
    if len(nums) == 0:
        return [[]]
    res = subset(nums[:-1])
    return res + [e + [nums[-1]] for e in res]

#Use only iteration:
def subsets2(nums):
    res = [[]]
    for num in nums: 
        res += [ i + [num] for i in res]
    return res


def subsets(nums):
    result = [[]]
    for num in nums:
        for e in result[:]:
            x = e[:]
            x.append(num)
            result.append(x)
    return result

#Use backtracking
def subsets_bk(nums):
    lst,result = [],[]
    def helper(result,lst,nums,pos):
        result.append(lst[:])
        for i in range(pos,len(nums)):
            lst.append(nums[i])
            helper(result,lst,nums,i+1)
            lst.pop()
    helper(result,lst,nums,0)
    return result
