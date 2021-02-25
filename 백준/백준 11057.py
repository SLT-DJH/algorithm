dp = [0]

start = [1] * 10
temp = [0] * 10

for i in range(1, 1001) :
    dp.append(sum(start) % 10007)

    startnum = dp[i]

    for j in range(10) :
        if j == 0 :
            temp[j] = startnum
        else :
            temp[j] = temp[j-1] - start[j-1]

    start = temp
    temp = [0] * 10

N = int(input())

print(dp[N])
