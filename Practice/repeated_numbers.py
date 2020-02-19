# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in range(len(numbers)):
            numbers[i] += 1
        print(numbers)
        for i in range(len(numbers)):
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
    


