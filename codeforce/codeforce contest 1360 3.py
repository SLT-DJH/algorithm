t = int(input())

for _ in range(t) :
    n = int(input())

    a = list(map(int, input().split()))

    a.sort()

    yescount = 0
    
    for i in range(len(a)) :
        if yescount == 0 :
            for j in range(i+1, len(a)) :
                if a[j] - a[i] == 1 :
                    yescount = 1
                    print('YES')
                    break
                else :
                    break
    
    for i in range(len(a)) :
        if yescount == 0 :
            for j in range(i+1, len(a)) :
                if a[i] % 2 == a[j] % 2 :
                    yescount = 1
                    print('YES')
                    break

    if yescount == 0 :
        print('NO')
