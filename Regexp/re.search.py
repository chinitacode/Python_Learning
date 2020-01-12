# Using the find method for strings only:
'''
def use_find(fname):
    f = open(fname)
    for line in f:
        line = line.rstrip()
        if line.find('From') >= 0: # Or line.startswith('From')
            print(line)

use_find('mbox-short.txt')
'''
# Using re.search() to search the special characters at each position of all lines
import re

'''
def use_re(fname):
    f = open(fname)
    for line in f:
        line = line.rstrip()
        if re.search('From', line):
            print(line)
use_re('mbox-short.txt')
'''
# Search the special characters only at the beginnings of all lines
def use_re(fname):
    f = open(fname)
    for line in f:
        line = line.rstrip()
        if re.search('^From', line):
            print(line)
use_re('mbox-short.txt')
