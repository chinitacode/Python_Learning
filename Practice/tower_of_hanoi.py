def hanoi(n, start, end, mid):
    if n == 1:
        print('Move disk 1 from rod', start, 'to rod', end)
    else:
        hanoi(n-1, start, mid, end)
        print('Move disk', n, 'from rod', start, 'to rod', end)
        hanoi(n-1, mid, end, start)
        
