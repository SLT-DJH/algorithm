def change(board, a, b, M, N) :
    board[b][a] = 2

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4) :
        cx = a + dx[i]
        cy = b + dy[i]

        if cx >= 0 and cy >= 0 and cx < M and cy < N :
            if board[cy][cx] == 1 :
                change(board, cx, cy, M, N)
                return

    

def DFS(board, M, N) :
    count = 0
    for i in range(N) :
        for j in range(M) :
            if board[i][j] == 1 :
                change(board, j, i, M, N)
                count += 1

    return count

T = int(input())

for _ in range(T) :
    M, N, a = map(int, input().split())

    board = [[0] * M for _ in range(N)]

    for i in range(a) :
        x, y = map(int, input().split())

        board[y][x] = 1
    
    print(DFS(board, M, N))
