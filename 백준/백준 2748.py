dp = [0 for _ in range(41)]

dp[0] = [1,0]
dp[1] = [0,1]

for i in range(2, 41) :
    box = []

    box.append(dp[i-1][0] + dp[i-2][0])
    box.append(dp[i-1][1] + dp[i-2][1])

    dp[i] = box

T = int(input())

for _ in range(T) :

    n = int(input())
    
    print(dp[n][0], dp[n][1])
    
