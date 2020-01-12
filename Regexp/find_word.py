def find_start_word(fname):
    f = open(fname)
    for line in f:
        '''
        line in txt files ends with '\n'
        so it can also be written as
        line.endswith('.\n')
        '''
        if line.startswith('hello')\
            and line[:-1].endswith('.'):
            print(line)

find_start_word('word.txt')
