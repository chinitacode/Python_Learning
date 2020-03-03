'''
263. 丑数 [简单]

编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:

输入: 6
输出: true
解释: 6 = 2 × 3
示例 2:

输入: 8
输出: true
解释: 8 = 2 × 2 × 2
示例 3:

输入: 14
输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数 7。
说明：

1 是丑数。
输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。
'''
class Solution:
    def isUgly(self, num: int) -> bool:
        if not num: return False
        while num%2 == 0:
            num >>= 1
        while num %3 == 0:
            num //= 3
        while num%5 == 0:
            num //= 5
        return num == 1


'''
264. 丑数 II [中等]
编写一个程序，找出第 n 个丑数。
丑数就是只包含质因数 2, 3, 5 的正整数。

示例:

输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:

1 是丑数。
n 不超过1690。


[Method 1]: Heap + Hash table
我们从堆中包含一个数字开始：1，去计算下一个丑数。
将 1 从堆中弹出然后将三个数字添加到堆中：1×2, 1×3，和 1×5。
现在堆中最小的数字是 2。为了计算下一个丑数，要将 2 从堆中弹出然后添加三个数字：2×2, 2×3，和 2×5。
重复该步骤计算所有丑数。
在每个步骤中，弹出堆中最小的丑数 k，并在堆中添加三个丑数：k×2, k×3，和 k×5。

必须用堆来保证新加入丑数数组的丑数顺序，因为丑数只可能从前面的数分别 ×2, ×3，和 ×5得到，
而很明显后面的 ×3，和 ×5会得到比用前面几个丑数分别 x2都大的数，所以我们必须把这三个数入堆和
还没剩下的堆里还没取出放入丑数数组的数进行比较。

此外我们用set来作hash table存储已经出现过了的丑数来避免重复（如3*4和2*6都为丑数12）

[Time]: O(N * (log(2n) + 3*log(2n))) = O(N*logN)
[Space]: O(n), 丑数数组和hash table 各自要用差不多O(n)的空间，另外每从堆里取一个丑数就加入新的3个丑数，
堆的大小差不多在O(2N), 加起来是O(4n) = n
'''
from heapq import heappush, heappop

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if not n: return
        count = 0
        nums, seen, heap = [], {1}, [1]
        while count < n:
            num = heappop(heap) # O(log 2n)
            nums.append(num)
            count += 1
            for i in [2,3,5]:
                ugly = num * i
                if ugly not in seen: # O(1)
                    heappush(heap, ugly) # O(log 2n)
                    seen.add(ugly)
        return nums[n-1]

'''
[Method 2]: 动态规划+三指针
此处的动态规划转移方程不能定量的写出来，但是应该能感觉到第i个丑数是由前面的数X2/3/5造出来的
至于究竟X多少，需要找到这些数里面比前一个丑数大的最小的值
由此引入三指针的解法
'''
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1 for _ in range(n)]
        # 三指针初始化
        i2 = 0
        i3 = 0
        i5 = 0
        for i in range(1,n):
            min_val = min(dp[i2]*2,dp[i3]*3,dp[i5]*5)
            dp[i] = min_val
            # 找出哪个指针对应的数造出了现在这个最小值，将指针前移一位
            if dp[i2]*2 == min_val:  
                i2 += 1
            if dp[i3]*3 == min_val: # 单独用if不用elif可以解决如当 dp[i2]== 5 和 dp[i5] == 2时，两个指针都要前进一位
                i3 += 1
            if dp[i5]*5 == min_val:
                i5 += 1
        return dp[-1]



'''
因为n 不超过1690，所以也可以预计算 1690 个丑数，使用另一个 Ugly 类在构造函数中完成所有丑数的预计算，
然后声明一个 Ugly 类的实例对象，将该实例对象声明为 Solution 类的静态变量。
'''
from heapq import heappop, heappush
class Ugly:
    def __init__(self):
        seen = {1, }
        self.nums = nums = []
        heap = []
        heappush(heap, 1)

        for _ in range(1690):
            curr_ugly = heappop(heap)
            nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly * i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)

class Solution:
    u = Ugly()
    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]
