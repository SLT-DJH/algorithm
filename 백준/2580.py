def checksdoku(x, y, z) :
    checkmymap = []
    
    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(mymap[i][j])
        checkmymap.append(box)
        
    checkmymap[x][y] = z

    temprow = []
    tempcolumn = []
    tempsquare = []

    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(checkmymap[i][j])
        temprow.append(box)

    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(checkmymap[j][i])
        tempcolumn.append(box)

    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(checkmymap[(3 * (i//3)) + (j//3)][3 * (i%3) + (j%3)])
        tempsquare.append(box)

    for i in range(9) :
        for j in range(9) :
            if temprow[i].count(j+1) <= 1 and tempcolumn[i].count(j+1) <= 1 and tempsquare[i].count(j+1) <= 1 :
                continue
            else :
                return False
    return True

def printsdoku(somelist) :
    blank = ""
    for i in range(9) :
        for j in range(9) :
            blank += (str(somelist[i][j]) + " ")
        print(blank)
        blank = ""


mymap = []

tempmymap = []

for i in range(9) :
    line = input()
    line = list(map(int, line.split()))

    mymap.append(line)
        
while tempmymap != mymap :
    #tempmymap 설정
    for i in range(9) :
        tempmymap.append(mymap[i])

    row = []
    column = []
    square = []

    #row 구하기
    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(mymap[i][j])
        row.append(box)

    for i in range(9) :
        if sum(row[i]) >= 36 and sum(row[i]) <= 44 and row[i].count(0) == 1 :
            get = row[i].index(0)
            put = 45 - sum(row[i])
            mymap[i][get] = put


    #column 구하기
    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(mymap[j][i])
        column.append(box)

    for i in range(9) :
        if sum(column[i]) >= 36 and sum(column[i]) <= 44 and column[i].count(0) == 1 :
            get = column[i].index(0)
            put = 45 - sum(column[i])
            
            mymap[get][i] = put

    #square 구하기
    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(mymap[(3 * (i//3)) + (j//3)][3 * (i%3) + (j%3)])
        square.append(box)

    for i in range(9) :
        if sum(square[i]) >= 36 and sum(square[i]) <= 44 and square[i].count(0) == 1:
            get = square[i].index(0)
            put = 45 - sum(square[i])
            
            mymap[(3 * (i//3)) + (get//3)][3 * (i%3) + (get%3)] = put

total = 0

for i in range(9) :
    total += sum(mymap[i])

if total == 405 :
    printsdoku(mymap)
else :
    blank = []
    
    for i in range(9) :
        for j in range(9) :
            if mymap[i][j] == 0 :
                basket = [i, j]
                blank.append(basket)

    graph = {}

    for i in range(len(blank)) :
        graph[i] = []

    for i in range(len(blank)) :
        for j in range(9) :
            if checksdoku(blank[i][0], blank[i][1], j+1) :
                graph[i].append(j+1)

    for i in range(len(graph)) :
        if len(graph[i]) == 1 :
            mymap[blank[i][0]][blank[i][1]] = graph[i][0]

    printsdoku(mymap)
