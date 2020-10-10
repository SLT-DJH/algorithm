t = int(input())

for _ in range(t) :
    n = int(input())

    board = []
    
    for i in range(n) :
        box = []
        
        get = input()

        for j in get :
            box.append(int(j))

        board.append(box)

    nocount = 0

    for i in range(n) :
        if nocount == 0 :
            for j in range(n) :
                if board[i][j] == 1 :
                    if j+1 < n :
                        if board[i][j+1] == 0 :
                            if i+1 < n :
                                if board[i+1][j] == 0 :
                                    print('NO')
                                    nocount = 1
                                    break
    if nocount == 0 :
        print('YES')
