import sys
sys.setrecursionlimit(10**8)

def find(y,x) :

    global sheep
    global wolf

    change = []

    mymap[y][x] = '-'
    
    up = y-1
    down = y+1
    left = x-1
    right = x+1

    temporary = [[up,x],[down,x],[y,left],[y,right]]

    for i in range(4) :
        if temporary[i][1] <= 0 or temporary[i][1] > C or temporary[i][0] <= 0 or temporary[i][0] > R :
            continue
        else :
            if mymap[temporary[i][0]][temporary[i][1]] == '#' or mymap[temporary[i][0]][temporary[i][1]] == '-' :
                continue
            elif mymap[temporary[i][0]][temporary[i][1]] == 'v' :
                wolf = wolf + 1
                change.append(temporary[i])
            elif mymap[temporary[i][0]][temporary[i][1]] == 'o' :
                sheep = sheep + 1
                change.append(temporary[i])
            else :
                change.append(temporary[i])
    if change != [] :
        
        for i in range(len(change)) :
            mymap[change[i][0]][change[i][1]] = '-'
        for i in range(len(change)) :
            find(change[i][0], change[i][1])
        

matrix = input()
matrix = list(map(int,matrix.split()))


R = matrix[0]
C = matrix[1]

mymap = []
myvisited = []

tempbox = []

tempbox.append('0')

for i in range(C) :
    tempbox.append('0')

mymap.append(tempbox)

for i in range(R) :
    line = input()
    box = []
    box.append('0')
    for j in range(C) :
        box.append(line[j])
    mymap.append(box)

total = []

box = []

wolf = 0

sheep = 0

totalwolf = 0

totalsheep = 0

for i in range(R+1) :
    for j in range(C+1) :
        check = mymap[i][j]
    
        if check == '.' :
            find(i,j)

            if wolf == 0 and sheep == 0 :
                continue
            else :
                box.append(wolf)
                box.append(sheep)
                total.append(box)
                box = []
                wolf = 0
                sheep = 0
        elif check == 'v' :
            wolf = wolf + 1
            find(i,j)

            box.append(wolf)
            box.append(sheep)
            total.append(box)
            box = []
            wolf = 0
            sheep = 0
                
        elif check == 'o' :
            sheep = sheep + 1
            find(i,j)

            box.append(wolf)
            box.append(sheep)
            total.append(box)
            box = []
            wolf = 0
            sheep = 0
            
for i in range(len(total)) :
    check = total[i]

    w = check[0]
    s = check[1]

    if s > w :
        w = 0
    else :
        s = 0

    totalwolf = totalwolf + w
    totalsheep = totalsheep + s
                

print(str(totalsheep) + " " + str(totalwolf))
