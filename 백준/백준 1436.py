def isnum(num) :
    get = str(num)

    for i in range(len(get)-2) :
        if get[i] == "6" and get[i+1] == "6" and get[i+2] == "6" :
            return True

    return False

while True :
    N = int(input())

    count = 666
    answer = 0

    while N != 0 :
        if isnum(count) :
            answer = count
            N = N - 1

        count += 1

    print(answer)
        
