'''
1346. 检查整数及其两倍数是否存在 [Easy]
给你一个整数数组 arr，请你检查是否存在两个整数 N 和 M，满足 N 是 M 的两倍（即，N = 2 * M）。
更正式地，检查是否存在两个下标 i 和 j 满足：

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

示例 1：

输入：arr = [10,2,5,3]
输出：true
解释：N = 10 是 M = 5 的两倍，即 10 = 2 * 5 。
示例 2：

输入：arr = [7,1,14,11]
输出：true
解释：N = 14 是 M = 7 的两倍，即 14 = 2 * 7 。
示例 3：

输入：arr = [3,1,7,11]
输出：false
解释：在该情况下不存在 N 和 M 满足 N = 2 * M 。
 

提示：
2 <= arr.length <= 500
-10^3 <= arr[i] <= 10^3

注意：
存在cases如[-20, 8, -10, 0, 2, 3], [0,0]等为True的情况。


[Method 1]: Brute force
除此之外其它都是拿空间换时间
[Time]: O(n**2)
[Space]: O(1)
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if len(arr) <= 1: return False
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if (arr[i] == 2*arr[j]) or (arr[j] == 2*arr[i]):
                    return True
        return False

'''
[Method 2]: Set
[Time]: O(n + n) == O(n)
[Space]: O(n)
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for num in arr:
            if ((num % 2 == 0 and num // 2 in s) or (num * 2 in s)): return True
            s.add(num)
        return False

'''
[Method 2]: Use Dictionary (最快)
[Time]: O(n)
[Space]: O(n)
Runtime: 48 ms, faster than 86.76% of Python3 online submissions for Check If N and Its Double Exist.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Check If N and Its Double Exist.
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doubles = {} # a dict used as a set，并避免重复
        zeros = 0 # Zero Count
        # 第一次遍历，记录0的个数并把每个非零数字的两倍数加入double这个dictionary
        for num in arr:
            if not num:
                zeros += 1
            else:
                doubles[2 * num] = 0
        if zeros >= 2: return True # 0 = 2*0, 所以可以直接判断需不需要再接着遍历来判断非零的数字
        for num in arr:
            if num in doubles:
                return True
        return False

'''
[Method 4]: 用collections.counter
虽然 0 的 2 倍仍然是 0 本身，但是只有 1 个 0 仍是不行的。所以要统计 0 的数量。
使用 collections.Counter 方便的统计数组中各个元素的数量。
[Time]: O(n + n) == O(n)
[Space]: O(n)
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        import collections
        s = collections.Counter(arr)
        for n in s:
            if n == 0:
                if s[n] > 1: return True
            elif n<<1 in s: # O(1)
                return True
        return False
