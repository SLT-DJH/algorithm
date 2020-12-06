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
        if x in truthlist :
            graph[y] = x
        elif y in truthlist :
            graph[x] = y
        else :
            graph[y] = x

N, M = map(int, input().split())

getnum = list(map(int, input().split()))

counttruth = getnum[0]

truthlist = getnum[1:]

graph = {}

for i in range(1, N+1) :
    graph[i] = i

checkbox = []

for _ in range(M) :
    unionlist = list(map(int, input().split()))[1:]

    unionlist = sorted(list(set(unionlist)))

    checkbox.append(unionlist)

    if len(unionlist) != 1 :
        for i in range(len(unionlist)-1) :
            a = unionlist[i]
            b = unionlist[i+1]

            union(a, b)

            for j in graph.keys() :
                find(j)
answer = 0

for i in checkbox :
    get = find(i[0])

    if get not in truthlist :
        answer += 1

print(answer)
