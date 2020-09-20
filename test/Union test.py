def find(node) :
    if getunion[node] != node :
        getunion[node] = find(getunion[node])
    return getunion[node]


def change(a, b) :
    a = find(a)
    b = find(b)

    if a != b :
        getunion[b] = a

def makeset(node) :
    getunion[node] = find(node)
        

def unioncal(k) :
    temp = []

    for i in range(N+1) :
        temp.append(getunion[i])

    change(k[0], k[1])

    for i in range(N+1) :
        makeset(i)

    if getunion == temp :
        return False
    else :
        return True

N = 6
getunion = [0, 1, 2, 3, 4, 5, 6]
