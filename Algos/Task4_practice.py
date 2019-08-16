'''

1. Two Sum (Easy)

Reverse String （反转字符串）

Reverse Words in a String（翻转字符串里的单词）

String to Integer (atoi)（字符串转换整数 (atoi)）[作为可选]

'''
#1. Two Sum (Easy)
# using hash O(N)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        wanted_nums = {}
        for i in range(len(nums)):
            # check if the left value is in wanted_nums(if num is the left value)
            if nums[i] in wanted_nums:
                # return the index of the first value and the current index
                return [wanted_nums[nums[i]], i]
            else:
                # Save each left value of tatget - num as key in wanted_nums
                # before return, including negative values
                wanted_nums[target - nums[i]] = i
        return [-1, -1]


# Or:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
        return [-1, -1]
