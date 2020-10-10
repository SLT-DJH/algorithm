def turnleft():
    global change
    
    change -= 1

    if change == -1 :
        change = 3

N, M = map(int, input().split())

A, B, d = map(int, input().split())

board = []

for _ in range(N) :
    line = list(map(int, input().split()))

    board.append(line)

start = d
change = d
back = 0

count = 1

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

x = B
y = A

board[y][x] = 2

while True :
    if back == 0 :
        cx = x + dx[change]
        cy = y + dy[change]

        if 0 <= cx < M-1 and 0 <= cy < N-1 :
            if board[cy][cx] == 1 or board[cy][cx] == 2:
                turnleft()

                if change == start :
                    back = 1
            else :
                board[cy][cx] = 2
                count += 1
                
                x = cx
                y = cy
                start = change
                change = start
        else :
            turnleft()
            if change == start :
                back = 1
    else :
        back = 0

        if start == 0 :
            y = y + 1
        elif start == 1 :
            x = x - 1
        elif start == 2 :
            y = y - 1
        elif start == 3 :
            x = x + 1

        if board[y][x] == 1 :
            break

print(count)
            
