def gettable(W) :
    w = len(W)
    
    temptable = [0] * w

    count = 0

    i = 1

    while i < w :
        if W[i] == W[count] :
            count += 1
            temptable[i] = count

            i += 1
        else :
            if count != 0 :
                while count > 0 and W[i] != W[count] :
                    count = temptable[count-1]
            else :
                i += 1

    return temptable

def KMP(S, temp, table) :
    count = 0
    
    x = 0
    y = 0

    while x < len(S) :
        if S[x] == temp[y] :
            x += 1
            y += 1
        else :
            if y != 0 :
                while y > 0 and S[x] != temp[y] :
                    y = table[y-1]
            else :
                x += 1

        if y == len(temp) :
            count += 1
            y = table[y-1]

        if count == 2 :
            break

    if count == 1 :
        return True
    else :
        return False

N = int(input())

for _ in range(N) :

    graph = {}
    
    A = str(input())
    W = str(input())
    S = str(input())

    table = gettable(W)

    m = len(A)
    l = len(W)
    n = len(S)

    for i in range(m) :
        if A[i] not in graph :
            graph[A[i]] = []

            count = 0

            now = A.index(A[i])

            while count != m :
                if now <= m - 1 :
                    
                    graph[A[i]].append(A[now])

                    now += 1
                else :
                    graph[A[i]].append(A[now-m])

                    now += 1

                count += 1

    answer = []

    for i in range(m) :     
        temp = ""

        for j in W :
            temp += graph[j][i]

        if KMP(S, temp, table) :
            if i != 0 :
                answer.append(i)
            else :
                answer.append(0)

    if answer == [] :
        print("no solution")
    elif len(answer) == 1 :
        print("unique: " + str(answer[0]))
    else :
        pri = "ambiguous: "

        for i in sorted(answer) :
            pri += str(i) + " "

        print(pri)
        
                
        
