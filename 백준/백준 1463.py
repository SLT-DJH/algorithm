dp = [0 for i in range((10**6) + 1)]

for i in range(10**6) :
    num = i+1
    
    if num == 1 :
        dp[num] = 0
    elif num == 2 :
        dp[num] = 1
    elif num == 3 :
        dp[num] = 1
    else :
        if num % 3 == 0 and num % 2 == 0 :
            dp3 = 1 + dp[num//3]
            dp2 = 1 + dp[num//2]

            if dp3 < dp2 :
                dp[num] = dp3
            else :
                dp[num] = dp2
        elif num % 3 == 0 :
            dp3 = 1 + dp[num//3]
            dp1 = 1 + dp[num-1]

            if dp1 < dp3 :
                dp[num] = dp1
            else :
                dp[num] = dp3
        elif num % 2 == 0 :
            dp2 = 1 + dp[num//2]
            dp1 = 1 + dp[num - 1]

            if dp1 < dp2 :
                dp[num] = dp1
            else :
                dp[num] = dp2
        else :
            dp1 = 1 + dp[num-1]

            dp[num] = dp1

a = int(input())

print(dp[a])
