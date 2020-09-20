def is_row(num, po, board) :
    x = po[0]
    y = po[1]
    
    row = []

    for j in range(9) :
        row.append(board[x][j])

    row[y] = num

    for j in range(9) :
        if row.count(str(j+1)) > 1 :
            return False

    return True

def is_column(num, po, board) :
    x = po[1]
    y = po[0]
    
    column = []

    for j in range(9) :
        column.append(board[j][x])

    column[y] = num

    for j in range(9) :
        if column.count(str(j+1)) > 1 :
            return False

    return True

def is_square(num, po, board) :
    square = []

    x = (3*(po[0]//3)) + (po[1]//3)

    for j in range(9) :
        square.append(board[(3*(x//3)) + (j//3)][3*(x%3)+(j%3)])

    y = (3*(po[0]%3)) + (po[1] % 3)

    square[y] = num

    for j in range(9) :
        if square.count(str(j+1)) > 1 :
            return False

    return True

def DFS(N, current_position, current_candidate, final, checkzero, board) :
    if current_position == N :
        final.append(current_candidate[:])
        return True

    for i in range(9) :
        if is_row(str(i+1), checkzero[current_position], board) and is_column(str(i+1), checkzero[current_position], board) and is_square(str(i+1), checkzero[current_position], board) :
            current_candidate.append(str(i+1))
            board[checkzero[current_position][0]][checkzero[current_position][1]] = str(i+1)
            if DFS(N, current_position + 1, current_candidate, final, checkzero, board) :
                return True
            board[checkzero[current_position][0]][checkzero[current_position][1]] = "."
            current_candidate.pop()
            
def printsdoku(somelist) :
    blank = ""
    for i in range(9) :
        for j in range(9) :
            blank += (str(somelist[i][j]) + " ")
        print(blank)
        blank = "" 

class Solution :
    def solveSudoku(self, board) :
        checkzero = []

        for i in range(9) :
            for j in range(9) :
                if board[i][j] == "0" :
                    checkzero.append([i,j])

        N = len(checkzero)

        final = []

        DFS(N, 0, [], final, checkzero, board)

        for i in range(len(checkzero)) :
            board[checkzero[i][0]][checkzero[i][1]] = final[0][i]

a = Solution()

board = []

for i in range(9) :
    line = input()
    line = line.split()

    board.append(line)

a.solveSudoku(board)

printsdoku(board)
