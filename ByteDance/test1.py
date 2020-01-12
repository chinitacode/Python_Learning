'''
1.万万没想到之聪明的编辑
时间限制：1秒

空间限制：32768K

我叫王大锤，是一家出版社的编辑。我负责校对投稿来的英文稿件，这份工作非常烦人，因为每天都要去修正无数的拼写错误。但是，优秀的人总能在平凡的工作中发现真理。我发现一个发现拼写错误的捷径：

1. 三个同样的字母连在一起，一定是拼写错误，去掉一个的就好啦：比如 helllo -> hello
2. 两对一样的字母（AABB型）连在一起，一定是拼写错误，去掉第二对的一个字母就好啦：比如 helloo -> hello
3. 上面的规则优先“从左到右”匹配，即如果是AABBCC，虽然AABB和BBCC都是错误拼写，应该优先考虑修复AABB，结果为AABCC

我特喵是个天才！我在蓝翔学过挖掘机和程序设计，按照这个原理写了一个自动校对器，工作效率从此起飞。用不了多久，我就会出任CEO，当上董事长，迎娶白富美，走上人生巅峰，想想都有点小激动呢！
……
万万没想到，我被开除了，临走时老板对我说： “做人做事要兢兢业业、勤勤恳恳、本本分分，人要是行，干一行行一行。一行行行行行；要是不行，干一行不行一行，一行不行行行不行。” 我现在整个人红红火火恍恍惚惚的……

请听题：请实现大锤的自动校对程序

输入描述:
第一行包括一个数字N，表示本次用例包括多少个待校验的字符串。
后面跟随N行，每行为一个待校验的字符串。

输出描述:
N行，每行包括一个被修复后的字符串。

输入例子1:
2
helloo
wooooooow

输出例子1:
hello
woow
'''
import sys
N = int(sys.stdin.readline().strip())
for eg in range(N):
    string = sys.stdin.readline().strip()
    res = ''
    for s in string:
        if (len(res)>1 and s == res[-1] and s == res[-2]) or (len(res)>2 and s == res[-1] and res[-3] == res[-2]): continue
        res += s
    print(res)

#Or:
N = int(input())
for eg in range(N):
    string = input()
    res = ''
    for s in string:
        if (len(res)>1 and s == res[-1] and s == res[-2]) or (len(res)>2 and s == res[-1] and res[-3] == res[-2]): continue
        res += s
    print(res)


'''
2.万万没想到之抓捕孔连顺
时间限制：1秒
空间限制：131072K

我叫王大锤，是一名特工。我刚刚接到任务：在字节跳动大街进行埋伏，抓捕恐怖分子孔连顺。
和我一起行动的还有另外两名特工，我提议
1. 我们在字节跳动大街的N个建筑中选定3个埋伏地点。
2. 为了相互照应，我们决定相距最远的两名特工间的距离不超过D。
我特喵是个天才! 经过精密的计算，我们从X种可行的埋伏方案中选择了一种。
这个方案万无一失，颤抖吧，孔连顺！
……
万万没想到，计划还是失败了，孔连顺化妆成小龙女，混在cosplay的队伍中逃出了字节跳动大街。
只怪他的伪装太成功了，就是杨过本人来了也发现不了的！

请听题：给定N（可选作为埋伏点的建筑物数）、D（相距最远的两名特工间的距离的最大值）以及可选建筑的坐标，
计算在这次行动中，大锤的小队有多少种埋伏选择。
注意：
1. 两个特工不能埋伏在同一地点
2. 三个特工是等价的：即同样的位置组合(A, B, C) 只算一种埋伏方法，不能因“特工之间互换位置”而重复使用


输入描述:
第一行包含空格分隔的两个数字 N和D(1 ≤ N ≤ 1000000; 1 ≤ D ≤ 1000000)

第二行包含N个建筑物的的位置，每个位置用一个整数（取值区间为[0, 1000000]）表示，从小到大排列（将字节跳动大街看做一条数轴）

输出描述:
一个数字，表示不同埋伏方案的数量。结果可能溢出，请对 99997867 取模

输入例子1:
4 3
1 2 3 4

输出例子1:
4

例子说明1:
可选方案 (1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)

输入例子2:
5 19
1 10 20 30 50

输出例子2:
1

例子说明2:
可选方案 (1, 10, 20)

[Analysis]:
这道题目使用双指针滑窗，加组合数算法，每次给定一个起点i，j向后滑倒临界位置。
此时的个数可以用组合数C(j-i,2) 算出，即后两个人可选范围内选2个人，有多少种情况。加起来即可。
这题目数据量比较大，写起来调试比较困难。
'''
n, D = map(int, (input().split()))
nums = list(map(int, (input().split())))
res, i, j = 0, 0, 2
while i < n-2:
    while j < n and nums[j] - nums[i] <= D:
        j += 1 #j会多加1
    if j - i - 1 >= 2:
        choice = j-i-1
        res += choice*(choice-1)//2
    i += 1
res %= 99997867
print(res)


'''
#TLE
'''
n, D = map(int, (input().split()))
nums = list(map(int, (input().split())))
if nums[-1] - nums[0] <= D:
    print(N*(N-1)*(N-2)//6)
def perm(nums, k):
    res = []
    tmp = []
    def helper(res, tmp, pos, k):
        if k == 0:
            res.append(tmp[:])
            return
        for i in range(pos, len(nums)):
            if not tmp or nums[i] - tmp[0] <= D:
                tmp.append(nums[i])
                helper(res, tmp, i+1, k-1)
                tmp.pop()
    helper(res, tmp, 0, k)
    return len(res)%99997867
print(perm(nums,3))

'''
#test
N, D = 5, 19
nums = [1,10,20,30,50]
if nums[-1] - nums[0] <= D:
    print(N*(N-1)*(N-2)//6)
def perm(nums, k):
    res = []
    tmp = []
    def helper(res, tmp, pos, k):
        if k == 0:
            res.append(tmp[:])
            return
        for i in range(pos, len(nums)):
            if not tmp or nums[i] - tmp[0] <= D:
                tmp.append(nums[i])
                helper(res, tmp, i+1, k-1)
                tmp.pop()
    helper(res, tmp, 0, k)
    return res
print(len(perm(nums,3)))
'''


'''
3.雀魂启动！
时间限制：1秒
空间限制：32768K

小包最近迷上了一款叫做雀魂的麻将游戏，但是这个游戏规则太复杂，小包玩了几个月了还是输多赢少。
于是生气的小包根据游戏简化了一下规则发明了一种新的麻将，只留下一种花色，
并且去除了一些特殊和牌方式（例如七对子等），具体的规则如下：

总共有36张牌，每张牌是1~9。每个数字4张牌。
你手里有其中的14张牌，如果这14张牌满足如下条件，即算作和牌
14张牌中有2张相同数字的牌，称为雀头。
除去上述2张牌，剩下12张牌可以组成4个顺子或刻子。顺子的意思是递增的连续3个数字牌（例如234,567等），
刻子的意思是相同数字的3个数字牌（例如111,777）

例如：
1 1 1 2 2 2 6 6 6 7 7 7 9 9 可以组成1,2,6,7的4个刻子和9的雀头，可以和牌
1 1 1 1 2 2 3 3 5 6 7 7 8 9 用1做雀头，组123,123,567,789的四个顺子，可以和牌
1 1 1 2 2 2 3 3 3 5 6 7 7 9 无论用1 2 3 7哪个做雀头，都无法组成和牌的条件。

现在，小包从36张牌中抽取了13张牌，他想知道在剩下的23张牌中，再取一张牌，取到哪几种数字牌可以和牌。

输入描述:
输入只有一行，包含13个数字，用空格分隔，每个数字在1~9之间，数据保证同种数字最多出现4次。

输出描述:
输出同样是一行，包含1个或以上的数字。代表他再取到哪些牌可以和牌。
若满足条件的有多种牌，请按从小到大的顺序输出。
若没有满足条件的牌，请输出一个数字0

输入例子1:
1 1 1 2 2 2 5 5 5 6 6 6 9

输出例子1:
9

例子说明1:
可以组成1,2,6,7的4个刻子和9的雀头

输入例子2:
1 1 1 1 2 2 3 3 5 6 7 8 9

输出例子2:
4 7

例子说明2:
用1做雀头，组123,123,567或456,789的四个顺子

输入例子3:
1 1 1 2 2 2 3 3 3 5 7 7 9

输出例子3:
0

例子说明3:
来任何牌都无法和牌


[Analysis]: 逆向思维
不从已有的牌面推导出再取什么牌才能胡牌，而是看依次将所能取的牌中一张牌加入是否能听胡。
所以简化为判断14张牌是否可以胡牌，即bingo。
胡牌主要有三方面，一是雀头，那么只能是雀头没选择出来的情况进行选择，即当前牌数不是3的倍数；
其次是刻子或顺子，只需对排除了这三张牌的牌面能否bingo。
[Note]:
__name__ 是当前模块名，当模块被直接运行时模块名为 __main__ 。
这句话的意思就是，当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。

[Time]: O(n*n*logn)


'''
from collections import Counter
def bingo(seq):
    if not seq:
        return True
    n = len(seq)
    #O(4) = O(1)
    first = seq.count(seq[0])
    #判断雀头，14 = 2 + 12， 这里又不考虑龙、暗7对的情况，所以只能有一对雀头，剩下的4组为顺子和刻子的组合。
    if n % 3 != 0 and first >= 2 and bingo(seq[2:]):
        return True
    #判断顺子
    if first >= 3 and bingo(seq[3:]):
        return True
    #判断刻子
    if seq[0] + 1 in seq and seq[0] + 2 in seq:
        #O(n)
        temp = seq[:]
        #只能一个个地按value来remove，因为不知道具体有多少个重复数字（即不知道index）
        temp.remove(seq[0])
        temp.remove(seq[0]+1)
        temp.remove(seq[0]+2)
        if bingo(temp):
            return True
    return False

if __name__ == '__main__':
    nums = list(map(int, input().strip().split()))
    #O(n)
    counted = Counter(nums)
    #set possible is not ordered
    #O(9) = O(1)
    possible = set(range(1, 10)) - {num for num in counted if counted[num] == 4}
    res = []
    for num in possible:
        #O(nlogn)
        if bingo(sorted(nums + [num])):
            res.append(str(num))
    if not res:
        print(0)
    else:
        print(' '.join(sorted(res)))


'''
4.特征提取
时间限制：1秒
空间限制：32768K

小明是一名算法工程师，同时也是一名铲屎官。某天，他突发奇想，想从猫咪的视频里挖掘一些猫咪的运动信息。
为了提取运动信息，他需要从视频的每一帧提取“猫咪特征”。
一个猫咪特征是一个两维的vector<x, y>。如果x_1=x_2 and y_1=y_2，那么这俩是同一个特征。
因此，如果喵咪特征连续一致，可以认为喵咪在运动。
也就是说，如果特征<a, b>在持续帧里出现，那么它将构成特征运动。
比如，特征<a, b>在第2/3/4/7/8帧出现，那么该特征将形成两个特征运动2-3-4 和7-8。
现在，给定每一帧的特征，特征的数量可能不一样。小明期望能找到最长的特征运动。

输入描述:
第一行包含一个正整数N，代表测试用例的个数。

每个测试用例的第一行包含一个正整数M，代表视频的帧数。

接下来的M行，每行代表一帧。其中，第一个数字是该帧的特征个数，接下来的数字是在特征的取值；
比如样例输入第三行里，2代表该帧有两个猫咪特征，<1，1>和<2，2>
所有用例的输入特征总数和<100000

N满足1≤N≤100000，M满足1≤M≤10000，一帧的特征个数满足 ≤ 10000。
特征取值均为非负整数。

输出描述:
对每一个测试用例，输出特征运动的长度作为一行

输入例子1:
1
8
2 1 1 2 2
2 1 1 1 4
2 1 1 2 2
2 2 2 1 4
0
0
1 1 1
1 1 1

输出例子1:
3

例子说明1:
特征<1,1>在连续的帧中连续出现3次，相比其他特征连续出现的次数大，所以输出3。

[Analysis]: 哈希表
用哈希表顺序存储每一个特征，按照每一行的顺序读取。
由于我们需要的是最大连续特征，那么为了保证连续，在读取本行结束时，遍历哈希表内的键，判断是否在本行中。
在本行的话，不做处理，不在本行的话，重置其键值为1。
接着记录当前最大键值即可。

'''
if __name__ == '__main__':
    N = int(input().strip())
    for _ in range(N):
        M = int(input().strip())
        res = 0
        seen = {}
        for i in range(M):
            arr = list(map(int, input().strip().split()))
            n = arr[0]
            one_frame = [(arr[2*i-1], arr[2*i]) for i in range(1,n+1)]
            for f in one_frame:
                if f in seen:
                    seen[f] += 1
                else:
                    seen[f] = 1
                if seen[f] > res:
                    res = seen[f]
            #重置那些不连续的特征为1
            for fea in seen:
                if fea not in one_frame:
                    seen[fea] = 1
        print(res)

'''
5.毕业旅行问题
时间限制：1秒
空间限制：32768K

小明目前在做一份毕业旅行的规划。
打算从北京出发，分别去若干个城市，然后再回到北京，每个城市之间均乘坐高铁，且每个城市只去一次。
由于经费有限，希望能够通过合理的路线安排尽可能的省一些路上的花销。
给定一组城市和每对城市之间的火车票的价钱，找到每个城市只访问一次并返回起点的最小车费花销。

输入描述:
城市个数n（1<n≤20，包括北京）
城市间的车票价钱 n行n列的矩阵 m[n][n]

输出描述:
最小车费花销 s

输入例子1:
4
0 2 6 5
2 0 4 4
6 4 0 2
5 4 2 0

输出例子1:
13

例子说明1:
共 4 个城市，城市 1 和城市 1 的车费为0，城市 1 和城市 2 之间的车费为 2，
城市 1 和城市 3 之间的车费为 6，城市 1 和城市 4 之间的车费为 5，依次类推。
假设任意两个城市之间均有单程票可购买，且票价在1000元以内，无需考虑极端情况。
'''
class Solution:
    def tsp(self, c):
        n = len(c)
        m = 2**(n)
        dp = [[float('inf')]*n for _ in range(m)]
        dp[1][0] = 0
        res = float('inf')
        for i in range(1, m):
            for j in range(1, n):
                if i&(1<<j): continue # j后面是要加入i的，这里不能重复
                for k in range(n):
                    if i&(1<<k): # i中必须得包括k
                        dp[i|(1<<j)][j] = min(dp[i|(1<<j)][j], dp[i][k] + c[k][j])
        for j in range(1,n):
            res = min(res, dp[m-1][j] + c[j][0])
        return res

if __name__ == '__main__':
    n = int(input().strip())
    c = []
    for i in range(n):
        c.append(list(map(int,input().strip().split())))
    print(Solution().tsp(c))




'''
6.找零
时间限制：1秒
空间限制：32768K

Z国的货币系统包含面值1元、4元、16元、64元共计4种硬币，以及面值1024元的纸币。
现在小Y使用1024元的纸币购买了一件价值为 N (0 < N <= 1024) 的商品，请问最少他会收到多少硬币？

输入描述:
一行，包含一个数N。

输出描述:
一行，包含一个数，表示最少收到的硬币数。

输入例子1:
200

输出例子1:
17

例子说明1:
花200，需要找零824块，找12个64元硬币，3个16元硬币，2个4元硬币即可。

'''
class Solution:
    def coin_change(self, m):
        coins = [1,4,16,64]
        dp = [float('inf')] * (m+1)
        dp[0] = 0
        for i in range(1,m+1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i-coin]+1, dp[i])
        return dp[m]
if __name__ == '__main__':
    m = 1024 - int(input().strip())
    print(Solution().coin_change(m))


'''
7.机器人跳跃问题
时间限制：1秒
空间限制：32768K

机器人正在玩一个古老的基于DOS的游戏。
游戏中有N+1座建筑——从0到N编号，从左到右排列。
编号为0的建筑高度为0个单位，编号为i的建筑的高度为H(i)个单位。

起初， 机器人在编号为0的建筑处。每一步，它跳到下一个（右边）建筑。
假设机器人在第k个建筑，且它现在的能量值是E, 下一步它将跳到第个k+1建筑。
它将会得到或者失去正比于与H(k+1)与E之差的能量。
如果 H(k+1) > E 那么机器人就失去 H(k+1) - E 的能量值，否则它将得到 E - H(k+1) 的能量值。

游戏目标是到达第个N建筑，在这个过程中，能量值不能为负数个单位。
现在的问题是机器人以多少能量值开始游戏，才可以保证成功完成游戏？

输入描述:
第一行输入，表示一共有 N 组数据.

第二个是 N 个空格分隔的整数，H1, H2, H3, ..., Hn 代表建筑物的高度

输出描述:
输出一个单独的数表示完成游戏所需的最少单位的初始能量

输入例子1:
5
3 4 3 2 4

输出例子1:
4

输入例子2:
3
4 4 4

输出例子2:
4

输入例子3:
3
1 6 4

输出例子3:
3



[Analysis]:

[Method 1]
用二分查找来找到最小能量值，start=0，end=max(H),高度小于能量值时，能量只增不减，能量最大值为max(H);
遍历建筑物，更新E值，若中间E小于0，则更新start=mid+1；
反之end=mid；
最后返回end。
'''

def binary_search(H):
    start, end = 0, max(H)
    while start < end:
        mid = start + (end - start)//2
        E = mid
        succeed = True
        for h in H:
            if E < h:
                E -= (h-E)
            else:
                E += (E-h)
            if E < 0:
                start = mid + 1
                succeed = False #E值不通过
                break
        if succeed: #如果到最后还剩有能量
            end = mid
    return end

if __name__ == '__main__':
    N = int(input().strip())
    H = list(map(int,input().strip().split()))
    print(binary_search(H))

'''
[Method 2]:
跳前，能量为E,
跳后，能量为E + (E-h) = 2E - h
所以跳前的E等于跳后的能量E的 (E + h) >> 1,
我们可以假设最后跳完的能量刚好为0，
则从最后一个建筑开始往前更新E，到建筑0时的能量就是所需的最小初始能量。
但是因为E只取整数，
所以再将(E + h)加除以2前应该加1，
这样如果(E + h)为奇数时加1再除以2就可以进位，
为偶数时加1再除也不影响。
'''
def hop(H):
    E = 0
    H.reverse()
    for h in H:
        E = (E + h) >> 1
    return E

if __name__ == '__main__':
    input()
    H = list(map(int,input().strip().split()))
    print(hop(H))
