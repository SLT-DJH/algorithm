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
            

T = str(input())
P = str(input())

answer = []

table = gettable(P)

j = 0
i = 0

m = len(T)
n = len(P)

while i < m :
    if T[i] == P[j] :
        i += 1
        j += 1
    else :
        if j != 0 :
            j = table[j-1]
        else :
            i += 1

    if j == n :
        answer.append(i - n + 1)
        j = table[j-1]

print(len(answer))

for i in answer :
    print(str(i), end=" ")
