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
