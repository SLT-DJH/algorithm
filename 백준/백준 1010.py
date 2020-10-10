T = int(input())

dp = [1, 1]

for i in range(2, 31) :
    dp.append(i * dp[i-1])

for _ in range(T) :
    N, M = map(int, input().split())
    
    get = dp[M] // dp[M-N]
    
    print(get // dp[N])
