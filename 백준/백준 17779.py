def makeboard(N, start, dx, dy) :

    temp = [[0 for _ in range(N)] for _ in range(N)]

    # 5번구역 먼저 설정

    x = start[0]
    y = start[1]
    
    yleftdi = 0
    yleft = start[1]
    yrightdi = 0
    yright = start[1]

    while x <= start[0]+dx+dy :
        for i in range(yleft, yright+1) :
            temp[x][i] = 5

        if yleftdi == 0 :
            if yleft - 1 == y - dx :
                yleftdi = 1
                yleft -= 1
            else :
                yleft -= 1
        else :
            yleft += 1

        if yrightdi == 0 :
            if yright + 1 == y + dy :
                yrightdi = 1
                yright += 1
            else :
                yright += 1
        else :
            yright -= 1

        x += 1

    for i in range(N) :
        for j in range(N) :
            if temp[i][j] == 0 :
                if i < start[0] + dx and j <= start[1] :
                    temp[i][j] = 1
                elif i <= start[0] + dy and j > start[1] :
                    temp[i][j] = 2
                elif i >= start[0] + dx and j < start[1] - dx + dy :
                    temp[i][j] = 3
                elif i > start[0] + dy and j >= start[1] - dx + dy :
                    temp[i][j] = 4
    return temp

def calcul(tempboard, board, N) :
    teul = [0] * 5
    
    for i in range(N) :
        for j in range(N) :
            if tempboard[i][j] == 1 :
                teul[0] += board[i][j]
            elif tempboard[i][j] == 2 :
                teul[1] += board[i][j]
            elif tempboard[i][j] == 3 :
                teul[2] += board[i][j]
            elif tempboard[i][j] == 4 :
                teul[3] += board[i][j]
            elif tempboard[i][j] == 5 :
                teul[4] += board[i][j]

    return max(teul) - min(teul)

def allboard(board, N) :
    count = 1000000
    
    for i in range(N) :
        if i != N-1 and i != N-2 :
            for j in range(N) :
                if j != 0 and j != N-1 :
                    start = (i, j)

                    dx = 1
                    dy = 1

                    while j-dx >= 0 and j+dy <= N-1 and i+dx+dy <= N-1 :

                        tempboard = makeboard(N, start, dx, dy)
                        tempcount = calcul(tempboard, board, N)

                        count = min(count, tempcount)

                        if j+dy == N-1 or i+dx+dy == N-1:
                            dx += 1
                            dy = 1
                        else :
                            dy += 1

    return count
            

N = int(input())

board = []

for _ in range(N) :
    mlist = list(map(int, input().split()))

    board.append(mlist)

answer = allboard(board, N)

print(answer)

