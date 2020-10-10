from itertools import combinations

def countzero(temp) :
    zerosum = 0

    for i in temp :
        zerosum += i.count(0)

    return zerosum

def checkinfect(position, board, N, M, infect) :
    temp = []

    for i in range(N) :
        box = []
        for j in range(M) :
            box.append(board[i][j])
        temp.append(box)

    for i in range(3) :
        temp[position[i][0]][position[i][1]] = 1

    getinfect = []

    for i in infect :
        getinfect.append(i)

    while getinfect :
        n = getinfect.pop(0)

        infectbox = []

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for i in range(4) :
            cx = n[1] + dx[i]
            cy = n[0] + dy[i]

            if 0 <= cx < M and 0 <= cy < N and temp[cy][cx] != 1 and temp[cy][cx] != 2:
                infectbox.append([cy, cx])
                temp[cy][cx] = 2

        getinfect.extend(infectbox)

    return countzero(temp)

N, M = map(int, input().split())

board = []

zero = []
infect = []

for i in range(N) :
    line = list(map(int, input().split()))

    for j in range(len(line)) :
        if line[j] == 0 :
            zero.append([i, j])
        elif line[j] == 2 :
            infect.append([i, j])

    board.append(line)

candidate = list(combinations(zero, 3))

best = 0

for i in candidate :
    
    take = checkinfect(i, board, N, M, infect)

    if take > best :
        best = take

print(best)
