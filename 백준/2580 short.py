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

for i in range(9) :
    line = input()
    line = list(map(int, line.split()))

    mymap.append(line)

blank = []

for i in range(9) :
        for j in range(9) :
            if mymap[i][j] == 0 :
                basket = [i, j]
                blank.append(basket)

while blank != [] :

    tempblank = []

    for i in range(9) :
        for j in range(9) :
            if mymap[i][j] == 0 :
                basket = [i, j]
                tempblank.append(basket)
    
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

    for i in range(9) :
        for j in range(9) :
            if mymap[i][j] == 0 :
                basket = [i, j]
                blank.append(basket)
    
    blank = []

    for i in range(9) :
            for j in range(9) :
                if mymap[i][j] == 0 :
                    basket = [i, j]
                    blank.append(basket)
    if tempblank == blank :
        break
    
printsdoku(mymap)
