N = 3
M = 4
D = 2

archer = [0,1,3]

board = [[0,0,0,0],[0,0,0,0],[0,0,1,0]]


def BFS(board, start, D, N, M, get) :
    checkbreak = 0

    row = -1
    column = -1
    
    while start != D+1 :
        tempget = []

        for i in get :
            if checkbreak == 0 :
                if board[i[0]][i[1]] == 1 :
                    row = i[0]
                    column = i[1]
                    checkbreak = 1
                    break
                else :
                    dx = [-1, 0, 1]
                    dy = [0, -1, 0]

                    for j in range(3) :
                        cx = i[1] + dx[j]
                        cy = i[0] + dy[j]

                        if 0 <= cx < M and 0 <= cy < N and [cy,cx] not in tempget :
                            tempget.append([cy, cx])
        
        if checkbreak == 1 :
            break
        else :
            start += 1

            get = tempget

    return row, column

for i in range(3) :
    y, x = BFS(board, 1, D, N, M, [[N-1, archer[i]]])
    print(y, x)
