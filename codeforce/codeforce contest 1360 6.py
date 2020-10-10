t = int(input())

for _ in range(t) :
    n, m = map(int, input().split())

    board = []

    for i in range(n) :
        box = []
        word = input()

        for j in word :
            box.append(j)

        board.append(box)

    print(board)

        


    
