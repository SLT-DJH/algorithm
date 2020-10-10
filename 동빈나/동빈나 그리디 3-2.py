N, K = map(int, input().split())

count = 0

while N != 1 :
    get = N // K
    take = N - (get * K)

    if get == 0 :
        count += (take - 1)
        break
    else :
        count += take

        N = get

        count += 1

print(count)
