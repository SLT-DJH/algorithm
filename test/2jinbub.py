def jinbub(number) :
    box = []
    while number != 1 :
        if number % 2 == 0 :
            box.append(0)
            number = number // 2 
        else :
            box.append(1)
            number = number // 2
    box.append(1)
    return box
        
        

T = int(input())

for i in range(T) :
    a = int(input())
    answerbox = jinbub(a)
    answer = ''
    for j in range(len(answerbox)) :
        if answerbox[j] == 1 :
            answer = answer + str(j) + ' '
        else :
            continue
    print(answer)
