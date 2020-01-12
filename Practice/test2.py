import sys

l = input()
output = [l]
n = len(l)
for i in range(n):
    output.append(output[i][1:] + output[i][:1])
num = len(set(output))
sys.stdout.write(str(num)+'\n')
