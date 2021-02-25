from collections import deque

M, N = map(int, input().split())

board = []

for i in range(N) :
    mlist = list(map(int, input().split()))

    board.append(mlist)


tempboard = []

goodlist = []
zerolist = []

for i in range(N) :
    tlist = []
    for j in range(M) :
        if board[i][j] == 1 :
            goodlist.append((j, i))
        elif board[i][j] == 0 :
            zerolist.append((j, i))
        tlist.append(board[i][j])
    tempboard.append(tlist)

if goodlist == [] :
    print(-1)
elif zerolist == [] :
    print(0)
else :

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    time = 0

    queue = deque()

    for i in goodlist :
        queue.append(i)

    temp = []

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            cx = x + dx[i]
            cy = y + dy[i]

            if 0 <= cx < M and 0 <= cy < N and board[cy][cx] == 0 :
                temp.append((cx, cy))
                board[cy][cx] = 1

        if queue == deque([]) :
            if temp != [] :
                time += 1
                queue.extend(temp)
                temp = []
            else :
                break

    pause = 0

    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 0 :
                pause = 1

    if pause == 1 :
        print(-1)
    else :
        print(time)
