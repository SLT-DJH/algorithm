a = input()

a = list(map(int, a.split()))

n = a[0]

k = a[1]

if n == 1 :
    print("<1>")
else :

    num = 1

    numlist = []

    answer = []

    for i in range(n) :
        numlist.append(i+1)


    for i in numlist :
        if num % k == 0 :
            answer.append(i)
            num += 1
        else :
            numlist.append(i)
            num += 1

    printanswer = ""

    for i in range(len(answer)) :
        if i == 0 :
            printanswer += "<"
            printanswer += str(answer[i])
            printanswer += ", "
        elif i == len(answer)-1 :
            printanswer += str(answer[i])
            printanswer += ">"
        else :
            printanswer += str(answer[i])
            printanswer += ", "

    print(printanswer)
