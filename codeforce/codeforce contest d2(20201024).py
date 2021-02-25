t = int(input())

for _ in range(t) :
    n = int(input())

    line = list(map(int, input().split()))

    tempset = list(set(line))

    if len(tempset) == 1 :
        print("NO")
    else :
        check = [0] * n

        check[0] = 1

        box = []

        get = 0

        for i in range(n) :
            if line[i] != line[get] :
                elseget = i

                box.append([get+1, i+1])
                check[i] = 1

        for i in range(n) :
            if check[i] == 0 :
                box.append([elseget+1, i+1])
                check[i] = 1

        print("YES")

        for i in box :
            print(i[0], i[1])
