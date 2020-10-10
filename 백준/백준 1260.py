def DFS(graph, start, visited, N) :
    stack = []

    stack += [start]

    while stack :
        n = stack.pop()
        if n not in visited :
            visited.append(n)
            graph[n].reverse()
            stack.extend(graph[n])

    return visited

def BFS(graph, start, visited, N) :
    queue = []

    queue += [start]

    while queue :
        n = queue.pop(0)
        if n not in visited :
            visited.append(n)
            graph[n].reverse()
            queue.extend(graph[n])

    return visited

def get(numlist) :
    answer = ""

    for i in numlist :
        answer += str(i)
        answer += " "

    return answer

N, M, start = map(int, input().split())

graph = {}

for i in range(N) :
    graph[i+1] = []

for _ in range(M) :
    a, b = map(int, input().split())

    if b not in graph[a] :
        graph[a].append(b)

    if a not in graph[b] :
        graph[b].append(a)

for i in range(N) :
    graph[i+1].sort()

dfs = DFS(graph, start, [], N)
bfs = BFS(graph, start, [], N)

print(get(dfs))
print(get(bfs))
