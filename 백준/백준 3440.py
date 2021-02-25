from collections import deque

def change(x, y, box, to, R, C) :
    dx = [-1, 0, 0]
    dy = [0, 1, -1]

    queue = deque([(x,y)])

    visited = [(x,y)]

    box[y][x] = to

    tempqueue = []

    while queue :
        sx, sy = queue.popleft()

        for i in range(3) :
            cx = sx + dx[i]
            cy = sy + dy[i]

            if 0<= cx < R and 0 <= cy < C and box[cy][cx] == '#' and (cx, cy) not in visited :
                tempqueue.append((cx,cy))
                visited.append((cx,cy))
                box[cy][cx] = to
                
        if queue == deque([]) :
            queue.extend(tempqueue)
            tempqueue = []

def nega(x, y, box, R, C) :
    if box[y][x-1] == 0 :
        return 1
    elif box[y][x-1] == 1 :
        return 0
    else :
        return gate(x-1, y, box, -2, R, C)

def check(x, y, box, R, C) :

    if box[y][x] == '1' :
        return '1', x, y
    elif box[y][x] == '=' :
        return '=', x, y
    elif box[y][x] == '&' :
        return '&', x, y
    
    dx = [-1, 0, 0]
    dy = [0, 1, -1]

    queue = deque([(x,y)])

    visited = [(x,y)]

    tempqueue = []

    whatis = ""

    while queue and whatis == "":
        sx, sy = queue.popleft()

        for i in range(3) :
            cx = sx + dx[i]
            cy = sy + dy[i]

            if 0 <= cx < R and 0 <= cy < C :

                if box[cy][cx] == '.' and (cx, cy) not in visited:
                    tempqueue.append((cx, cy))
                    visited.append((cx, cy))
            
                if box[cy][cx] == '1' :
                    whatis = '1'
                    wx = cx
                    wy = cy
                    break
                elif box[cy][cx] == '=' :
                    whatis = '='
                    wx = cx
                    wy = cy
                    break
                elif box[cy][cx] == '&' :
                    whatis = '&'
                    wx = cx
                    wy = cy
                    break

        if queue == deque([]) :
            queue.extend(tempqueue)
            tempqueue = []

    return (whatis, wx, wy)

def gate(x, y, box, negative, R, C) :
    ## check what gate

    what, wx, wy = check(x-1, y, box, R, C)

    gatebox = []

    queue = deque([(x,y)])

    tempqueue = []
    visited = [(x,y)]

    dx = [-1, 0, 0]
    dy = [0, 1, -1]

    while queue :
        sx, sy = queue.popleft()

        for i in range(3) :
            cx = sx + dx[i]
            cy = sy + dy[i]

            if (cx,cy) not in visited and 0<= cx < R and 0 <= cy < C :
                if box[cy][cx] == '#':
                    tempqueue.append((cx,cy))
                    visited.append((cx,cy))

                    if cx-1 >= 0 and (cx-1, cy) != (wx, wy) and box[cy][cx-1] == '=' :
                        a = left(cx-1, cy, box, R, C)
                        gatebox.append(a)

        if queue == deque([]) :
            queue.extend(tempqueue)
            tempqueue = []

    gateanswer = -1

    if gatebox == [] :
        if what == '1' :
            gateanswer = 0
        elif what == '&' :
            gateanswer = 1
        elif what == '=' :
            gateanswer = 0
    else :

        if what == '1' :
            if sum(gatebox) == 0 :
                gateanswer = 0
            elif sum(gatebox) == len(gatebox) :
                gateanswer = 1
            else :
                gateanswer = 1
        elif what == '&' :
            if sum(gatebox) == 0 :
                gateanswer = 0
            elif sum(gatebox) == len(gatebox) :
                gateanswer = 1
            else :
                gateanswer = 0
        elif what == '=' :
            if sum(gatebox) == 0 :
                gateanswer = 0
            elif sum(gatebox) % 2 == 1 :
                gateanswer = 1
            elif sum(gatebox) % 2 == 0 :
                gateanswer = 0

    if negative == 2 :
        change(x, y, box, gateanswer, R, C)
        return gateanswer
    elif negative == -2 :
        if gateanswer == 1 :
            change(x, y, box, 1, R, C)
            return 0
        elif gateanswer == 0 :
            change(x, y, box, 0, R, C)
            return 1

def up(x, y, box, R, C) :
    if box[y-1][x] == 'x' or box[y-1][x] == '|' :
        return up(x, y-1, box, R, C)
    elif box[y-1][x] == '+' :
        return plus(x, y-1, box, R, C)    

def plus(x, y, box, R, C) :
    if (x-1) >= 0 :
        if box[y][x-1] == '-' or box[y][x-1] == '=' or box[y][x-1] == 'x' or box[y][x-1] == '+':
            return left(x-1, y, box, R, C)
        elif (y-1) >= 0 :
            if box[y-1][x] == '|' or box[y-1][x] == 'x' or box[y-1][x] == '+':
                return up(x, y-1, box, R, C)

def left(x, y, box, R, C) :
    if box[y][x-1] == '0' or box[y][x-1] == 0:
        return 0
    elif box[y][x-1] == '1' or box[y][x-1] == 1:
        return 1
    elif box[y][x-1] == '-' or box[y][x-1] == '=' or box[y][x-1] == 'x':
        return left(x-1, y, box, R, C)
    elif box[y][x-1] == '#' :
        return gate(x-1, y, box, 2, R, C)
    elif box[y][x-1] == '+' :
        return plus(x-1, y, box, R, C)
    elif box[y][x-1] == 'o' :
        return nega(x-1, y, box, R, C)

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

getbox = []

graph = {}

star = 0

box = []

while True :
    temp = []

    get = str(input())

    if len(get) == 0 :
        star = 0
        
        for i in get :
            temp.append('.')

        box.append(temp)
    else :        

        if get[0] == '*' :
            if star == 0 :
                star = 1
                
                C = len(box)
                R = 0

                for i in box :
                    R = max(R, len(i))

                for i in box :
                    if len(i) < R :
                        for _ in range(R-len(i)) :
                            i.append('.')
                    
                for i in range(C) :
                    for j in range(R) :
                        if box[i][j] in alpha :
                            getbox.append(box[i][j])
                            graph[box[i][j]] = left(j, i, box, R, C)
                getbox.sort()
                for i in getbox :
                    ans = i + "=" + str(graph[i])
                    print(ans)
                
                box = []
                getbox = []
                graph = {}
            elif star == 1 :
                break
        else :
            star = 0
            
            for i in get :
                if i == ' ' :
                    temp.append('.')
                else :
                    temp.append(i)

            box.append(temp)
