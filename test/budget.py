import math

while True :

    N = int(input())

    M = input()
    M = list(map(int, M.split()))
    M.sort()

    box = []

    for i in range(N) :
        box.append(M[i])

    budget = int(input())

    if sum(box) <= budget :
        print(max(box))
    else :
        start = 0
        limit = M[len(M)-1]
        mid = math.floor((start + limit) / 2)
        print(start, mid, limit)
        while  sum(box) != budget and mid != start and mid != limit:
            for i in range(N) :
                if M[i] < mid :
                    box[i] = M[i]
                else :
                    box[i] = mid
            print(box)
            if sum(box) < budget :
                start = mid
                mid = math.floor((start + limit) / 2)
                print(start, mid, limit)
            else :
                limit = mid
                mid = math.floor((start + limit) / 2)
                print(start, mid, limit)
        if sum(box) > budget :
            print(max(box)-1)
        else :
            print(max(box))
