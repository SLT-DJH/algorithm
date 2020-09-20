import sys
sys.setrecursionlimit(1000000)

def check(x, y, n, board) :
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if board[i][j] != board[x][y] :
                return False

    return True

def DFS(x, y, n, board) :
    global answer
    
    if check(x, y, n, board) :
        get = board[x][y]

        if get == -1 :
            answer[0] += 1
        elif get == 0 :
            answer[1] += 1
        elif get == 1 :
            answer[2] += 1
    else :
        m = n // 3

        for i in range(3) :
            for j in range(3) :
                DFS(x + (i * m), y + (j * m), m, board)
    

N = int(input())

board = []

for _ in range(N) :
    line = list(map(int, input().split()))
    board.append(line)

answer = [0 , 0, 0]
## -1, 0, 1
    
DFS(0, 0, N, board)

for num in answer :
    print(num)
