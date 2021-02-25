r, n = map(int, input().split())

box = []

box.append([0,1,1])

for _ in range(n) :
    t, tx, ty = map(int, input().split())

    box.append([t, tx, ty])

dp = [0] * (n+1)

if n <= 1000 :

    for i in range(1, n+1) :
        get = box[i]

        temp = 0

        for j in range(0, i) :
            if j != 0 :
                T = get[0] - box[j][0]
                dis = abs(get[1] - box[j][1]) + abs(get[2] - box[j][2])

                if T >= dis :
                    if dp[j] != 0 :
                        temp = max(dp[j]+1, temp)
            else :
                T = get[0] - box[j][0]
                dis = abs(get[1] - box[j][1]) + abs(get[2] - box[j][2])

                if T >= dis :
                    temp = max(dp[j]+1, temp)                

        dp[i] = temp

    print(max(dp))
else :
    
    for i in range(1, 1001) :
        get = box[i]

        temp = 0

        for j in range(0, i) :
            if j != 0 :
                T = get[0] - box[j][0]
                dis = abs(get[1] - box[j][1]) + abs(get[2] - box[j][2])

                if T >= dis :
                    if dp[j] != 0 :
                        temp = max(dp[j]+1, temp)
            else :
                T = get[0] - box[j][0]
                dis = abs(get[1] - box[j][1]) + abs(get[2] - box[j][2])

                if T >= dis :
                    temp = max(dp[j]+1, temp)                

        dp[i] = temp

    maxdp = max(dp[0:1001])

    for i in range(1001, n+1) :
        if i == 1001 :
            dp[i] = maxdp + 1
        else :
            dp[i] = dp[i-1] + 1

    print(dp[n])
