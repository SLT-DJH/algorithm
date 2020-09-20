def is_good(num, po, board) :
    board[po[0]][po[1]] = num
    
    rowbox = []
    columnbox = []
    squarebox = []
    
    for j in range(9) :
        rowbox.append(board[po[0]][j])
        columnbox.append(board[j][po[1]])
        squarebox.append(board[(3*(po[0]//3)) + (j//3)][3*(po[0]%3)+(j%3)])

    print(rowbox)
    print(columnbox)
    print(squarebox)

    for k in range(9) :
        if rowbox.count(str(k+1)) > 1 or columnbox.count(str(k+1)) > 1 or squarebox.count(str(k+1)) > 1 :
            board[po[0]][po[1]] = "."
            return False

    return True

def is_square(num, po, board) :
    x = (3 * (po[0]//3)) + (po[1]//3)
    y = 3 * (po[0] % 3) + (po[1]%3)

    print(x,y)
    
    square = []

    for j in range(9) :
        square.append(board[(3*(po[0]//3)) + (j//3)][3*(po[0]%3)+(j%3)])

    square[y] = num

    print(square)

    for j in range(9) :
        if square.count(str(j+1)) > 1 :
            return False

    return True

board = [[".",".","9","7","4","8",".",".","."],
         ["7",".",".",".",".",".",".",".","."],
         [".","2",".","1",".","9",".",".","."],
         [".",".","7",".",".",".","2","4","."],
         [".","6","4",".","1",".","5","9","."],
         [".","9","8",".",".",".","3",".","."],
         [".",".",".","8",".","3",".","2","."],
         [".",".",".",".",".",".",".",".","6"],
         [".",".",".","2","7","5","9",".","."]]

print(is_square("2", [6,4], board))
