from itertools import combinations

def BFS(temp, start, D, N, M, get) :
    checkbreak = 0

    row = -1
    column = -1
    
    while start != D+1 :
        tempget = []

        for i in get :
            if checkbreak == 0 :
                if temp[i[0]][i[1]] == 1 :
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
        

def isover(temp) :
    allsum = 0

    for i in temp :
        allsum += sum(i)

    if allsum == 0 :
        return True
    else :
        return False
    
def gamestart(archer, temp, N, M, D) :

    enemy = 0

    while True :
        archershoot = [0,0,0]

        changebox = []
        
        for i in range(3) :
            y, x = BFS(temp, 1, D, N, M, [[N-1, archer[i]]])

            if y != -1 :
                changebox.append([y, x])

        if changebox != [] :
            for i in changebox :
                if temp[i[0]][i[1]] == 1 :
                    enemy += 1
                    temp[i[0]][i[1]] = 0

        if isover(temp) :
            break
        
        new = [[0 for _ in range(M)]]

        temp.pop()

        temp = new + temp
        
    return enemy

N, M, D = map(int, input().split())

board = []

for _ in range(N) :
    line = list(map(int, input().split()))

    board.append(line)

archernum = [i for i in range(M)]

archerlist = list(combinations(archernum, 3))

final = []

for i in archerlist :
    temp = []
    
    for j in range(N) :
        numbox = []
        for k in range(M) :
            numbox.append(board[j][k])
        temp.append(numbox)
    
    final.append(gamestart(i, temp, N, M, D))

print(max(final))
