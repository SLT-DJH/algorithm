N, M = map(int, input().split())

board = []

for _ in range(N) :
    box = []
    line = input()

    for i in line :
        box.append(i)

    board.append(box)

checkboard = [[0] * M for _ in range(N)]

position = [[0,0]]

count = 0

while checkboard[N-1][M-1] == 0 :
    check = []
    
    for i in position :
        if checkboard[i[0]][i[1]] == 0 :
            checkboard[i[0]][i[1]] = 1
            check.append(i)

    for i in check :
                 
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]

        for j in range(4) :
            cx = i[1] + dx[j]
            cy = i[0] + dy[j]

            if 0 <= cx < M and 0 <= cy < N and board[cy][cx] == '1' and checkboard[cy][cx] != 1 :
                position.append([cy, cx])
    count += 1

print(count)

            




