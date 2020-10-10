T = int(input())

for _ in range(T) :
    n, k = map(int, input().split())

    line = list(map(int, input().split()))

    get = len(set(line))

    if k == 1 :
        if get == 1 :
            print(1)
        else :
            print(-1)
    else :
        if get == k :
            print(1)
        else :
            print(2)
