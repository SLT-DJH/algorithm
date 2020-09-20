import sys

sys.setrecursionlimit(10**5)

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

N = int(input())

M = int(input())

cost = []

union = {}

for i in range(M) :
    line = input()

    line = list(map(int, line.split()))

    cost.append(line[2])

    if line[0] > line[1] :
        union[i] = [line[1], line[0]]
    else :
        union[i] = [line[0], line[1]]

getunion = []

for i in range(N+1) :
    getunion.append(i)

total = 0

path = []

while len(path) != (N-1) :
    mini = min(cost)

    if unioncal(union[cost.index(mini)]) :
        path.append(union[cost.index(mini)])
        total += mini

    cost[cost.index(mini)] = 10001

print(total)


