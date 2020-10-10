def DFS(graph, start, visited) :
    stack = []

    stack += [start]

    while stack :
        n = stack.pop()
        if n not in visited :
            visited.append(n)
            stack.extend(graph[n])

    return visited

N = int(input())

M = int(input())

graph = {}

for i in range(N) :
    graph[i+1] = []

for _ in range(M) :
    a, b = map(int, input().split())

    if a not in graph[b] :
        graph[b].append(a)

    if b not in graph[a] :
        graph[a].append(b)

print(len(DFS(graph, 1, [])) - 1)
