from itertools import permutations

N = input()

N = str(N)

box = []

for i in range(len(N)) :
    box.append(N[i])

permu = permutations(box, len(box))

permu = list(permu)

candidate = []

for i in range(len(permu)) :
    if permu[i][0] == '0' :
        continue
    else :
        candidate.append(permu[i])
        
answer = []

for i in range(len(candidate)) :
    get = ''
    for j in range(len(candidate[i])) :
        get += candidate[i][j]
    get = int(get)

    if get % 30 == 0 :
        answer.append(get)

if answer == [] :
    print(-1)
else :
    answer.sort()
    print(answer[len(answer) - 1])

