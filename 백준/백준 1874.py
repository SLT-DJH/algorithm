a = int(input())

todolist = []

point = 0
num = 1

numlist = []
answer = []

for i in range(a) :
    get = int(input())

    todolist.append(get)

while True :
    getpoint = todolist[point]

    numlist.append(num)
    answer.append("+")

    if num == getpoint :
        numlist.pop()
        answer.append("-")

        point += 1

        if numlist != [] :
            
            while True :
                check = numlist.pop()
                temppoint = todolist[point]

                if check == temppoint :
                    answer.append("-")
                    point += 1
                else :
                    numlist.append(check)
                    break

                if numlist == [] :
                    break

            num += 1
        
        else :
            num += 1
    else :
        num += 1

    if num > a :
        break

if numlist == [] :
    for i in answer :
        print(i)
else :
    print('NO')
