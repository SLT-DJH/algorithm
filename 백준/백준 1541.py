getlist = []
checklist = []

line = input()

for i in line :
    if i == "+" :
        checklist.append("+")
    elif i == "-" :
        checklist.append("-")

line = line.split("+")

for i in range(len(line)) :
    line[i] = line[i].split("-")


for i in range(len(line)) :
    for j in range(len(line[i])) :
        getlist.append(line[i][j])

answer = 0
minus = 0

for i in range(len(getlist)) :
    if i == 0 :
        answer += int(getlist[i])
    else :
        if minus == 0 :
            if checklist[i-1] == "+" :
                answer += int(getlist[i])
            elif checklist[i-1] == "-" :
                minus = 1
                answer = answer - int(getlist[i])
        else :
            if checklist[i-1] == "+" :
                answer = answer - int(getlist[i])
            elif checklist[i-1] == "-" :
                answer = answer - int(getlist[i])

print(answer)
