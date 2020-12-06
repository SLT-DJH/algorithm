def gettable(temp) :
    m = len(temp)

    temptable = [0] * m

    count = 0

    i = 1

    while i < m :
        if temp[count] == temp[i] :
            count += 1
            temptable[i] = count

            i += 1
        else :
            if count != 0 :
                while count > 0 and temp[count] != temp[i] :
                    count = temptable[count-1]
            else :
                i += 1

    return temptable

S = str(input())

best = 0

for i in range(len(S)) :
    temp = S[i:]
    
    if len(temp) < best :
        break
    else :

        table = gettable(temp)

        best = max(best, max(table))

print(best)
