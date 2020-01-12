import sys 
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))


import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)


import sys
try:
    while True:
        line =  sys.stdin.readline().strip()
        if line == '':
            break
        a = list(map(int, line.split(' ')))
except:
    pass

'''
input() takes an optional prompt argument. It also strips the trailing
newline character from the string it returns,
and supports history features if the readline module is loaded.

readline() takes an optional size argument,
does not strip the trailing newline character and
does not support history whatsoever.
#
readline(limit=-1)
Read and return one line from the stream. If limit is specified,
at most limit bytes will be read.

The line terminator is always b'\n' for binary files; for text files,
the newlines argument to open() can be used to select the line terminator(s)
recognized.

readlines(hint=-1)
Read and return a list of lines from the stream.
hint can be specified to control the number of lines read:
no more lines will be read if the total size (in bytes/characters) of
all lines so far exceeds hint.
'''
#如果只有一行input且只有两个数字
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        n, k = list(map(int, line.split()))
except:
    pass
