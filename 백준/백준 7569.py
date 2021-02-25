from collections import deque

M, N, H = map(int,input().split())

board = []

for i in range(H) :
    temp = []
    for j in range(N) :
        mlist = list(map(int, input().split()))

        temp.append(mlist)

    board.append(temp)

day = 0

#오른쪽, 하단, 왼쪽, 상단, 위, 아래
dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


queue = deque([])

for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if board[i][j][k] == 1 :
                queue.append([i,j,k])
                
tempqueue = []
    
while queue :
    z, y, x = queue.popleft()

    for d in range(6) :
        cx = x + dx[d]
        cy = y + dy[d]
        cz = z + dz[d]

        if 0 <= cx < M and 0 <= cy < N and 0 <= cz < H and board[cz][cy][cx] == 0 :
                tempqueue.append([cz, cy, cx])
                board[cz][cy][cx] = 1
                
    if queue == deque([]) :
        if tempqueue == [] :
            break
        else :
            queue.extend(tempqueue)

            tempqueue = []
        
            day += 1

nozero = 0

for i in range(H) :
    if nozero == 0 :
        for j in range(N) :
            if nozero == 0 :
                for k in range(M) :
                    if board[i][j][k] == 0 :
                        nozero = 1
                        break
            else :
                break
    else :
        break

if nozero == 0 :
    print(day)
else :
    print(-1)
