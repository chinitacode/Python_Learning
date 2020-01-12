import re

def sum_numbers(fname):
    nums_str = []
    f = open(fname)
    for line in f:
        tmp = re.findall('.*?([0-9]+)', line)
        if len(tmp) < 1: continue
        nums_str += tmp
    nums = list(map(int, nums_str))
    return sum(nums)

print(sum_numbers('regex_sum_42.txt'))
print(sum_numbers('regex_sum_164642.txt'))
