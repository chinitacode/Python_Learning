import sys 


    
def ugly_str(s):
    slist = list(s)
    count = 0
    for i in range(len(s) - 1):
        if slist[0] == '?':
            if slist[1] == 'A':
                slist[0] = 'B'
            elif slist[1] == 'B':
                slist[0] == 'A'
            else:
                slist[]
        if slist[i] == '?':
            if slist[i + 1] == 'A':
                slist[i] = 'B'
            elif slist[i + 1] == 'B':
                slist[i] = 'A'
            else:
                for j in range(i,len(s) - 1 - i):
                    if slist[j] != '?':
                        
        if slist[i] == slist[i+1]:
            count += 1
    return count




for line in sys.stdin:
    s = line
    print(ugly_str(s))
