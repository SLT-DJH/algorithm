
def find(x) :
    if graph[x] == x :
        return x
    else :
        p = find(graph[x])

        graph[x] = p

        return p

def union(x, y) :
    x, y = find(x), find(y)

    if x != y :
        graph[y] = x

N, M = map(int, input().split())

graph = {}

for i in range(1, N+1) :
    graph[i] = i

getnum = list(map(int, input().split()))

counttruth = getnum[0]

truthlist = getnum[1:]

checkbox = []

for _ in range(M) :
    unionlist = list(map(int, input().split()))

    unionlist = sorted(list(set(unionlist)))

    checkbox.append(unionlist)

    for i in range(len(unionlist)-1) :
        a = unionlist[i]
        b = unionlist[i+1]

        union(a, b)

print(truthlist, graph.values(), checkbox)
