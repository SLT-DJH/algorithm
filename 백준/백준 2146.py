from collections import deque

N = int(input())

board = []

for _ in range(N) :
    mlist = list(map(int, input().split()))

    board.append(mlist)

bridgeboard = [[0 for _ in range(N)] for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

start = 2

def colorland(y, x, start) :
    global board
    global N
    global dx
    global dy
    
    queue = deque([(y , x)])

    board[y][x] = start

    temp = []

    while queue :
        vy, vx = queue.popleft()

        for i in range(4) :
            cx = vx + dx[i]
            cy = vy + dy[i]

            if 0 <= cx < N and 0 <= cy < N and board[cy][cx] == 1 :
                board[cy][cx] = start
                temp.append((cy, cx))

        if queue == deque([]) :
            queue.extend(temp)
            temp = []

for i in range(N) :
    for j in range(N) :
        if board[i][j] == 1 :
            colorland(i, j, start)
            start += 1

bridge = 1000000

allend = []

def countbridge(y, x, now) :
    global board
    global N
    global dx
    global dy
    global allend

    queue = deque([(y,x)])
    bridgeboard[y][x] = 1

    temp = []
    endpoint = []

    while queue :
        vy, vx = queue.popleft()

        count = 0

        for i in range(4) :
            cx = vx + dx[i]
            cy = vy + dy[i]

            if 0 <= cx < N and 0 <= cy < N and board[cy][cx] != 0 and bridgeboard[cy][cx] == 0 :
                bridgeboard[cy][cx] = 1
                temp.append((cy, cx))

            if 0 <= cx < N and 0 <= cy < N and board[cy][cx] == 0 :
                count += 1
                
        if count != 0 :
            endpoint.append((vy,vx))

        if queue == deque([]) :
            queue.extend(temp)
            temp = []

    allend.append(endpoint)

for i in range(N) :
    for j in range(N) :
        if board[i][j] != 0 and bridgeboard[i][j] == 0:
            now = board[i][j]
            countbridge(i, j, now)

for i in range(len(allend)-1) :
    for j in range(i+1, len(allend)) :
        prom = allend[i]
        to = allend[j]

        for k in range(len(prom)) :
            ky, kx = prom[k]

            for l in range(len(to)) :
                ly, lx = to[l]

                bridge = min(bridge, abs(ky-ly) + abs(kx-lx) - 1)

print(bridge)
