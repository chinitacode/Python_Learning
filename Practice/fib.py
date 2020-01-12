def fib_iter(n):
    i = 0
    prev,curr = 0,1
    while i < n:
        prev,curr = curr,prev + curr
        i += 1
    return prev

def fib_recur(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-2) + fib_recur(n-1)

def fib(n):
    prev,curr = 0,1
    for i in range(n):
        prev,curr = curr,prev+curr
    return prev
    
