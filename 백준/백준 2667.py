def change(board, i, j, start, N, count) :
    board[i][j] = start

    count.append(1)
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for k in range(4) :
        cx = dx[k] + i
        cy = dy[k] + j

        if cx >= 0 and cx < N and cy >= 0 and cy < N :
            if board[cx][cy] == 1 :
                change(board, cx, cy, start, N, count)
            
def DFS(board, start, N) :

    count = []
    
    for i in range(N) :
        for j in range(N) :
            if board[i][j] == 1 :
                change(board, i, j, start, N, count)

                final.append(sum(count))

                count = []

                start += 1

N = int(input())

board = []

for _ in range(N) :
    line = input()

    box = []

    for i in line :
        box.append(int(i))

    board.append(box)

final = []

DFS(board, 2, N)

final.sort()

print(len(final))
for i in final :
    print(i)
