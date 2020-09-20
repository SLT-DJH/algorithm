def get25(num) :
    two = 0
    five = 0

    while num != 1 :
        if num % 2 == 0 :
            two += 1
            num = num // 2
        elif num % 5 == 0 :
            five += 1
            num = num // 5
        else :
            num = num // num

    return two, five

N = int(input())

dp = [[0,0] for _ in range(501)]

for i in range(2, 501) :
    a = dp[i-1][0]
    b = dp[i-1][1]

    ta , tb = get25(i)

    ta = ta + a
    tb = tb + b

    dp[i] = [ta, tb]

two = dp[N][0]
five = dp[N][1]

if two < five :
    print(two)
else :
    print(five)
