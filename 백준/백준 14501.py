N = int(input())

dp = [0 for _ in range(N+2)]

daybox = [0]
paybox = [0]

for _ in range(N) :
    a, b = map(int, input().split())

    daybox.append(a)
    paybox.append(b)

daybox.append(0)
paybox.append(0)

for i in range(1, len(daybox)) :
    dp[i] = max(dp[i], dp[i-1])
    
    if i + daybox[i] < len(daybox) :
        dp[i+daybox[i]] = max(dp[i+daybox[i]], dp[i] + paybox[i])


print(dp[N+1])
