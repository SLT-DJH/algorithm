n = int(input())

box = []

for _ in range(n) :
    box.append(int(input()))

dp = [0] * n

if n < 3 :
    if n == 1 :
        print(box[0])
    elif n == 2 :
        print(sum(box))
else :

    for i in range(3) :
        if i == 0 :
            dp[i] = box[i]
        elif i == 1 :
            dp[i] = box[i-1] + box[i]
        else :
            dp[i] = max(box[i]+ box[i-1], box[i]+box[i-2], dp[i-1])

    for i in range(3, n) :
        dp[i] = max(dp[i-1], dp[i-2] + box[i], dp[i-3] + box[i] + box[i-1])

    print(dp[-1])
