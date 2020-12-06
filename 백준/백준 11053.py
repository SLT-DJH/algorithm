n = int(input())

numlist = list(map(int, input().split()))

dp = [0] * n

for i in range(n) :
    if i == 0 :
        dp[0] = 1
    else :
        count = 0
        temp = numlist[:i]
        temp = list(set(temp))
        for j in range(len(temp)) :
            if temp[j] < numlist[i] :
                count += 1

        count += 1
        dp[i] = count

print(max(dp))
