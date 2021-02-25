def go(start, visited, graph) :
    if visited[start] == 0 :
        visited[start] = 1
    else :
        return

    go(graph[start], visited, graph)
    

T = int(input())

for _ in range(T) :
    N = int(input())

    graph = [0] * (N+1)
    visited = [0] * (N+1)

    mlist = list(map(int, input().split()))

    for i in range(N) :
        graph[i+1] = mlist[i]
        
    cycle = 0

    for i in range(1, N+1) :
        if visited[i] == 0 :
            go(i, visited, graph)
            cycle += 1

    print(cycle)
