N = int(input())

numlist = list(map(int, input().split()))

dp = [0] * N

for i in range(N) :
    if dp[i] == 0 :
        dp[i] = numlist[i]
        
    for j in range(i+1, N) :
        if numlist[i] < numlist[j] :
            dp[j] = max(dp[j], dp[i] + numlist[j])

print(max(dp))
