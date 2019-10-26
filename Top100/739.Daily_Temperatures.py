'''
739. Daily Temperatures [Medium]
Given a list of daily temperatures T, return a list such that,
for each day in the input, tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example,
given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].

[Method 1]: 单调栈+逆序遍历
本题使用逆序遍历，为什么要使用逆序遍历。
因为正常遍历思路，遍历到当前天，你无法知道后面几天的温度情况。
逆序遍历，后面几天的温度情况已经知晓，很容易得到经过几天后的温度比今天温度高。

思路：
逆序遍历，把每天温度保存下来，存放在一个单调递减的栈中，
如果不满足这个要求，则需要将栈顶元素依次弹出，直至重新满足要求为止。
不满足要求的情况即为，当前天的温度等于或者比栈顶的温度要高；
重新满足要求后，栈顶元素即为后面比当前天温度高的一天；
如果栈空了，然么说明后面几天没有比当前天温度还要高的。

上面讲栈中存放的是当前天的温度，实际上存放的当前天温度对应的数组下标(index)。
有了数组下标就也有了当前天的温度。
因为要计算隔了几天后温度比当前天温度高，存放数组下标更合适(直接用栈顶元素下标减去当前index)。
[Time]: O(n)
[Space]: O(W), W is the size of the stack. The size of the stack is bounded
as it represents strictly increasing temperatures. If T = [73,73,73,73,73], then W = 1.
Runtime: 544 ms, faster than 60.71% of Python3 online submissions for Daily Temperatures.
Memory Usage: 17.4 MB, less than 15.79% of Python3 online submissions for Daily Temperatures.
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0]*len(T)
        for i in range(len(T)-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res

'''
[Method 2]: 单调栈+顺序遍历
每个温度都按顺序入栈。
出栈条件：遇到比自己大的温度，出栈时索引距离即天数差。
[space]: O(n)  because the stack stores indices with duplicated temperatures,
If T = [73,73,73,73,73], then stack = [73,73,73,73,73].
Runtime: 520 ms, faster than 94.45% of Python3 online submissions for Daily Temperatures.
Memory Usage: 17.4 MB, less than 13.16% of Python3 online submissions for Daily Temperatures.
'''
class Solution(object):
    def dailyTemperatures(self, T):
        stack, r = [], [0] * len(T)
        for i, t in enumerate(T):
            #出栈条件：栈顶温度低于当前温度，则可以赋值给output
            while stack and T[stack[-1]] < t:
                r[stack.pop()] = i - stack[-1]
            stack.append(i)
        return r

'''
#Or:
Runtime: 516 ms, faster than 96.86% of Python3 online submissions for Daily Temperatures.
Memory Usage: 17.5 MB, less than 10.53% of Python3 online submissions for Daily Temperatures.
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, r = [], [0] * len(T)
        for i in range(len(T)):
            #出栈条件：栈顶温度低于当前温度，则可以赋值给output
            while stack and T[stack[-1]] < T[i]:
                r[stack.pop()] = i - stack[-1]
            stack.append(i)
        return r


'''
[Method 3]: 后序遍历。
从倒数第二天开始往前遍历，记录k为下一个可能比本身温度高的那天的index，
看当天温度t是否高于或者等于第k天的温度(即k不合格，需要再往后看)，如果res[k]为0，则说明后面没有比第k日高的温度，即也没有比当天t更高的温度；
反之，则k += res[k], 即去查看下一个比之前k更高的温度，看是否也高于t...，如果没有，则继续看res[k]是否为0，即对比后面的温度，
因此此处需要用一个while循环。
[Time]: O(n*w), w为k需要更新的次数
[Space]: O(1)
Runtime: 524 ms, faster than 91.29% of Python3 online submissions for Daily Temperatures.
Memory Usage: 17.6 MB, less than 10.53% of Python3 online submissions for Daily Temperatures.
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        for i in range(len(T) - 2, -1, -1):
            k = i+1
            while T[i] >= T[k] and res[k] != 0:
                k += res[k]
            if T[i] < T[k]:
                res[i] = k-i
        return res


'''
[Method 4]: Hashmap of the next higher temperature
The range of temperature is quite small: [30, 100]
so it is possible to have a hash map of temperatures to earliest days when that higher temperature occurred.

We iterate through the list of temperatures from the back,
and for each day, loop through higher temperatures to check if it exist in the following days' temperatures,
and count the minimum distance of days.

Example, for the input, when we are at 72
[73, 74, 75, 71, 69, 72, 76, 73]
                      ^
# We have the following hash map:
{
  73: 7,
  76: 6,
}
Then we iterate from 73, 74, ... to check whether a higher temperature exists in its hashmap,
then we find 73 is in the hashmap, and its value(corresponds to its index) is 7,
then we update the variable 'day' to store the minimal days difference substracting i by the minimal index 7,
which is 2,
and continue the iteration and find 76 exists in the hashmap as well, and its value is 6,
so we update 'day' with the minimal days to wait 6-5 = 1,
next we check if 'day' has real value(we initialize it with float('inf') for example),
if so, update the output array res[i] =  day = 1
So the minimum day to wait for temperatures higher than 72 is 1.
[Time]: O(N*W), W is the range of the temperature, here the greatest value of W is 70 (if t == 30);
[Space]: O(N)
Runtime: 2524 ms, faster than 5.01% of Python3 online submissions for Daily Temperatures.
Memory Usage: 17.4 MB, less than 13.16% of Python3 online submissions for Daily Temperatures.
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if not T: return
        nxt, res = {}, [0] * len(T)
        nxt[T[-1]] = len(T) - 1
        for i in range(len(T)-2, -1, -1):
            days = float('inf')
            for t in range(T[i]+1, 101):
                if t in nxt:
                    days = min(days, nxt[t] - i)
                if days < float('inf'):
                    res[i] = days
            nxt[T[i]] = i
        return res

'''
# Or:
Runtime: 1224 ms, faster than 6.39% of Python3 online submissions for Daily Temperatures.
Memory Usage: 17.5 MB, less than 10.53% of Python3 online submissions for Daily Temperatures.
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        nxt = [float('inf')] * 102
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            #Use 102 so min(nxt[t]) has a default value
            warmer_index = min(nxt[t] for t in range(T[i]+1, 102))
            if warmer_index < float('inf'):
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans
