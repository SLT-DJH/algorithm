def nextwater() :
    for i in range(len(water)) :
        check = water[i]
        x = check[0]
        y = check[1]
        up = y-1
        down = y+1
        left = x-1
        right = x+1

        temporary = [[x,up] , [x,down], [left,y], [right,y]]

        for i in range(len(temporary)) :
            if temporary[i][1] <= 0 or temporary[i][1] > R or temporary[i][0] <= 0 or temporary[i][0] > C :
                continue
            else :
                if temporary[i] in water or temporary[i] in hole or temporary[i] in rock :
                    continue
                else :
                    water.append(temporary[i])


def nextmole() :
    box = []
    
    for i in range(len(mole)) :
        box.append(mole[i])

    for i in range(len(box)) :
        mole.remove(box[i])
    
    for i in range(len(box)) :
        check = box[i]
        x = check[0]
        y = check[1]
        up = y-1
        down = y+1
        left = x-1
        right = x+1

        temporary = [[x,up] , [x,down], [left,y], [right,y]]

        for i in range(len(temporary)) :
            if temporary[i][1] <= 0 or temporary[i][1] > R or temporary[i][0] <= 0 or temporary[i][0] > C :
                continue
            else :
                if temporary[i] in water or temporary[i] in rock or temporary[i] in mole:
                    continue
                else :
                    mole.append(temporary[i])
    


matrix = input()
matrix = list(map(int, matrix.split()))

R = matrix[0]
C = matrix[1]

x = 0
y = 0

point = []

hole = []
water = []
mole = []
rock = []

for i in range(R) :
    check = input()
    for j in range(C) :
        if check[j] == 'D' :
            x = j+1
            y = i+1
            point.append(x)
            point.append(y)
            hole.append(point)
            x = 0
            y = 0
            point = []
        elif check[j] == '*' :
            x = j+1
            y = i+1
            point.append(x)
            point.append(y)
            water.append(point)
            x = 0
            y = 0
            point = []
        elif check[j] == 'S' :
            x = j+1
            y = i+1
            point.append(x)
            point.append(y)
            mole.append(point)
            x = 0
            y = 0
            point = []
        elif check[j] == 'X' :
            x = j+1
            y = i+1
            point.append(x)
            point.append(y)
            rock.append(point)
            x = 0
            y = 0
            point = []

count = 0

while True :
    count = count + 1
    nextwater()
    nextmole()
    if mole == [] :
        print('KAKTUS')
        break
    elif hole[0] in mole :
        print(count)
        break
            
