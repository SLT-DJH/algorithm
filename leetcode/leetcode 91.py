get = input()

dp = [1]

for i in range(len(get)) :
    if i == 0 :
        dp.append(1)
    else :
        newdp = 0
        
        getdp1 = dp[i]
        
        getdp2 = dp[i-1]

        checknum1 = get[i]

        checknum2 = get[i-1:i+1]

        if int(checknum1) == 0 :
            if int(checknum2) <= 26 and int(checknum2) >= 10 :
                newdp += getdp2
        else :
            if int(checknum2) <= 26 and int(checknum2) >= 10 :
                newdp += getdp1
                newdp += getdp2
            else :
                newdp += getdp1

        dp.append(newdp)
        print(dp)

print(dp)
