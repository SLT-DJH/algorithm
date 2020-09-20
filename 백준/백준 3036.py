def printget(take, num) :
    start = num

    while start != 1 :
        if take % start == 0 and num % start == 0 :
            take = take // start
            num = num // start
        else :
            start = start - 1

    return (str(take) + "/" + str(num))

N = int(input())

get = list(map(int, input().split()))

take = get[0]

for i in range(N) :
    if i == 0 :
        continue
    else :
        print(printget(take, get[i]))
