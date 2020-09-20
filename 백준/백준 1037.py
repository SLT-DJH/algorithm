N = int(input())

get = list(map(int, input().split()))

get.sort()

if len(get) % 2 == 0 :
    print(get[(len(get)//2) - 1] * get[(len(get)//2)])
else :
    print(get[(len(get)//2)] ** 2)
