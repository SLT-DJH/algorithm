def prim() :
    global total
    
    if visited == [] :
        visited.append(1)

        movable = []

        for i in connect[1] :
            movable.append(i)

        temptotal = 0

        move = 0

        for i in movable :
            if temptotal == 0 :
                temptotal = cost[1][i]
                move = i
            else :
                if temptotal > cost[1][i] :
                    temptotal = cost[1][i]
                    move = i
        visited.append(move)
        total += temptotal

        connect[1].remove(move)
        connect[move].remove(1)
        
    else :
        temptotal = 0

        start = 0

        move = 0
        
        for i in visited :
            for j in connect[i] :
                if j in visited :
                    continue
                else :
                    if temptotal == 0 :
                        temptotal = cost[i][j]
                        start = i
                        move = j
                    else :
                        if temptotal > cost[i][j] :
                            temptotal = cost[i][j]
                            start = i
                            move = j
        visited.append(move)
        total += temptotal

        connect[start].remove(move)
        connect[move].remove(start)

N = int(input())

M = int(input())

cost = []

connect = []

for i in range(N+1) :
    box = []
    for j in range(N+1) :
        box.append(0)
    cost.append(box)
    
for i in range(N+1) :
    box = []
    connect.append(box)

for i in range(M) :
    line = input()
    line = list(map(int, line.split()))

    a = line[0]
    b = line[1]
    c = line[2]

    cost[a][b] = c
    cost[b][a] = c

    connect[a].append(b)
    connect[b].append(a)

visited = []

total = 0

while len(visited) != N :
    prim()

print(total)
