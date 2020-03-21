'''
322. Coin Change [Medium]
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.


Good to note that the name of the problem is the Change-Making problem
(https://en.wikipedia.org/wiki/Change-making_problem), the most common variation of Coin Change problem.
Change-Making problem is a variation of the Knapsack problem,
more precisely - the Unbounded Knapsack problem, also known as the Complete Knapsack problem.
For me the problem name was a bit misleading (maybe done intentionally),
as Coin Change problem is slightly different - finding the ways of making a certain change.
***More information about Knapsack problems in the book by Martello/Toth ->
http://www.or.deis.unibo.it/kp/KnapsackProblems.pdf


对待DP问题，首先我们要找到某个状态的最优解，然后在它的帮助下，找到下一个状态的最优解。
“状态”代表什么，及如何找到它?

“状态”用来描述该问题的子问题的解。
如果我们有面值为 1 元、3 元和 5 元的硬币若干枚，如何用最少的硬币凑够 11 元？
(表面上这道题可以用贪心算法，但贪心算法无法保证可以求出解，比如 1 元换成 2 元的时候)

首先我们思考一个问题，如何用最少的硬币凑够 i 元(i<11)？为什么要这么问呢？
两个原因：1.当我们遇到一个大问题时，总是习惯把问题的规模变小，这样便于分析讨论。
         2.这个规模变小后的问题和原来的问题是同质的，除了规模变小， 本质上它还是同一个问题(规模变小后的问题其实是原问题的子问题)。

好了，让我们从最小的 i 开始吧。当 i=0，即我们需要多少个硬币来凑够 0 元。
由于 1，3，5 都大于 0，即没有比 0 小的币值，因此凑够 0 元我们最少需要 0 个硬币。
(这个分析很傻是不是？别着急，这个思路有利于我们理清动态规划究竟在做些什么。)
这时候我们发现用一个标记来表示这句“凑够 0 元我们最少需要 0 个硬币。”会比较方便。
那么， 我们用 d(i)=j 来表示凑够 i 元最少需要 j 个硬币。于是我们已经得到了 d(0)=0， 表示凑够 0 元最小需要 0 个硬币。
当 i=1 时，只有面值为 1 元的硬币可用， 因此我们拿起一个面值为 1 的硬币，接下来只需要凑够 0 元即可，而这个是已经知道答案的， 即 d(0)=0。
所以，d(1) = d(1-1) + 1 = d(0) + 1 = 0+1 = 1。
当 i=2 时， 仍然只有面值为 1 的硬币可用，于是我拿起一个面值为 1 的硬币， 接下来只需要再凑够 2-1=1 元即可(记得要用最小的硬币数量)。
所以 d(2)=d(2-1)+1=d(1)+1=1+1=2。一直到这里，你都可能会觉得，好无聊， 感觉像做小学生的题目似的。因为我们一直都只能操作面值为 1 的硬币！
耐心点， 让我们看看 i=3 时的情况：
当 i=3 时，我们能用的硬币就有两种了：1 元的和 3 元的( 5 元的仍然没用，因为你需要凑的数目是 3 元！)。
既然能用的硬币有两种，我就有两种方案：
1）如果我拿了一个 1 元的硬币，我的目标就变为了：
凑够 3-1=2 元需要的最少硬币数量。
即 d(3)=d(3-1)+1=d(2)+1=2+1=3。 这个方案说的是，我拿 3 个 1 元的硬币；
2）我拿起一个 3 元的硬币， 我的目标就变成：凑够 3-3=0 元需要的最少硬币数量。
即 d(3)=d(3-3)+1=d(0)+1=0+1=1. 这个方案说的是，我拿 1 个 3 元的硬币。
因为我们可是要用最少的硬币数量来凑够 3 元的。所以， 选择 d(3)=1，怎么来的呢：
d(3)=min{d(3-1)+1, d(3-3)+1}。

从以上的文字中， 我们要抽象出动态规划里非常重要的两个概念：状态和状态转移方程。

上文中 d(i)表示凑够 i 元需要的最少硬币数量，我们将它定义为该问题的”状态”。
这个状态是怎么找出来的呢？根据子问题定义状态。你找到子问题，状态也就浮出水面了。
最终我们要求解的问题，可以用这个状态来表示：d(11)，即凑够 11 元最少需要多少个硬币。

那状态转移方程是什么呢？既然我们用 d(i)表示状态，那么状态转移方程自然包含 d(i)，
上文中包含状态 d(i)的方程是：d(3)=min{d(3-1)+1, d(3-3)+1}。
它就是状态转移方程，描述状态之间是如何转移的。当然，我们要对它抽象一下，
d(i)=min{ d(i-coin)+1 }，其中 i-coin >=0，coin表示硬币的面值;

针对以上情况，因为有1元的硬币，所以最终都能得到零钱组合。
但是如果没有1元，假设我们只有2元，那就不一定有解了，如当面临2元硬币和3块钱时。

根据当前题目，我们可以设置dp[0] = 0作为我们的base case,因为不可能有0元的银币。
然后有多少元钱，就设置多长的dp数列，并且每个值都设置为一个最大值，如float('inf')，
因为我们不确定是否能够找零，如果没有解则它的值就肯定大于当前的币值。
然后从1元开始循环到给定的amount元，如果有比当前面值小的硬币，我们就可以试着看能不能找零：
dp[i] = min(dp[i-coin] + 1, dp[i])

循环完后，如果dp[-1]（或者dp[amount]）是小于amount的，就说明有解，直接返回就是；
反之无解，则返回-1。

[Time]: O(mn), m为银币个数，n为amount大小
[Space]: O(n),n为amount大小
Runtime: 1264 ms, faster than 72.60% of Python3 online submissions for Coin Change.
Memory Usage: 13.1 MB, less than 94.44% of Python3 online submissions for Coin Change.
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1 # 但如果amount为0返回0
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j] = min(dp[j],dp[j-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1




'''
[Method 2]:DFS
Runtime: 152 ms, faster than 99.29% of Python3 online submissions for Coin Change.
Memory Usage: 13.5 MB, less than 30.56% of Python3 online submissions for Coin Change.
'''
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        self.ans = math.inf
        count = 0
        def dfs(coins, amount, s, count):
            coin = coins[s]
            if s == 0:
                if amount % coin == 0:
                    self.ans = min(self.ans, count + amount // coin)
                    return
                return
            for k in range(amount // coin, -1, -1):
                if k + count >= self.ans:
                    break
                dfs(coins, amount - k * coin, s - 1, count + k)
        dfs(coins, amount, len(coins) - 1, count)
        return  -1 if self.ans == math.inf else self.ans

# Or:
import functools
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort(reverse = True)
        n = len(coins)
        self.res = float('inf')

        @functools.lru_cache(None)
        def dfs(index, remain, count):
            if remain == 0:
                self.res= min(self.res, count)
            for i in range(index, n):
                if coins[i]<=remain < coins[i] * (self.res - count): #When there is no hope to reduce total count, stop the dfs
                    dfs(i, remain - coins[i], count + 1)


        dfs(0, amount, 0)

        return self.res if self.res < float('inf') else -1



'''
[Method 3]: Fast python branch and bound solution


'''
def coinChange(self, coins, amount):
    if len(coins) == 0:
        return -1
    if amount == 0:
        return 0

    # try biggest coins first
    sortedCoins = sorted(coins, reverse=True)

    # upper bound on number of coins (+1 to represent the impossible case)
    upperBound = (amount + sortedCoins[-1] - 1) / sortedCoins[-1] + 1

    self.bestNCoins = upperBound

    self.branchAndBoundSearch(sortedCoins, amount, 0)

    if self.bestNCoins == upperBound:
        return -1
    else:
        return self.bestNCoins

def branchAndBoundSearch(self, sortedCoins, amount, nCoins):
    # lower bound on number of coins, achieved using the biggest coin
    lowerBound = nCoins + (amount + sortedCoins[0] - 1) / sortedCoins[0]

    if lowerBound > self.bestNCoins:
        return

    if len(sortedCoins) == 0:
        return

    # if amount matches the biggest coin, that is the solution
    if amount == sortedCoins[0] and nCoins + 1 < self.bestNCoins:
        self.bestNCoins = nCoins + 1
        return

    # try use the biggest coin
    if amount > sortedCoins[0]:
        self.branchAndBoundSearch(sortedCoins, amount - sortedCoins[0], nCoins + 1)

    # else try not to use the biggest coin
    if len(sortedCoins) > 1:
        self.branchAndBoundSearch(sortedCoins[1:], amount, nCoins)
