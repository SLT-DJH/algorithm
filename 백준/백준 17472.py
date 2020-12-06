import heapq

def bfs(i, j, board, now, dx, dy, M, N) :
    board[i][j] = now
    
    for k in range(4) :
        cx = j + dx[k]
        cy = i + dy[k]

        if cx >= 0 and cy >= 0 and cx < M and cy < N and board[cy][cx] != now and board[cy][cx] != 0:
            bfs(cy, cx, board, now, dx, dy, M, N) 


N, M = map(int, input().split())

board = []

for _ in range(N) :
    line = list(map(int, input().split()))

    board.append(line)

now = 2

islandbox = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 1 :
            bfs(i, j, board, now, dx, dy, M, N)
            islandbox.append(now)

            now += 1

m = len(islandbox)

position = [[] for i in range(m)]

for i in range(N) :
    for j in range(M) :
        if board[i][j] != 0 :
            check = board[i][j]

            position[islandbox.index(check)].append((i,j))

connect = []

check = [0] * m

for i in range(m) :
    start = islandbox[i]

    for j in range(i+1, m) :
        minlen = 1000000
        end = islandbox[j]

        for k in position[islandbox.index(start)] :
            for l in position[islandbox.index(end)] :
                if k[0] == l[0] :
                    if k[1] < l[1] :
                        x = k[1]
                        y = l[1]
                    else :
                        x = l[1]
                        y = k[1]

                    #x가 작은 y가 큰
                    countzero = 0
                    for z in range(x+1, y) :
                        if board[k[0]][z] != 0 :
                            countzero = 1
                            break

                    if countzero == 0 :        
                        temp = min(minlen, abs(k[1] - l[1]) - 1)

                        if temp != 1 :
                            minlen = temp                            

                if k[1] == l[1] :
                    if k[0] < l[0] :
                        x = k[0]
                        y = l[0]
                    else :
                        x = l[0]
                        y = k[0]

                    countzero = 0
                    for z in range(x+1, y) :
                        if board[z][k[1]] != 0 :
                            countzero = 1
                            break

                    if countzero == 0 :
                        temp = min(minlen, abs(k[0] - l[0]) - 1)

                        if temp != 1 :
                            minlen = temp

        if minlen != 1000000:
            heapq.heappush(connect, (minlen, start, end))

answer = 0

graph = {}

for i in range(m) :
    graph[islandbox[i]] = islandbox[i]

def find(x) :
    if graph[x] == x :
        return x
    else :
        p = find(graph[x])

        graph[x] = p
        return p

def union(x, y) :
    x, y = find(x), find(y)

    if x != y :
        if x < y :
            graph[x] = y
        else :
            graph[y] = x
            
checkend = 0

while connect :
    get = heapq.heappop(connect)

    temp = graph.values()

    if len(set(temp)) == 1 :
        checkend = 1
        break
    else :
        if find(get[1]) != find(get[2]) :
            answer += get[0]

            union(get[1], get[2])

            for i in range(m) :
                graph[islandbox[i]] = find(islandbox[i])

temp = graph.values()

if len(set(temp)) == 1 :
    checkend = 1

if checkend == 1 :
    print(answer)
else :
    print(-1)
        


    
