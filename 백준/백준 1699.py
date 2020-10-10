N = int(input())

dp = [0 for i in range(N+1)]

for i in range(1, len(dp)) :
    get = int(i ** 0.5)
    check = i / get

    if get == check :
        dp[i] = 1
    else :
        if get-1 != 0 :
            best = 1000000
            
            for j in range(get, 0, -1) :
                temp = dp[j**2] + dp[i - (j**2)]

                if temp < best :
                    best = temp
                
            dp[i] = best
        else :
            dp[i] = dp[get**2] + dp[i-(get**2)]

print(dp[N])
