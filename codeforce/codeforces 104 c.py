t = int(input())

for _ in range(t) :
    n = int(input())

    box = [0] * (n-1)

    mid = (n-1) // 2

    if n % 2 == 0 :
        
        for i in range(len(box)) :
            if i < mid :
                box[i] = 1
            elif i == mid :
                box[i] = 0
            else :
                box[i] = -1
    else :
        for i in range(len(box)) :
            if i < mid :
                box[i] = 1
            else :
                box[i] = -1

    answer = []

    now = n-1

    while now != 0 :
        for i in range(now) :
            answer.append(box[i])

        now -= 1

    for i in answer :
        print(i, end=" ")

        
            
