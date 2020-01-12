# permutation of size K
def permuteK(result,nums,k):
    if k == 0:
        print(result)
    for i in range(len(nums)):
        permuteK(result + str(nums[i]), nums[:i] + nums[i+1:], k - 1)


def permk(result, tmp, nums, k):
    '''
    >>> nums = [1, 2, 3, 4]
    >>> result = []
    >>> permk(result, '', nums, 2)
    >>> result
    ['12', '13', '14', '21', '23', '24', '31', '32', '34', '41', '42', '43']
    >>> nums = [1, 2, 3, 4]
    >>> result = []
    >>> permk(result, '', nums, 3)
    >>> result
    ['123', '124', '132', '134', '142', '143', '213', '214', '231', '234', '241', '243', '312', '314', '321', '324', '341', '342', '412', '413', '421', '423', '431', '432']
    '''
    
    if k == 0:
        result.append(tmp)
    for i in range(len(nums)):
        permk(result, tmp + str(nums[i]), nums[:i] + nums[i+1:], k - 1)

# permutation of size K using backtracking:
def find_perm(li, k):
    result = []
    tmp = []
    def helper(result, tmp, li, k):
        if k == 0:
            result.append(tmp[:])
            return
        for i in range(len(li)):
            tmp.append(li[i])
            helper(result, tmp, li[:i] + li[i+1:], k-1)
            tmp.pop()
    helper(result, tmp, li, k)
    return result

#全排列
def perm(li):
    result = []
    tmp = []
    def helper(result, tmp, li):
        if len(li) == 0:
            result.append(tmp[:])
        for i in range(len(li)):
            tmp.append(li[i])
            helper(result, tmp, li[:i] + li[i+1:])
            tmp.pop()
    helper(result, tmp, li)
    return result


#将1~9放入9个[]中，使得[][][]+[][][]=[][][]等式成立
def perm_of_sum():
    nums = list(range(1, 10))
    result, tmp = [], []
    def helper(result, tmp, nums):
        if len(tmp) == 9:
            if 100 * (tmp[0] + tmp[3]) + 10 * (tmp[1] + tmp[4]) + tmp[2] + tmp[5] == 100 * tmp[6] + 10 * tmp[7] + tmp[8]:
                result.append(tmp[:])
                return
            else:
                return
        for i in range(len(nums)):
            tmp.append(nums[i])
            helper(result, tmp, nums[:i] + nums[i+1:])
            tmp.pop()
    helper(result, tmp, nums, )
    return result
            
