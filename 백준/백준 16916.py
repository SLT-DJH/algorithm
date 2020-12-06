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
                i += 1
    return temptable

T = str(input())
P = str(input())

table = gettable(P)

t = len(T)
p = len(P)

i = 0
j = 0

check = 0

while i < t :
    if T[i] == P[j] :
        i += 1
        j += 1
    else :
        if j != 0 :
            j = table[j-1]
        else :
            i += 1
    
    if j == p :
        check = 1
        break

if check == 1 :
    print(1)
else :
    print(0)
