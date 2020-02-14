'''
78. Subsets [Medium]
[Method 1]: recursion
[Time]: O(2^n)
'''
def subset(nums):
    '''
    Runtime: 16 ms, faster than 90.16% of Python online submissions for Subsets.
    Memory Usage: 12.1 MB, less than 22.03% of Python online submissions for Subsets.
    '''
    if len(nums) == 0:
        return [[]]
    res = subset(nums[:-1])
    return res + [e + [nums[-1]] for e in res]

#Use only iteration:
def subsets2(nums):
    res = [[]]
    for num in nums:
        res += [e + [num] for e in res]
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
# O(2^n)
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
