def calcul(totalcost) :
    total = 0

    for i in range(N-1) :
        total+= cost[int(totalcost[i])][int(totalcost[i+1])]

    return total


def dfs_recursive(graph, start, visited=[]):
    
    visited = visited + [start] ## visited.append(start)대신 visited = visited + [start]를 대입
    if len(visited) == N :
        totalbox.append(calcul(visited)) # print(visited) 추가
    
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    
    return visited

N = int(input())

M = int(input())

cost = []

graph = {}

for i in range(N) :
    graph[str(i+1)] = []

for i in range(N+1) :
    box = []
    for j in range(N+1) :
        box.append(0)
    cost.append(box)

for i in range(M) :
    line = input()
    line = list(map(int, line.split()))

    a = line[0]
    b = line[1]
    c = line[2]

    cost[a][b] = c
    cost[b][a] = c

    graph[str(a)].append(str(b))
    graph[str(b)].append(str(a))

print(cost)
print(graph)

totalbox = []

dfs_recursive(graph, '1')

print(totalbox)


