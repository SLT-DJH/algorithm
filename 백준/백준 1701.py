def gettable(P) :
    m = len(P)

    temptable = [0] * m

    count = 0

    i = 1

    while i < m :
        if P[i] == P[count] :
            count += 1
            temptable[i] = count
            
            i += 1
        else :
            if count != 0 :
                count = temptable[count-1]
            else :
                temptable[i] = 0
                i +=1
        
    return temptable

get = str(input())
M = len(get)

nowlen = M - 1

answer = 0

while nowlen != 0 :
    count = 0

    end = nowlen - 1

    for i in range(M-nowlen+1) :
        temp = get[i:end+1]
        table = gettable(temp)

        j = 0
        k = 0

        while j < M and count != 2:
            if get[j] == temp[k] :
                j += 1
                k += 1
            else :
                if k != 0 :
                    k = table[k-1]
                else :
                    j += 1

            if k == nowlen :
                count += 1
                k = table[k-1]

        end += 1

        if count == 2 :
            break
        else :
            count = 0

    if count == 2 :
        answer = nowlen
        break
    else :
        nowlen -= 1

print(answer)
            

        
