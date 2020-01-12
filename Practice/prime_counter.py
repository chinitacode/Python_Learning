from math import sqrt
from time import time

def prime_counter(n):
    start = time()
    count = 0
    for i in range(2 , n+1):
        prime = True
        k = 2
        while k <= sqrt(i):
            if i % k == 0:
                prime = False
                break
            k += 1
        if prime:
            count += 1
    t = time() - start
    return count,t

def count_prime(n):
    start = time()
    #Create an array of boolean values of True,
    #and mark as False the numbers which are not prime.
    #Sum off the True values in the end.
    is_prime = [True]*(n + 1)
    i = 2
    while i <= sqrt(n):
        if is_prime[i]:
            j = i
            while j*i <= n:
                is_prime[i*j] = False
                j += 1
        i += 1

    count = sum(is_prime[2 : n+1])
    t = time() - start
    return count,t

from math import sqrt

def prime_table(n):
    is_prime = [True] * (n + 1)
    i = 2
    while (i * i <= n):
        if (is_prime[i]):
            j = i
            while (j * i <= n):
                is_prime[i * j] = False
                j += 1
        i += 1
    table = []
    for i in range(2,n+1):
        if is_prime[i]:
            table.append(i)
    return table
