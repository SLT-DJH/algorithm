def go(index, i, j, board, n) :
    if index == 0 :
        for k in range(j) :
            if board[i][k] == 1 :
                return False

        return True
    elif index == 1 :
        for k in range(j+1, n) :
            if board[i][k] == 1 :
                return False

        return True
    elif index == 2 :
        for k in range(i) :
            if board[k][j] == 1 :
                return False
        return True
    elif index == 3 :
        for k in range(i+1, n) :
            if board[k][j] == 1 :
                return False
        return True

def check(board, n) :
    answer = 0
    
    for i in range(n) :
        for j in range(n) :
            if board[i][j] == 1 :
                if i == 0 or i == n - 1 or j == 0 or j == n - 1 :
                    continue
                else :
                    x = i
                    y = j
                    ##left, right, top, bottom
                    checkbox = [j, n-1-j, i, n-1-i]
                    tempsum = 0

                    while True :
                        get = min(checkbox)

                        if get == n :
                            break

                        index = checkbox.index(get)

                        if go(index, i, j, board, n) :
                            tempsum = get
                            print(index, i, j, get)
                            break
                        else :
                            checkbox[index] = n

                    answer += tempsum

    return answer
                    

T = int(input())

for _ in range(T) :
    N = int(input())
    board = []
    for _ in range(N) :
        line = list(map(int, input().split()))
        board.append(line)

    print(check(board,N))
