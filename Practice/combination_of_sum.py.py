import sys 

def comb_sum(n, k):
    result = []
    tmp = []
    def helper(result, tmp, n, pos, k):
        total = sum(tmp)
        if k == 0:
            if total % n == 0:
                result.append(tmp[:])
                return
            else:
                return
        for i in range(pos, n):
            tmp.append(i)
            helper(result, tmp, n, i + 1, k - 1)
            tmp.pop()
    helper(result, tmp, n, 0, k)
    return len(result)


try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        n, k = list(map(int, line.split()))
except:
    pass



'''
for line in sys.stdin:
    n, k = map(int,line.split())
    print(comb_sum(n,k))
'''

'''
for line in sys.stdin:
    if not line:
        break
    n, k = map(int,line.split())
    print(comb_sum(n,k))
'''
