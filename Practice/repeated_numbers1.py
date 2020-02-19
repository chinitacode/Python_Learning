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
