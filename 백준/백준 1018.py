def getboard(position, board) :
    tempboard = []

    for i in range(8) :
        box = []
        for j in range(8) :
            box.append(board[i+position[0]][j+position[1]])

        tempboard.append(box)

    return tempboard

def checkboard(tempboard, final) :
    black = 0
    white = 0

    for i in range(2) :
        if i == 0 : #black ['B','W']
            for j in range(8) :
                for k in range(8) :
                    if j % 2 == 0 : # black['B','W']
                        if k % 2 == 0 : # black ['B','W'], 'B'
                            if tempboard[j][k] != 'B' :
                                black += 1
                        else : # black ['B','W'], 'W'
                            if tempboard[j][k] != 'W' :
                                black += 1
                    else : # black ['W', 'B']
                        if k % 2 == 0 : # black ['W', 'B'], 'W'
                            if tempboard[j][k] != 'W' :
                                black += 1
                        else : # black['W','B'] , 'B'
                            if tempboard[j][k] != 'B' :
                                black += 1
        else : # white ['W','B']
            for j in range(8) :
                for k in range(8) :
                    if j % 2 == 0 : # white['W','B']
                        if k % 2 == 0 : # white ['W','B'], 'W'
                            if tempboard[j][k] != 'W' :
                                white += 1
                        else : # white ['W','B'], 'B'
                            if tempboard[j][k] != 'B' :
                                white += 1
                    else : # white ['B', 'W']
                        if k % 2 == 0 : # white ['B', 'W'], 'B'
                            if tempboard[j][k] != 'B' :
                                white += 1
                        else : # white ['B','W'] , 'W'
                            if tempboard[j][k] != 'W' :
                                white += 1

    if black < white :
        final.append(black)
    else :
        final.append(white)
                        
                

a = input()
a = list(map(int, a.split()))

N = a[0]
M = a[1]

n = N - 8
m = M - 8

board = []

for _ in range(N) :
    box = []

    line = input()

    for chess in line :
        box.append(chess)

    board.append(box)

final = []

for i in range(n+1) :
    for j in range(m+1) :
        take = getboard([i,j], board)

        checkboard(take, final)

print(min(final))
