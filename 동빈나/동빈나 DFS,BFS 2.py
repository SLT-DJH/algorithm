from collections import deque

def BFS(y, x, board, N, M) :
    queue = deque([[y,x]])

    count = 1

    board[y][x] = 0
    
    while True :
        if board[N-1][M-1] == 0 :
            return count
        
        count += 1

        box = deque([])
        
        while queue :
            v = queue.popleft()

            dx = [1, -1, 0, 0]
            dy = [0, 0, -1, 1]

            for i in range(4) :
                cx = v[0] + dx[i]
                cy = v[1] + dy[i]

                if 0 <= cx < M and 0 <= cy < N and board[cy][cx] != 0 :
                    box.append([cy, cx])
                    board[cy][cx] = 0

        queue.extend(box)
        

N, M = map(int, input().split())

board = []

for _ in range(N) :
    box = []
    
    line = input()

    for i in line :
        box.append(int(i))

    board.append(box)

print(BFS(0, 0, board, N, M))
