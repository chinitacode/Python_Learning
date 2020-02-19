coins1 = [2, 5, 3]
N1 = [5, 5, 5]
m1 = 12

coins2 = [5, 3, 2]
N2 = [1, 5, 5]
m2 = 13



def coin_change1(coins, m, N):
    n = len(coins)
    dp = [float('inf')] * (m + 1)
    dp[0] = 0
    for i in range(n):
        for j in range(m, coins[i]-1, -1):
            for k in range(1, N[i] + 1):
                if k*coins[i] <= j:
                    dp[j] = min(dp[j], dp[j - k*coins[i]] + k)
    print(dp)
    return -1 if dp[m] == float('inf') else dp[m]

#print(coin_change1(coins1, m1, N1))
print(coin_change1(coins2, m2, N2))


def coin_change2(coins, m, N):
    n = len(coins)
    dp = [float('inf')] * (m + 1)
    dp[0] = 0
    def unbounded(coin, k):
        for j in range(coin, m+1):
            dp[j] = min(dp[j], dp[j-coin] + k)
    def zeroOne(coin, k):
        for j in range(m, coin-1, -1):
            dp[j] = min(dp[j], dp[j-coin] + k)
    def multi(coin, count):
        if count*coin > m:
            unbounded(coin, 1)
            return
        k = 1
        while k < count:
            zeroOne(k*coin, k)
            count = count - k
            k = k*2
        zeroOne(count*coin, count)
    for i in range(n):
        multi(coins[i], N[i])
    print(dp)
    return -1 if dp[m] == float('inf') else dp[m]

print(coin_change2(coins2, m2, N2))
