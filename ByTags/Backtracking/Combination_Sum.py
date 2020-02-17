'''
39. Combination Sum [Medium]

Given a set of candidate numbers (candidates) (without duplicates) and
a target number (target), find all unique combinations in candidates
where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

[Method 1]: Backtracking
Runtime: 96 ms, faster than 41.37% of Python3 online submissions for Combination Sum.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Combination Sum.
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, tmp = [], []
        candidates.sort()
        def backtrack(res, tmp, pos, k):
            if k == 0:
                res.append(tmp[:])
                return
            if k < 0:
                return
            for i in range(pos, len(candidates)):
                tmp.append(candidates[i])
                backtrack(res, tmp, i, k-candidates[i])
                tmp.pop()
        backtrack(res, tmp, 0, target)
        return res

# Or:
class Solution(object):
    def combinationSum(self, candidates, target):
        def dfs(remain, combo, index):
            if remain == 0:
                result.append(combo)
                return
            for i in range(index, len(candy)):
                if candy[i] > remain:
                    # exceeded the sum with candidate[i]
                    break #the for loop

                dfs(remain - candy[i], combo + [candy[i]], i)

        candy = sorted(candidates)
        result = []
        dfs(target, [], 0)
        return result

'''
[Method 2]: DP（完全/多重背包）
根据动态规划的基本思路，有：
dp[i][j]: 用前i个数凑齐j的方案，
状态转移方程：dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]],
即不用当前第i个数凑齐j的情况加上用当前数凑齐j的情况（也就是不用当前数i凑齐j-nums[i]的情况）
因为是完全背包，dp[i][j]不需要从dp[i-1][j]得到，所以可以优化为：
dp[j] = dp[j] + dp[j-nums[i]]。
但这种情况是用来求能凑齐的方案个数的，也就是dp[j]是一个整数，如题目518. Coin Change 2。
而本题求的是所有的方案的集合，也就是说从之前的一维数组，此题要用到三维数组（dp存的是集合的集合），
我们只能将第三维的具体某一方案的集合写出动态规划的转移方程式：
tmp = [[num] + comb for comb in dp[j-num]]
tmp代表当前用num可能凑齐的组合方式的list容器（因为凑不齐的话（如果dp[j-num]为[]）则tmp就是个空容器，加减空容器并不影响原list），
也就是说剩下的j-num刚好是已经凑齐了的（有可能无num也可能有num,毕竟是完全背包）
然后dp[j] += tmp即可。
另外要注意初始状态dp[0], 即target为0的情况是有一解的（空解）：
dp[0] = [[]]
因为当target凑不齐的时候都返回[[]]。
[Time]: O(n * target * c), n为nums长度，c为dp[j-num]的长度，肯定有限，所以用常数c表示；
[Space]: O(n * target * c )
Runtime: 56 ms, faster than 76.94% of Python3 online submissions for Combination Sum.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Combination Sum.
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> int:
        # 保存方案，使用三维数组
        # 第一维： dp：存储了和为从0到target的所有组合方案(list)的list
        # 第二维： dp[j]: 表示和为j的方案的list
        # 第三维 dp[j][i]:表示和为j的第i个方案的list
        # 初始化 eg: [[[]], [], [], [], [], []]， 保证和为0有一种方案 [], 完全背包需要恰好装满的时候，dp[0] 必须初始化为0
        dp = [[[]]] + [[] for i in range(target)]

        for num in nums:  # 对于每个数
            for j in range(num, target + 1):  # 完全背包，从小到大
                # 当前组合方案含num的时候，即剩下的j-num都已经组合好了，如果没有则tmp为[]
                tmp = [[num] + comb for comb in dp[j - num]]
                dp[j] += tmp  # 把新组合方案添加到原来和为j的list里， 注意，加上空集则dp[j]不变
        return dp[target]
