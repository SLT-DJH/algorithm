T = int(input())

for i in range(T) :
    N = int(input())
    line = list(map(int, input().split()))
    
    profit = 0

    for j in range(len(line)) :
        if j != len(line) - 1 :
            get = line[j]
            check = max(line[j+1:])
            if get < check :
                profit += check - get
    print("#{} {}".format(i+1, profit))
