N = int(input())

graph = []

for i in range(N) :
    graph.append([])

for i in range(N) :
    line = list(map(int, input().split()))

    for j in range(N) :
        if line[j] == 1 :
            graph[i].append(j)
            graph[j].append(i)

print(graph)
