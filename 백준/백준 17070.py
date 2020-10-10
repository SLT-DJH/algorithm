N = int(input())

board = []

for _ in range(N) :
    line = list(map(int, input().split()))
  
    board.append(line)

boardcheck = []

for i in board :
    boardcheck.append(i)

check = []

for i in range(N) :
    box = []

    for j in range(N) :
        box.append([])

    check.append(box)

check[0][1].append(0)

get = 2

while get != N + 1 :
    for i in range(get) :
        for j in range(get) :
            if boardcheck[i][j] != 2 :
                if check[i][j] != [] :
                    for k in check[i][j] :
                        if k == 0 :
                            if j+1 < N and board[i][j+1] != 1:
                                check[i][j+1].append(0)

                            if i+1 < N and j+1 < N and board[i+1][j] != 1 and board[i][j+1] != 1 and board[i+1][j+1] != 1:
                                check[i+1][j+1].append(1)
                        elif k == 1 :
                            if j+1 < N and board[i][j+1] != 1:
                                check[i][j+1].append(0)

                            if i+1 < N and board[i+1][j] != 1:
                                check[i+1][j].append(2)

                            if i+1 < N and j+1 < N and board[i+1][j] != 1 and board[i][j+1] != 1 and board[i+1][j+1] != 1:
                                check[i+1][j+1].append(1)
                        elif k == 2 :
                            if i+1 < N and j+1 < N and board[i+1][j] != 1 and board[i][j+1] != 1 and board[i+1][j+1] != 1:
                                check[i+1][j+1].append(1)

                            if i+1 < N and board[i+1][j] != 1:
                                check[i+1][j].append(2)

                boardcheck[i][j] = 2

    get += 1

print(len(check[N-1][N-1]))
    
