'''
46. Permutations [Medium]
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

[Method 1]: Recursion 1: 先全排列好前面的数字，再把最后一个数字加进去全排列。
全排列公式： P(N,k)= N!/(N−k)! =N(N−1)...(N−k+1)
Time: O(n!), 实际上会比n!慢，因为会从进行只有1个元素的全排列，到2个元素的全排列再到最后N个元素的全排列，
即 1! + 2! + 3! + ... + N! ==> N < O(N!) < N * N!
Space: O(n!) 因为有n个全排列需要储存。
Runtime: 52 ms, faster than 37.03% of Python3 online submissions for Permutations.
Memory Usage: 13.9 MB, less than 5.36% of Python3 online submissions for Permutations.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2: return [nums]
        return self.perms(nums, 0, len(nums)-1)
    def perms(self, nums, start, end):
        if start == end:
            return [[nums[0]]]
        prev = self.perms(nums, start, end-1)
        num = nums[end]
        length = end - start
        ans = []
        for perm in prev:
            for i in range(length+1):
                tmp = perm[:i] + [num] + perm[i:]
                ans.append(tmp[:])
        return ans

'''
#或者使用切片(最好不，因为slicing a list of size k takes O(k))：
Time: N < O(N!) < N * N!
Space: O(n!)
Runtime: 48 ms, faster than 71.58% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 5.36% of Python3 online submissions for Permutations.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        result = []
        tmp = self.permute(nums[:-1])
        for e in tmp:
            for i in range(len(e) + 1):
                #insert the last num of nums
                lst = e[:i] + [nums[-1]] + e[i:]
                result.append(lst)
        return result

'''
[Method 2]: Recursion 2: 从第一个数字开始，每个数字加上全排列好了的剩下的数字的所有组合。
Time: O(n!); Space: O(n!)
Runtime: 48 ms, faster than 71.58% of Python3 online submissions for Permutations.
Memory Usage: 13.8 MB, less than 5.36% of Python3 online submissions for Permutations.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        if length < 2: return [nums]
        ans = []
        for i in range(length):
            num = nums[i]
            rest = nums[:i] + nums[i+1:]
            for perm in self.permute(rest):
                ans.append([num] + perm )
        return ans

'''
#code2:全局变量result和局部变量tmp
Runtime: 48 ms, faster than 71.58% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 5.36% of Python3 online submissions for Permutations.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.perm([], [], nums)
    def perm(self, result, tmp, nums):
        if len(nums) == 0:
            result.append(tmp)
        for i in range(len(nums)):
            self.perm(result, tmp+[nums[i]], nums[:i]+nums[i+1:])
        return result


'''
[Method 3]: Backtracking
Time: O(n!); Space: O(n!)
Runtime: 48 ms, faster than 71.58% of Python3 online submissions for Permutations.
Memory Usage: 14 MB, less than 5.36% of Python3 online submissions for Permutations.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        tmp = []
        def backtrack(result, tmp, rest):
            if len(rest) == 0:
                result.append(tmp[:])
            for i in range(len(rest)):
                tmp.append(rest[i])
                backtrack(result, tmp, rest[:i] + rest[i+1:])
                tmp.pop()
        backtrack(result, tmp, nums)
        return result




'''
[Method 4]: Iteration
Time: O(n*n!), 3个for循环，实际上是n*(1*1 + 1*2 + 2*3 +...+n!)
Space: O(n!)
Runtime: 48 ms, faster than 71.58% of Python3 online submissions for Permutations.
Memory Usage: 13.8 MB, less than 5.36% of Python3 online submissions for Permutations.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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
