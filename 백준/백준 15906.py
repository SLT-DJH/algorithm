from collections import deque

def normalBFS(start, end, dx, dy, temp):
    count = 0

    queue = deque([start])

    temp[start[0] - 1][start[1] - 1] = 1
    
    if temp[end[0]-1][end[1]-1] == 1 :
        return count

    while True :
        tempqueue = []

        while queue:
            y, x = queue.popleft()

            for i in range(4):
                cx = x - 1 + dx[i]
                cy = y - 1 + dy[i]

                if 0 <= cx < N and 0 <= cy < N and temp[cy][cx] != 1:
                    tempqueue.append((cy + 1, cx + 1))
                    temp[cy][cx] = 1

        count += 1

        if temp[end[0] - 1][end[1] - 1] == 1:
            break

        if tempqueue == []:
            break

        queue.extend(tempqueue)

    return count


def specialBFS(start, end, dx, dy, stemp, warp, t, board, N):
    count = t

    queue = deque([start])

    stemp[start[0] - 1][start[1] - 1] = 1
    
    if stemp[end[0]-1][end[1]-1] == 1 :
        return count

    while True:
        tempqueue = []

        while queue:
            y, x = queue.popleft()
            
            for i in range(4) :
                if i == 0 :
                    for j in range(x-1, N) :
                        if board[y-1][j] == "#" and stemp[y-1][j] != 1:
                            stemp[y-1][j] = 1
                            tempqueue.append((y,j+1))
                            break
                if i == 1 :
                    for j in range(y-1, N) :
                        if board[j][x-1] == "#" and stemp[j][x-1] != 1:
                            stemp[j][x-1] = 1
                            tempqueue.append((j+1, x))
                            break
                if i == 2 :
                    for j in range(0, x) :
                        if board[y-1][j] == "#" and stemp[y-1][j] != 1:
                            stemp[y-1][j] = 1
                            tempqueue.append((y, j+1))
                            break
                if i == 3 :
                    for j in range(0, y) :
                        if board[j][x-1] == "#" and stemp[j][x-1] != 1:
                            stemp[j][x-1] = 1
                            tempqueue.append((j+1, x))
                            break

            for i in range(4):
                cx = x - 1 + dx[i]
                cy = y - 1 + dy[i]

                if 0 <= cx < N and 0 <= cy < N and stemp[cy][cx] != 1 :
                    tempqueue.append((cy + 1, cx + 1))
                    stemp[cy][cx] = 1

        count += 1

        for k in stemp :
            print(k)

        print("")
            

        if stemp[end[0] - 1][end[1] - 1] == 1:
            break

        if tempqueue == []:
            break

        queue.extend(tempqueue)

    return count

N, t, r, c = map(int, input().split())

board = []

for i in range(N):
    mlist = []

    get = str(input())

    for j in get :
        mlist.append(j)

    board.append(mlist)

warp = []

for i in range(N):
    for j in range(N):
        if board[i][j] == "#":
            warp.append((i + 1, j + 1))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

temp = [[0 for i in range(N)] for i in range(N)]
stemp = [[0 for i in range(N)] for i in range(N)]

a = normalBFS((1, 1), (r, c), dx, dy, temp)
b = specialBFS((1, 1), (r, c), dx, dy, stemp, warp, t, board, N)

print(min(a,b))
