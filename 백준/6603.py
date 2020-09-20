from itertools import combinations 

def printanswer(a) :
    do = ''
    for i in range(len(a)) :
        get = a[i]
        for j in range(6) :
            do += str(a[i][j]) + ' '
        print(do)
        do = ''

answer = []

while True :
    box = []
    
    a = input()

    a = list(map(int, a.split()))

    k = a[0]

    del a[0]

    numbers = a

    if k == 0 :
        break
    else :
        combi = combinations(numbers, 6)
        combi = list(combi)
        for i in range(len(combi)) :
            box.append(combi[i])
        answer.append(box)

for i in range(len(answer)) :
    printanswer(answer[i])
    print('')
