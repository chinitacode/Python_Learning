'''
60. Permutation Sequence [Medium]
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"


[Method 1]: Backtracking (TLE)
如遇到：
n = 9
k = 206490
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        res, tmp = [], []
        def backtrack(res, tmp, nums, k):
            if not k: return
            if not nums:
                res.append(tmp[:])
                k -= 1
                return
            for i in range(len(nums)):
                tmp.append(nums[i])
                backtrack(res, tmp, nums[:i] + nums[i+1:], k)
                tmp.pop()
        backtrack(res, tmp, nums, k)
        return ''.join(str(num) for num in res[k-1])

# or (TLE but better):
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        len_res = math.factorial(n)
        k = (k % len_res) if k > len_res else k
        res, tmp = [], []
        def backtrack(res, tmp, nums, k):
            if not k: return
            if not nums:
                res.append(tmp[:])
                k -= 1
                return
            for i in range(len(nums)):
                tmp.append(nums[i])
                backtrack(res, tmp, nums[:i] + nums[i+1:], k)
                tmp.pop()
        backtrack(res, tmp, nums, k)
        return ''.join(str(num) for num in res[k-1])

'''
[Method 2]: 深度优先遍历 + 剪枝
1、我们知道所求排列一定在叶子结点处得到。事实上，进入每一个分支的时候，
我们都可以通过递归的层数，直接计算这一分支可以得到的叶子结点的个数；

这是因为：进入一个分支的时候，我们可以根据已经选定的数的个数，
进而确定还未选定的数的个数，然后计算阶乘，就知道这一个分支的叶子结点有多少个。

2、如果 kk 大于这一个分支将要产生的叶子结点数，直接跳过这个分支，这个操作叫“剪枝”；

3、如果 kk 小于等于这一个分支将要产生的叶子结点数，
那说明所求的全排列一定在这一个分支将要产生的叶子结点里，需要递归求解；

4、计算阶乘的时候，你可以使用循环计算，特别注意：0!=10!=1，
它表示了没有数可选的时候，即表示到达叶子结点了，排列数只剩下 11 个；

[Time]: O(N**2) for循环每次最多循环N遍（k=n! 就是这种情况），
最少循环N-depth（depth为递归的深度，k=1就是这种情况），所以最坏时间复杂度为：N+N+....+N=O(N的平方)，
最好时间复杂度为：N+N-1+...+1=N*(N+1)/2=O(N的平方），因此，时间复杂度应该是O(N的平方）

[Space]: O(N)
Runtime: 28 ms, faster than 75.08% of Python3 online submissions for Permutation Sequence.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Permutation Sequence.
'''
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0:
            return ""

        used = [False for _ in range(n + 1)]
        path = []
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i

        k = (k % factorial[n]) if k > factorial[n] else k

        def dfs(n, k, index, path):
            if index == n:
                return
            cnt = factorial[n - 1 - index]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                path.append(i)
                used[i] = True
                dfs(n, k, index + 1, path)

        dfs(n, k, 0, path)
        return ''.join([str(num) for num in path])
