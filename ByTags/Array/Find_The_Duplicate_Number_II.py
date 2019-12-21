'''
【剑指offer】
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。
也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。


[Method 1]: 抽屉原理(桶排序)
因为原数组包含的是从0到n-1的数，为了处理0，先把原数组每个数+1，
然后遍历每个数，把每个数(其绝对值-1)看成是一个index，把该index的数取反，
表示该index的数是存在的，
因为只需要输出第一个重复的数字，
则当我们遇到该index的数为负时，就可以直接输出其idx，即为重复的数字，并返回True。
否则遍历完后返回False。
'''
# python 2.7.3
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in xrange(len(numbers)):
            numbers[i] += 1
        for i in xrange(len(numbers)):
            idx = abs(numbers[i]) - 1
            if numbers[idx] < 0:
                duplication[0] = idx
                return True
            numbers[idx] = - numbers[idx]
        return False


if __name__ == '__main__':
    sol = Solution()
    duplication = [False]
    s = sol.duplicate([2,3,1,0,2,5,3],duplication)
    print(s)
    print(duplication)


'''
拓展：如果要求输出所有重复的数组成的list，
和未出现的数字list：
仍然是把数字先加1避免处理0不好取反的情况，
然后把每个数（绝对值-1）看成是数组下标，
把对应的数取反，
遍历时当当前数为负，则说明当前idx重复出现了，加入duplication这个set中，
最后再遍历一次，把不在duplication的为正的数的index加入到missing中。
'''
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到所有重复的一个值加入到duplication
    # 并且找到missing numbers加入到missing
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            numbers[i] += 1
        print(numbers)
        for i in range(len(numbers)):
            idx = abs(numbers[i]) - 1
            if numbers[idx] < 0:
                duplication.add(idx)
            numbers[idx] = - numbers[idx]
        missing = [idx for idx in range(len(numbers)) if numbers[idx] > 0 and idx not in duplication]
        print('missing numbers: ',missing)
        return missing != None


if __name__ == '__main__':
    sol = Solution()
    duplication = set()
    s = sol.duplicate([2,3,1,0,2,5,3],duplication)
    print(s)
    print('Repeated numbers: ',duplication)

    '''
    [3, 4, 2, 1, 3, 6, 4]
    missing numbers:  [4, 6]
    True
    Repeated numbers:  {2, 3}
    '''

'''
[Method 2]: 交换排序
利用元素数字都在0到n-1的范围内的特点，若不存在重复数字，
则排序后的数字就在与其相同的索引值的位置，即数字i在第i个位置。
遍历的过程中寻找位置和元素不相同的值，并进行交换排序，
在此过程中如果有 numbers[i] == numbers[numbers[i]], 则找到重复数字，输出返回。
时间复杂度O(n)，空间复杂度O(1)。
'''

# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            while i != numbers[i]:
                idx = numbers[i]
                if numbers[i] == numbers[idx]:
                    duplication[0] = numbers[i]
                    return True
                numbers[i], numbers[idx] = numbers[idx], numbers[i]
        return False

if __name__ == '__main__':
    sol = Solution()
    duplication = [False]
    s = sol.duplicate([2,3,1,0,2,5,3],duplication)
    print(s)
    print(duplication)




'''
要求不mutate原数组，则和leetcode的本题思路相同，
即用二分法（种方法无法保证找出所有的重复数字，需要在解决前了解需求。）或者快慢指针
[Method 3]: 二分法(分治，抽屉原理) O(nlogn)
这道题目主要应用了抽屉原理和分治的思想。

抽屉原理：n+1 个苹果放在 n 个抽屉里，那么至少有一个抽屉中会放两个苹果。

用在这个题目中就是，一共有 n+1 个数，每个数的取值范围是1到n，所以至少会有一个数出现两次。

然后我们采用分治的思想，将每个数的取值的区间[1, n]划分成[1, n/2]和[n/2+1, n]两个子区间，
然后分别统计两个区间中数的个数。
注意这里的区间是指 数的取值范围，而不是 数组下标。

划分之后，左右两个区间里一定至少存在一个区间，区间中数的个数大于区间长度。
这个可以用反证法来说明：如果两个区间中数的个数都小于等于区间长度，
那么整个区间中数的个数就小于等于n，和有n+1个数矛盾。

因此我们可以把问题划归到左右两个子区间中的一个，而且由于区间中数的个数大于区间长度，
根据抽屉原理，在这个子区间中一定存在某个数出现了两次。

依次类推，每次我们可以把区间长度缩小一半，直到区间长度为1时，我们就找到了答案。

复杂度分析
时间复杂度：每次会将区间长度缩小一半，一共会缩小 O(logn) 次。
每次统计两个子区间中的数时需要遍历整个数组，时间复杂度是 O(n)。
所以总时间复杂度是 O(nlogn)。
空间复杂度：代码中没有用到额外的数组，所以额外的空间复杂度是 O(1)。


'''
