n = int(input())

numlist = []

for i in range(n) :
    numlist.append(i+1)

while True :
    if len(numlist) == 1 :
        print(numlist[0])
        break
    
    check = len(numlist)
    
    tempnum = []

    for i in range(len(numlist)) :
        if (i+1) % 2 == 0 :
            tempnum.append(numlist[i])

    if len(tempnum) == 1 :
        print(tempnum[0])
        break

    if check % 2 == 1 :
        tempnum.append(tempnum[0])

        tempnum = tempnum[1:]

    numlist = tempnum

    
    
