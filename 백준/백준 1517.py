a = int(input())

b = list(map(int, input().split()))

count = 0

def calcul(x, y) :
    global count

    temp = []

    xpoint = 0
    ypoint = 0

    while True :
        if xpoint == len(x) or ypoint == len(y) :
            if xpoint == len(x) :
                temp.append(y[ypoint])
                ypoint += 1
            elif ypoint == len(y) :
                temp.append(x[xpoint])
                xpoint += 1
        else :
            if x[xpoint] <= y[ypoint] :
                temp.append(x[xpoint])
                xpoint += 1
            else :
                temp.append(y[ypoint])
                ypoint += 1
                count += len(x) - xpoint

        if xpoint == len(x) and ypoint == len(y) :
            break
        
    return temp

div = []

for i in range(a) :
    div.append([b[i]])

while len(div) != 1 :
    
    newtree = [[]] * (len(div) // 2)

    if len(div) % 2 == 0 :
        for i in range(len(newtree)) :
            newtree[i] = calcul(div[i * 2], div[(i * 2) + 1])
    else :
        for i in range(len(newtree)) :
            if i == len(newtree)-1 :
                newtree[i] = calcul(calcul(div[i*2], div[(i*2)+1]), div[(i*2) + 2])
            else :
                newtree[i] = calcul(div[i * 2], div[(i * 2) + 1])

    div = newtree

print(count)
