def nextwater() :

    change = []

    for i in range(R+1) :
        for j in range(C+1) :
            if mymap[i][j] == 'S' :
                position.append([i,j])
                mymap[i][j] = '.'
    
    for i in range(R+1) :
        for j in range(C+1) :
            if mymap[i][j] == '*' :
                y = i
                x = j

                up = y-1
                down = y+1
                left = x-1
                right = x+1

                temporary = [[up,x],[down,x],[y,left],[y,right]]

                for k in range(4) :
                    if temporary[k][1] <= 0 or temporary[k][1] > C or temporary[k][0] <= 0 or temporary[k][0] > R :
                        continue
                    else :
                        if mymap[temporary[k][0]][temporary[k][1]] == '*' or mymap[temporary[k][0]][temporary[k][1]] == 'D' or mymap[temporary[k][0]][temporary[k][1]] == 'X' :
                            continue
                        else :
                            change.append(temporary[k])
    
    for i in range(len(change)) :
        mymap[change[i][0]][change[i][1]] = '*'

def nextmole () :
    change = []

    for i in range(len(position)) :
        y = position[i][0]
        x = position[i][1]

        up = y-1
        down = y+1
        left = x-1
        right = x+1

        temporary = [[up,x],[down,x],[y,left],[y,right]]

        for j in range(4) :
            if temporary[j][1] <= 0 or temporary[j][1] > C or temporary[j][0] <= 0 or temporary[j][0] > R :
                continue
            else :
                if mymap[temporary[j][0]][temporary[j][1]] == '*' or mymap[temporary[j][0]][temporary[j][1]] == 'X' :
                    continue
                elif myvisited[temporary[j][0]][temporary[j][1]] == 'S' :
                    continue
                else :
                    change.append(temporary[j])

    for i in range(len(change)) :
        mymap[change[i][0]][change[i][1]] = 'S'
        myvisited[change[i][0]][change[i][1]] = 'S'


matrix = input()
matrix = list(map(int, matrix.split()))

R = matrix[0]
C = matrix[1]

mymap = []
myvisited = []

position = []

target = []

tempbox = []

tempbox.append('0')

for i in range(C) :
    tempbox.append('0')

mymap.append(tempbox)
myvisited.append(tempbox)

for i in range(R) :
    line = input()
    box = []
    box2 = []
    box.append('0')
    box2.append('0')
    for j in range(C) :
        if line[j] == 'S' :
            box.append(line[j])
            box2.append('S')
        elif line[j] == 'D' :
            box.append(line[j])
            box2.append('0')
            target.append(i+1)
            target.append(j+1)
        else :
            box.append(line[j])
            box2.append('0')
    mymap.append(box)
    myvisited.append(box2)

count = 0

while True :
    count = count + 1
    nextwater()
    nextmole()
    if mymap[target[0]][target[1]] == 'S' :
        print(count)
        break
    if position == [] :
        print('KAKTUS')
        break
    position = []
