'''
【动态规划】
0-1 背包问题 0/1 Knapsack Problem
完全背包问题 Unbounded Knapsack Problem
最小路径和（详细可看 Minimum Path Sum）
编程实现莱文斯坦最短编辑距离
编程实现查找两个字符串的最长公共子序列
编程实现一个数据序列的最长递增子序列





Note:
递归不是动态规划，不能混淆，二者有相通的地方:递归是自顶向下，动归是自底向上。
动归是递归综合备忘录算法以后的反向思维形式。
动态规划算法通常基于一个递推公式及一个或多个初始状态。
当前子问题的解将由上一次子问题的解推出。
使用动态规划来解题只需要多项式时间复杂度， 因此它比回溯法、暴力法等要快许多。
'''

'''
1. 0-1背包问题
假设我们有n件物品，分别编号为0, 2...n-1,每个只有1件。
其中编号为i的物品价值为value[i]，它的重量为weight[i]。
为了简化问题，假定价值和重量都是整数值。
现在，假设我们有一个背包，它能够承载的重量是capacity。
现在，我们希望往包里装这些物品，使得包里装的物品价值最大化，那么我们该如何来选择装的东西呢？

[思路]:
1.首先我们先构建一个表格dp[i][j]，横轴为各个可选择的物品，纵轴为背包的容纳重量（从1到背包的实际最大容纳）。
dp[i][j]表示前i个物品放入容量为j的背包中可以获得的最大价值。
2.状态转移方程为：
dp[i][j] = max{dp[i-1][j], dp[i-1][j-weight[i]] + value[i]}
即，“将前i件物品放入容量为j的背包中”这个子问题，若只考虑第i件物品的策略（放或者不放），
则可转化为一个只牵扯前i-1件物品的问题：
1.若不放当前的第i件物品，则问题转化为“前i-1件物品放入容量为j的背包中”，价值为dp[i-1][j]；
2.若放当前的第i件物品，则问题转化为“先将前i-1件物品放入剩下容量为j-weight[i-1]的背包中，再放入当前第i件物品”，
价值为dp[i-1][j-weight[i]] + value[i]。

[优化空间复杂度]：
以上方法的时间和空间复杂度都为O(n*capacity),其中时间复杂度基本已经不能再优化了，
但空间复杂度却可以优化到O(capacity)。

因为dp[i][j]只和上一层的两个状态有关，所以可以将状态转化为一维数组：
dp[j] = max(dp[j],dp[j-weight[i]] + value[i])；
即要推dp[j],必须保证dp[j]是从dp[j-weight[i]]推出来的。
如果j是顺序递增的，则dp[i][j]是由dp[i][j-weight[i]]推出来的，并非由原来的dp[i-1][j-weight[i]]推导得到的。
E.g.
开始循环前，即背包为空时，dp[0]到最大容量dp[5]的值都为0.
开始循环后，我们需要比较dp[j]（即循环前的值）和dp[j-weight[i]] + value[i]；
因为是顺序循环，j-weight[i] < j, 因此dp[j-weight[i]]会成为前面才刚刚被赋值过得值，
例如当i = 0，
从j=1(至少要让背包容量大于等于物品重量，不然为负没有意义)开始循环，dp[1] = max(dp[1],dp[1-1]+1500) = max(0,1500) = 1500，
（即dp[0][1] = 1500，即背包容量为1时刚好可以放第0件物品，所获得的最大价值为该物品的价值1500.）
然后dp[2] = max(dp[2], dp[2-1] + 1500) = max(0, dp[1] + 1500) = 1500 + 1500 = 3000,
注意！！！
这个时候的dp[j-weight[i]]就成了dp[1],而这个dp[1]是我们刚才才更新的值，是当前的dp[i],并不是由dp[i-1]得到的，
而且此时我们明明只是想把第一个物品（i=0）放进容量为2的背包里，得到的最大价值只是第一个物品的价值，即1500而已，
又怎么可能是3000？所以由此可知0-1背包问题中j不可顺序循环，而是逆序。

https://blog.csdn.net/xiajiawei0206/article/details/19933781

'''
#0-1 背包问题
def knapsack1(weight, value, capacity):
    '''

    >>> knapsack1([], [], 10)
    0
    >>> knapsack1([3], [10], 0)
    0
    >>> knapsack1([4], [15], 4)
    15
    >>> knapsack1([4], [15], 10)
    15
    >>> knapsack1([4], [15], 3)
    0
    >>> weight = [1, 2, 3, 8, 7, 4]
    >>> value = [20, 5, 10, 40, 15, 25]
    >>> capacity = 10
    >>> knapsack1(weight, value, capacity)
    60
    >>> weight = [10, 20, 30]
    >>> value = [60, 100, 120]
    >>> capacity = 50
    >>> knapsack1(weight, value, capacity)
    220

    '''

    #winpty python -m doctest knapsack_problem_0_1.py
    n = len(weight)
    if n < 1 or capacity < 1: return 0
    dp = [0]*(capacity + 1)
    for item in range(n):
        for j in range(capacity, weight[item]-1, -1):
            dp[j] = max(dp[j], dp[j - weight[item]] + value[item])
    return dp[capacity]


'''
拓展：01硬币找零问题（01背包）
给定不同面额的硬币 coins 和总金额 m。每个硬币最多选择一次。
计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

同理，dp[i][j]表示选取当前第i个硬币能凑成总金额为j时最少的硬币个数，
即不拿当前第i个硬币时只用之前的硬币可以凑成j块钱所需最少硬币个数dp[i-1][j]，
与拿当前第i个硬币加上拿之前的硬币凑成j-Coins[i]块钱的硬币数量之和dp[i-1][j-coins[i]] + 1 的最小值。
即写成状态转移方程如下：
dp[i][j] = min(dp[i-1][j], dp[i-1][j-coins[i]] + 1)

同样，我们来优化空间复杂度，依然必须从最大总金额amount开始逆序枚举（枚举到当前硬币i的比值，不然j-coins[i]为负没有意义）。
dp[j] = min(dp[j], dp[j-coins[i]] + 1)
因为这道题是求最少硬币个数，在状态转移方程中用的是min()，所以初始化dp矩阵时给每个值都设为最大值float('inf'),
边界情况为dp[0] = 0, 表示凑出金额为0的最小个数是0个。(但是若本身输入amount为0，则没有硬币组合，返回-1)
最后检查dp[amount], 如果值为'inf', 则说明找不到硬币组合，输出-1，反之才输出相应硬币组合的个数。

[注意]：其实在主循环循环到最后一个硬币时的从amount开始的内循环的第一步就可以结束了，因为我们只需要dp[amount]，
但是接着循环的话可以更新其他amount的硬币组合，毕竟多考虑了一个硬币的情况。

'''
#0-1 硬币找零问题
def coinChange1(coins, amount):
    '''
    >>> coinChange1([2], 1)
    -1
    >>> coins = [2, 3, 5]
    >>> coinChange1(coins, 10)
    3
    >>> coinChange1(coins, 11)
    -1
    >>> coinChange1(coins, 0)
    -1
    >>> coins = [2, 1, 2, 3, 5]
    >>> coinChange1(coins, 10)
    3
    >>> coinChange1(coins, 11)
    4
    >>> coinChange1(coins, 5)
    1
    >>> coinChange1(coins, 6)
    2
    '''

    n = len(coins)
    if n < 1 or amount < 1: return -1
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(amount, coin-1, -1):
            dp[j] = min(dp[j], dp[j-coin] + 1)
    print(dp)
    return dp[amount] if dp[amount] != float('inf') else -1


'''
2.完全背包问题 Unbounded Knapsack Problem

假设我们有n种物品，分别编号为0, 2...n-1,每种物品有多件。
其中编号为i的物品价值为value[i]，它的重量为weight[i]。
为了简化问题，假定价值和重量都是整数值。
现在，假设我们有一个背包，它能够承载的重量是capacity。
现在，我们希望往包里装这些物品，使得包里装的物品价值最大化，那么我们该如何来选择装的东西呢？

[思路]
这个问题非常类似于01背包问题，所不同的是每种物品有无限件。
也就是从每种物品的角度考虑，与它相关的策略已并非取或不取两种，而是有取0件、取1件、取2件……等很多种。
如果仍然按照解01背包时的思路，令DP[i][j]表示前i种物品恰放入一个容量为v的背包的最大权值。
仍然可以按照每种物品不同的策略写出状态转移方程，像这样：
DP[i][j] = max{DP[i-1][j-k*weight[i]] + k*value[i] | 0 <= k*weight[i] <= j}

这跟01背包问题一样有O(n*capacity)个状态需要求解，但求解每个状态的时间已经不是常数了，
求解状态DP[i][j]的时间是O(capacity/weight[i]),(即k的最大值)，
总的复杂度为O(n*capacity*Σ(capacity/weight[i]))，是比较大的。

[代码优化]：
完全背包问题有一个很简单有效的优化，是这样的：
若两件物品i、j满足weight[i] <= weight[j]且value[i] >= value[j]，则将物品j去掉，不用考虑。
即，如果一个物品A是占的地少且价值高，而物品B是占地多，但是价值不怎么高，那么肯定是优先考虑A物品的。
对于随机生成的数据，这个方法往往会大大减少物品的件数，从而加快速度。
然而这个并不能改善最坏情况的复杂度，因为有可能特别设计的数据可以一件物品也去不掉。
这个优化可以简单的O(N^2)地实现，一般都可以承受。

另外，针对背包问题而言，比较不错的一种方法是：
首先将重量大于capacity的物品去掉，然后使用类似计数排序的做法，
计算出重量相同的物品中价值最高的是哪个，可以O(capacity+n)地完成这个优化。

[转化为01背包问题求解]
既然01背包问题是最基本的背包问题，那么我们可以考虑把完全背包问题转化为01背包问题来解。
最简单的想法是，考虑到第i种物品最多选capacity/weight[i]件，
于是可以把第i种物品转化为capacity/weight[i]件费用及价值均不变的物品，然后求解这个01背包问题。
这样完全没有改进基本思路的时间复杂度，但这毕竟给了我们将完全背包问题转化为01背包问题的思路：将一种物品拆成多件物品。

更高效的转化方法是：把第i种物品拆成费用为weight[i]*2^k、价值为value[i]*2^k的若干件物品，
其中k满足weight[i]*2^k <= capacity。这是二进制的思想，因为不管最优策略选几件第i种物品，总可以表示成若干个2^k件物品的和。
这样把每种物品拆成O(log capacity/weight[i])件物品，是一个很大的改进。

但我们有更优的O(n*capacity)的算法。
[O(n*capacity)的算法]
这个算法使用一维数组，先看伪代码：
for i=1..N
    for j=0...capacity
        DP[j]=max{DP[j], DP[j-weight[i]]+value[i]}

我们会发现，这个伪代码与01背包的伪代码只有j的循环次序不同而已。
为什么这样一改就可行呢？
首先想想为什么01中要按照j=capacity...0的逆序来循环。
这是因为要保证第i次循环中的状态DP[i][j]是由状态DP[i-1][j-weight[i]]递推而来。
换句话说，这正是为了保证每件物品只选一次，保证在考虑“选入第i件物品”这件策略时，
依据的是一个绝无已经选入第i件物品的子结果f[i-1][j-weight[i]]。

而现在完全背包的特点恰是每种物品可选无限件，所以在考虑“加选一件第i种物品”这种策略时，
却正需要一个可能已选入第i种物品的子结果f[i][j-weight[i]]，所以就可以并且必须采用j=0...capacity的顺序循环。
这就是这个简单的程序为何成立的道理。
'''
# Unbounded Knapsack Problem
def knapsack2(weight, value, capacity):
    '''

    >>> knapsack2([], [], 10)
    0
    >>> knapsack2([3], [10], 0)
    0
    >>> knapsack2([4], [15], 4)
    15
    >>> knapsack2([4], [15], 10)
    30
    >>> knapsack2([4], [15], 3)
    0
    >>> weight = [1, 50]
    >>> value = [1, 30]
    >>> capacity = 100
    >>> knapsack2(weight, value, capacity)
    100
    >>> weight = [1, 3, 4, 5]
    >>> value = [10, 40, 50, 70]
    >>> capacity = 8
    >>> knapsack2(weight, value, capacity)
    110

    '''
    n = len(weight)
    if n < 1 or capacity < 1: return 0
    dp = [0]*(capacity + 1)
    for i in range(n):
        for j in range(weight[i], capacity+1):
            dp[j] = max(dp[j], dp[j - weight[i]]+value[i])
    #print(dp)
    return dp[capacity]


'''
拓展：完全硬币找零问题（完全背包）
322. Coin Change [Medium]
给定不同面额的硬币 coins 和总金额 amount。每个硬币可以选择无数次。
计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

状态表示:
dp[i][j] 为考虑前 i 种硬币，凑出金额为 j 的最少数目。

状态转移:
对第 i 种硬币，我们可以不拿，或者拿 1...k 个，直到把金额拿爆:
dp[i][j] = min(dp[i-1][j], dp[i-1][j-c]+1, dp[i-1][j-2*c]+2, ..., dp[i-1][j-k*c]+k)

又因为其中包含了大量的冗余计算
例如：dp[i][j-c] = min(dp[i-1][j-c], dp[i-1][j-2*c]+2, ..., dp[i-1][j-k*c]+k)
两者合并得到：dp[i][j] = min(dp[i-1][j], dp[i][j-c]+1)
dp[i][j-c]+1可表示在当前i状态（也许已经拿了好几个i物品了）还要不要继续拿的情况。
又因为dp[i][j]只和上一层一个状态 (dp[i-1][j]) 和这一层的一个状态 (dp[i][j-c]+1) 有关。
可以将状态优化为一维数组:
dp[j] = min(dp[j], dp[j-c]+1)

边界情况:
dp[0] = 0 表示金额为0时，最小硬币凑法为0
其余要初始化为inf，因为此题要求的是恰好金额为amount时的最小硬币数，所以有些状态可能达不到。
'''
def coinChange2(coins, amount):
    '''
    >>> coinChange2([2], 1)
    -1
    >>> coins = [2, 3, 5]
    >>> coinChange2(coins, 10)
    2
    >>> coinChange2(coins, 11)
    3
    >>> coinChange2(coins, 0)
    0
    >>> coinChange2([1, 2, 5], 10)
    2
    >>> coinChange2([1, 2, 5], 11)
    3
    '''

    if len(coins) < 1: return -1
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j-coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

'''
可以看到，此题解法与01问题解法几乎完全相同！！！只是枚举金额时变为由小到大了。
'''

'''
518. Coin Change 2 [Medium]

You are given coins of different denominations and a total amount of money.
Write a function to compute the number of combinations that make up that amount.
You may assume that you have infinite number of each kind of coin.


Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Note:
You can assume that
0 <= amount <= 5000
1 <= coin <= 5000
the number of coins is less than 500
the answer is guaranteed to fit into signed 32-bit integer


[Method 1]: DP:完全背包问题
用dp[i][j]表示用前i个硬币可以凑成j块钱的组合个数。
对于第i个硬币，仍然不用或者用两种情况，以及用的话用几枚硬币。

可得状态转移方程：
dp[i][j] = dp[i-1][j] + dp[i][j-coin]

即用前i-1个硬币凑成j块钱的组合，加上用前i-1个硬币凑成j-coin块钱，然后用第i个硬币凑成剩下的coin块钱的组合个数。

[注意！！！]
对于dp[i-1][j-coin]，要考虑硬币面额刚好为当前要凑的面值的情况，即单独那枚硬币就是1种组合，
所以dp[0][0] = 1, 语义是，不考虑任何硬币，凑出总金额为0的组合数为1。

例如硬币coins = [1, 2, 5], amount = 5 时，不考虑面额为5的最后一枚硬币，只考虑前两枚硬币，已经有：
1+1+1+1+1 = 5
1+1+1+2 = 5
1+2+2 = 5
这3种组合，
那么再考虑最后一枚硬币，即 0 + 5 = 5 这1种组合,
也就是dp[1][5] + dp[2][0] = 3 + dp[2][0], 因此dp[2][0] 必须为1， 也就是dp[i][0]都得为1。

因为每个硬币就可以取无数枚，可以看成完全背包问题，因此dp[i][j]不需要从dp[i-1][j]得到，
而是才更新的dp[i][j]，因为可能已经放了几个i物品了，所以我们用的是顺序循环，从当前coin的面额开始循环到总面值，
毕竟如果面值j < coin的话，减出来为负是没有意义的。
所以优化后的一维状态转移方程为：

dp[j] = dp[j] + dp[j-coin]

Time: O(NV), N为硬币个数，V为需要凑的面值。
Space: O(V)
Runtime: 140 ms, faster than 79.18% of Python3 online submissions for Coin Change 2.
Memory Usage: 13.7 MB, less than 16.67% of Python3 online submissions for Coin Change 2.

'''
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = dp[i] + dp[i-coin]
        return dp[amount]

'''
3.多重背包问题 Multi-Knapsack Problem (MKP)

[题目]：
有N种物品和一个容量为V的背包。第i种物品最多有n[i]件可用，每件的重量是w[i]，价值是v[i]。
求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。

[基本算法]：
这题目和全然背包问题非常类似。
主要的方程仅仅需将全然背包问题的方程稍微一改就可以，由于对于第i种物品有n[i]+1种策略：
取0件，取1件……取n[i]件。
令dp[i][j]表示前i种物品恰放入一个容量为j的背包的最大权值，则有状态转移方程：

dp[i][j] = max{dp[i - 1][j - k*w[i]] + k*v[i] | 0 <= k <= n[i]}。

复杂度是O(V*Σn[i])。

[转化为01背包问题]：
还有一种好想好写的基本方法是转化为01背包求解：
把第i种物品换成n[i]件01背包中的物品，则得到了物品数为Σn[i]的01背包问题，直接求解，复杂度仍然是O(V*Σn[i])。

可是我们期望将它转化为01背包问题之后可以像全然背包一样减少复杂度。
仍然考虑二进制的思想，我们考虑把第i种物品换成若干件物品，
使得原问题中第i种物品可取的每种策略——取0..n[i]件——均能等价于取若干件代换以后的物品。
另外，取超过n[i]件的策略必不能出现。

多重背包转换成 01 背包问题就是多了个初始化，把它的件数C 用二进制分解成若干个件数的集合，
这里面数字可以组合成任意小于等于C的件数，而且不会重复，之所以叫二进制分解，是因为这样分解可以用数字的二进制形式来解释：
    7的二进制 7 = 111 它可以分解成 001 010 100 这三个数可以组合成任意小于等于7的数；
    15 = 1111 可分解成 0001 0010 0100 1000 四个数字
    13 = 1101 则分解为 0001 0010 0100 0110 前三个数字可以组合成7以内任意一个数，
即1、2、4可以组合为1——7内所有的数，加上 0110 = 6，可以组合成任意一个大于6小于等于13的数，比如12，可以让前面贡献6且后面也贡献6就行了。
虽然有重复但总是能把 13 以内所有的数都考虑到了，基于这种思想去把多件物品转换为，多种一件物品，就可用01背包求解了。

即，将第i种物品分成若干件物品，当中每件物品有一个系数，这件物品的费用和价值均是原来的费用和价值乘以这个系数。
使这些系数分别为 1,2,4,...,2^(k-1),n[i]-2^k+1，且k是满足n[i]-2^k+1>0的最大整数。
比如，假设n[i]为13，就将这样的 物品分成系数分别为1,2,4,6的四件物品。

分成的这几件物品的系数和为n[i]，表明不可能取多于n[i]件的第i种物品。
另外这样的方法也能保证对于0..n[i]间的每个整数，均能够用若干个系数的和表示，
这个证明能够分0..2^k-1和2^k..n[i]两段来分别讨论得出，并不难，希望你自己思考尝试一下。

这样就将第i种物品分成了O(log n[i])种物品，将原问题转化为了复杂度为<math>O(V*Σlog n[i])的01背包问题，是非常大的改进。

以下给出O(log amount)时间处理一件多重背包中物品的过程，当中amount表示物品的数量：

procedure MultiplePack(cost,weight,amount)
    if cost*amount>=V
        CompletePack(cost,weight)
        return
    integer k=1
    while k<amount
        ZeroOnePack(k*cost,k*weight)
        amount=amount-k
        k=k*2
    ZeroOnePack(amount*cost,amount*weight)

'''
weight = [3,2,6,7,1,4,9,5]
value = [6,3,5,8,3,1,6,9]
N = [3,5,1,9,3,5,6,8]#每种物品的个数
target = 20 #The capacity of the knapsack
DP = [0] * (target+1)
n = len(weight)

def UnboundedKnapsack(weight,value):
    for j in range(weight,target+1):
        DP[j] = max(DP[j],DP[j-weight] + value)

def OneZeroKnapsack(weight,value):
    for j in range(target, weight-1, -1):
        DP[j] = max(DP[j],DP[j-weight] + value)

def MultiKnapsack(weight,value,count):
        if (weight * count) >= target:#当该种物品的个数乘以体积大于背包容量，视为有无限个即完全背包
            UnboundedKnapsack(weight,value)
            return
        temp_count = 1  #以上情况不满足，转化为以下情况，具体参考《背包九讲》多重背包的时间优化
        while temp_count < count:
            OneZeroKnapsack(temp_count*weight,temp_count*value)
            count = count - temp_count
            temp_count = temp_count * 2  #转化为1，2，4
        OneZeroKnapsack(count*weight,count*value) #9个中剩下两个

for i in range(n):
    MultiKnapsack(weight[i],value[i],N[i])
print(DP[target])


'''
三、多重硬币找零问题（多重背包）
给定不同面额的硬币 coins 和总金额 m。每个硬币选择的次数有限制为s。
计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

[状态表示]
这里和完全硬币问题的的初始状态表态表示很相似。
对于第i种硬币，我们可以不拿，或者拿1...k个，直到拿到个数的限制。

dp[i][j] = min(dp[i-1][j], dp[i-1][j-c]+1, dp[i-1][j-2*c]+2, ..., dp[i-1][j-k*c]+k)

所以在01问题的代码的基础上添加一层枚举硬币个数的循环即可
这里可以使用二进制优化，转化为01背包问题求解。
'''
coins1 = [2, 5, 3]
N1 = [5, 5, 5]
m1 = 12

coins2 = [5, 3, 2]
N2 = [1, 5, 5]
m2 = 13
#用0-1背包求解
def coin_change1(coins, m, N):
    n = len(coins)
    dp = [float('inf')] * (m + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(m, coins[i]-1, -1):
            for k in range(1, N[i] + 1):
                if k*coins[i] <= j:
                    dp[j] = min(dp[j], dp[j - k*coins[i]] + k)
    print(dp)
    return -1 if dp[m] == float('inf') else dp[m]

#print(coin_change1(coins1, m1, N1))
print(coin_change1(coins2, m2, N2))

#多重背包
def coin_change2(coins, m, N):
    n = len(coins)
    dp = [float('inf')] * (m + 1)
    dp[0] = 0
    def unbounded(coin, k):
        for j in range(coin, m+1):
            dp[j] = min(dp[j], dp[j-coin] + k)
    def zeroOne(coin, k):
        for j in range(m, coin-1, -1):
            dp[j] = min(dp[j], dp[j-coin] + k)
    def multi(coin, count):
        if count*coin > m:
            unbounded(coin, 1)
            return
        k = 1
        while k < count:
            zeroOne(k*coin, k)
            count = count - k
            k = k*2
        zeroOne(count*coin, count)
    for i in range(n):
        multi(coins[i], N[i])
    print(dp)
    return -1 if dp[m] == float('inf') else dp[m]

print(coin_change2(coins2, m2, N2))
