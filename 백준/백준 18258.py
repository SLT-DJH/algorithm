a = int(input())

queue = []
answer = []

for i in range(a) :
    get = input()
    realget = get.split()
    
    if realget[0] == 'push' :
        queue.append(int(realget[1]))
    elif realget[0] == 'pop' :
        if queue == [] :
            answer.append(-1)
        else :
            answer.append(queue[0])
            queue = queue[1:]
    elif realget[0] == 'size' :
        answer.append(len(queue))
    elif realget[0] == 'empty' :
        if queue == [] :
            answer.append(1)
        else :
            answer.append(0)
    elif realget[0] == 'front' :
        if queue == [] :
            answer.append(-1)
        else :
            answer.append(queue[0])
    elif realget[0] == 'back' :
        if queue == [] :
            answer.append(-1)
        else :
            answer.append(queue[len(queue)-1])

for i in answer :
    print(i)
