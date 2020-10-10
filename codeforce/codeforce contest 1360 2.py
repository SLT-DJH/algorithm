t = int(input())

for _ in range(t) :
    n = int(input())

    line = list(map(int, input().split()))

    best = 1000

    line.sort()

    for i in range(len(line)) :
        if i != len(line) - 1 :
            get = abs(line[i] - line[i+1])

            if get < best :
                best = get

    print(best)
