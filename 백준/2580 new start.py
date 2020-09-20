import sys

def checksdoku(x, y, z) :
    checkmymap = []
    
    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(mymap[i][j])
        checkmymap.append(box)
        
    checkmymap[x][y] = z

    temprow = row(checkmymap)
    tempcolumn = column(checkmymap)
    tempsquare = square(checkmymap)

    for i in range(9) :
        for j in range(9) :
            if temprow[i].count(j+1) <= 1 and tempcolumn[i].count(j+1) <= 1 and tempsquare[i].count(j+1) <= 1 :
                continue
            else :
                return False
    return True

def boolsdoku(mapmap) :
    temprow = row(mapmap)
    tempcolumn = column(mapmap)
    tempsquare = square(mapmap)

    for i in range(9) :
        for j in range(9) :
            if temprow[i].count(j+1) <= 1 and tempcolumn[i].count(j+1) <= 1 and tempsquare[i].count(j+1) <= 1 :
                continue
            else :
                return False
    return True
    

def dfs_recursive(graph, start) :

    for node in graph[start] :
        mymap[blank[start][0]][blank[start][1]] = node
        if boolsdoku(mymap) :
            if start + 1 < len(graph) :
                dfs_recursive(graph, start + 1)
                
            if start + 1 == len(graph) :
                printsdoku(mymap)
                sys.exit()

        mymap[blank[start][0]][blank[start][1]] = 0

def row(k) :
    row = []

    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(k[i][j])
        row.append(box)

    return row

def column(k) :
    column = []

    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(k[j][i])
        column.append(box)

    return column

def square(k) :
    square = []

    for i in range(9) :
        box = []
        for j in range(9) :
            box.append(k[(3 * (i//3)) + (j//3)][3 * (i%3) + (j%3)])
        square.append(box)

    return square

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

tempgraph = {}

while True :
    blank = []

    for i in range(9) :
            for j in range(9) :
                if mymap[i][j] == 0 :
                    basket = [i, j]
                    blank.append(basket)
    if blank == [] :
        break
    else :
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
        if graph == tempgraph :
            break
        else :
            tempgraph = graph

blank = []

for i in range(9) :
        for j in range(9) :
            if mymap[i][j] == 0 :
                basket = [i, j]
                blank.append(basket)
                
if blank == [] :
    printsdoku(mymap)
else :
    graph = {}

    for i in range(len(blank)) :
                graph[i] = []

    for i in range(len(blank)) :
                for j in range(9) :
                    if checksdoku(blank[i][0], blank[i][1], j+1) :
                        graph[i].append(j+1)
    dfs_recursive(graph, 0)
