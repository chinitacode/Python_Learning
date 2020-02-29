'''
将元素为str的任意嵌套层列表转化为一个字符串，
并用'\n'连接。要求用递归实现。

input: 元素为字符串的任意嵌套列表
output: 以'\n'连接的一个字符串

例：
输入： [["a", ["b", "c"], "d"]
输出： "a\nb\nc\nd"
'''


import sys
def transform_string(arr):
    try:
        return "\n".join(arr)
    except:
        l = []
        for e in arr:
            l.append(transform_string(e))
        return "\n".join(l)

if __name__ == "__main__":
    arr = eval(sys.stdin.readline().strip())
    print(transform_string(arr))
