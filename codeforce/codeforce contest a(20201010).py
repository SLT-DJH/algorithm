t = int(input())

for _ in range(t) :
    n = int(input())

    numlist = list(map(int, input().split()))

    getall = sum(numlist)
    
    if getall == 0 :
        print("NO")
    elif getall < 0 :
        print("YES")
        temp = sorted(numlist)
        for i in range(len(temp)) :
            if i != len(temp) - 1 :
                print(temp[i], end = " ")
            else :
                print(temp[i])
    elif getall > 0 :
        print("YES")
        temp = sorted(numlist, reverse = True)
        for i in range(len(temp)) :
            if i != len(temp) - 1 :
                print(temp[i], end = " ")
            else :
                print(temp[i])
        

    
        
