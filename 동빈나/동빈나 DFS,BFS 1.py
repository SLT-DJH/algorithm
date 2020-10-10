from collections import deque

def BFS(y, x, board, N, M) :
    global count

    queue = deque([[y, x]])

    board[y][x] = 1

    while queue :
        v = queue.popleft()

        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4) :
            cx = v[1] + dx[i]
            cy = v[0] + dy[i]

            if 0 <= cx < M and 0 <= cy < N and board[cy][cx] != 1 :
                queue.append([cy, cx])
                board[cy][cx] = 1

    count += 1

N, M = map(int, input().split())

board = []

for _ in range(N) :
    box = []

    line = input()

    for i in line :
        box.append(int(i))

    board.append(box)

count = 0

for i in range(N) :
    for j in range(M) :
        if board[i][j] == 0 :
            BFS(i, j, board, N, M)

print(count)
