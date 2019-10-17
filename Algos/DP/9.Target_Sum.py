'''
494. Target Sum [Medium]
You are given a list of non-negative integers,
a1, a2, ..., an, and a target, S.
Now you have 2 symbols + and -.
For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5

Explanation:
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.

[Method 1]: DP
该问题可以转换为 416.Partition Equal Subset Sum 问题，从而使用 0-1 背包的方法来求解。
可以将这组数看成两部分，P 和 N，其中 P 使用正号，N 使用负号，有以下推导：
                  sum(P) - sum(N) = target
sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                       2 * sum(P) = target + sum(nums)
因此只要找到一个子集，令它们都取正号，并且和等于 (target + sum(nums))//2，就证明存在解。

[Time]: O(n + n*cap) = O(n*cap), N为nums的元素个数，cap为(S+Sum) // 2；
[Space]: O(cap+1)
Runtime: 76 ms, faster than 98.69% of Python3 online submissions for Target Sum.
Memory Usage: 13.8 MB, less than 58.33% of Python3 online submissions for Target Sum.
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        Sum = sum(nums)
        if S > Sum or (S+Sum) % 2: return 0
        cap = (S+Sum) // 2
        dp = [0] * (cap+1)
        dp[0] = 1
        for num in nums:
            for j in range(cap, num-1, -1):
                dp[j] = dp[j] + dp[j-num]
        return dp[cap]


'''
[Metho 2]: DFS
利用dfs深度优先搜索
设置一个哈希表（字典），键是一个元祖，元祖第一位是目前的和，第二位是目前的位数。
值是这个元祖推导到最后能有多少个解。
例如d[(4,5)] = 1 代表已经读了前4位的时，正好有一个解符合条件（那么在这个例子中符合条件的S就是5），
然后倒导d([3,5]) = 2 ......(在这种情况下，第4位是0，总共就4位)
初始化节点为(0,0)，代表已经读了0位，现在和为0。
开始深度优先搜索，i为0时表示还未开始读，当i比len(nums)小，说明可以深入。
为了避免重复运算，要看当前节点是否在d里已经出现过。
每次深入的结果，就是d[(i, cur)] = dfs(cur + nums[i], i + 1, d) + dfs(cur - nums[i], i + 1, d)。
意思就是当前节点推导到最后有多少个可能性呢？
这个节点再读取一位，要么是加上这一位，要么是减掉这一位，所以这个节点的可能性就是对加上下一位的可能性与减掉下一位的可能性之和。
当深入到最后一位时，再深入就超了位数限制了，此时可以直接判断这个节点的和（即元祖的第二位）是否等于需要的S。
The get() method is used to avoid such situations.
This method returns the value for the given key, if present in the dictionary.
If not, then it will return None (if get() is used with only one argument).
d.get((i, cur), int(cur == S),若满足cur == S则返回1，否则返回0。
因为dfs可能遍历到重复节点，所以return一行写作d.get((i, cur), int(cur == S))。
如果是重复节点直接返回字典里对应值就完事儿

[Time]: O(2^n + 2^(n-1) + ... + 2^0) = O(2^n). Size of recursion tree will be 2^n, n refers to the size of nums array.
[Space]:O(n). The depth of the recursion tree can go upto n.
Runtime: 560 ms, faster than 15.16% of Python3 online submissions for Target Sum.
Memory Usage: 14.6 MB, less than 50.00% of Python3 online submissions for Target Sum.
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        d = {}
        def dfs(cur, i, d):
            if i < len(nums) and (cur, i) not in d: # 搜索周围节点
                d[(cur, i)] = dfs(cur + nums[i], i + 1, d) + dfs(cur - nums[i],i + 1, d)
            return d.get((cur, i), int(cur == S))
        return dfs(0, 0, d)

'''
#or:
dfs遍历所有可能结果，以当前位置 i 和当前总和 cur 为根节点，以下一位数字的加减为邻域扩散搜索
利用 d 构造记忆，以便剪枝（搜索过程中遇到相同位置和相同cur值时返回值应该相同）
dfs中 d 参数传的是引用，所以只有第一次会采用默认值 {}
'''
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        def dfs(cur, i, d = {}):
            if i < len(nums) and (i, cur) not in d: # 搜索周围节点
                d[(i, cur)] = dfs(cur + nums[i], i + 1) + dfs(cur - nums[i], i + 1)
            return d.get((i, cur), int(cur == S))

        return dfs(0, 0)
