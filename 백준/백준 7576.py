def checkall(checkboard, N, M) :
    for i in range(N) :
        for j in range(M) :
            if checkboard[i][j] == 0 :
                return False

    return True

M, N = map(int, input().split())

board = []

for _ in range(N) :
    line = list(map(int, input().split()))

    board.append(line)

count = 0

checkboard = [[0] * M for _ in range(N)]

deque = []

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 1 :
            deque.append([i,j])
        elif board[i][j] == -1 :
            checkboard[i][j] = 1

while deque :
    temp = []

    for _ in range(len(deque)) :
        n = deque.pop(0)

        if checkboard[n[0]][n[1]] != 1 :
            checkboard[n[0]][n[1]] = 1

            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]

            box = []

            for i in range(4) :
                cx = n[1] + dx[i]
                cy = n[0] + dy[i]

                if 0 <= cx < M and 0 <= cy < N and checkboard[cy][cx] != 1 :
                    box.append([cy,cx])

            temp.extend(box)
    deque = temp

    count += 1
    
if checkall(checkboard, N, M) :
    print(count - 1)
else :
    print(-1)
