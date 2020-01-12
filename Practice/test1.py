import sys
from math import sqrt
while True:
    n,m = input().split()
    n,m = int(n),int(m)
    l = [n]
    for i in range(m-1):
        n = sqrt(n)
        l.append(n)
    sys.stdout.write(str(round(sum(l),2))+'\n')
