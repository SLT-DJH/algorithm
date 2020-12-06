dp = [0] * 1001

box = [[1] * 10]

for i in range(1, 1001) :
    dp[i] = sum(box[i-1]) % 10007

    temp = []

    now = dp[i]

    for j in range(10) :
       temp.append(now)

       now -= box[i-1][j]

    box.append(temp)


n = int(input())

print(dp[n])
