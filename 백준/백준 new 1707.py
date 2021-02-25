from collections import deque

def bfs(start, graph, colorbox, visited) :
    visited[start] = 1
    
    if colorbox[start] == 0 :
        colorbox[start] = 1

        now = 2

    queue = deque([start])
    temp = []

    while queue :
        get = queue.popleft()

        for i in graph[get] :
            if colorbox[i] == 0 :
                colorbox[i] = now
            else :
                if colorbox[i] != now :
                    return False

            temp.append(i)

        for i in graph[get] :
            graph[i].remove(get)

        graph[get] = []

        if queue == deque([]) :
            if temp != [] :
                queue.extend(temp)
                temp = []
                if now == 1 :
                    now = 2
                else :
                    now = 1
            else :
                break

    return True

K = int(input())

for _ in range(K) :
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    colorbox = [0] * (V+1)
    visited = [0] * (V+1)

    for i in range(E) :
        a, b = map(int, input().split())

        graph[a].append(b)
        graph[b].append(a)

    check = True

    for i in range(1, V+1) :
        if not check :
            break
        else :
            if visited[i] == 0 :
                if not bfs(i, graph, colorbox, visited) :
                    check = False

    if check == True :
        print("YES")
    else :
        print("NO")
