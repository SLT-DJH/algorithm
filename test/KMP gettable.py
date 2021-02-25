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
