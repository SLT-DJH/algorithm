n = int(input())

dp = [0 for i in range(301)]

box = [0 for i in range(301)]

for i in range(n) :
    box[i] = int(input())

for i in range(3) :
    if i == 0 :
        dp[i] = box[0]
    elif i == 1 :
        dp[i] = box[0] + box[1]
    elif i == 2 :
        dp[i] = max(box[0] + box[2], box[1] + box[2])

for i in range(3, n) :
    dp[i] = max(dp[i-3] + box[i-1] + box[i], dp[i-2] + box[i])

print(dp[n-1])
