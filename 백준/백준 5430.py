from collections import deque

T = int(input())

for _ in range(T) :

    function = list(str(input()))

    N = int(input())

    temp = str(input())

    if N != 0 :

        numlist = deque(list(map(int, temp[1:len(temp)-1].split(","))))
    else :
        numlist = deque([])

    direction = 0
    error = 0

    for i in function :
        if i == "R" :
            if direction == 0 :
                direction = -1
            else :
                direction = 0
        elif i == "D" :
            if numlist == deque([]) :
                error = 1
                break
            else :
                if direction == -1 :
                    numlist.pop()
                else :
                    numlist.popleft()

    if error == 1 :
        print('error')
    else :
        if direction == 0 :
            answer = list(numlist)
        else :
            answer = list(numlist)[::-1]

        typing = ""

        for i in range(len(answer)) :
            if i != len(answer) -1 :
                typing += str(answer[i]) + ","
            else :
                typing += str(answer[i])

        print("[" + typing + "]")
            
                
            
