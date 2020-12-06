def check(x, y, graph, N, visited) :
    visited.append(x)
    
    if graph[x] == [] :
        return False
    else :
        if y in graph[x] :
            return True
        else :
            answer = 0
            
            for i in graph[x] :
                if i not in visited :
                    if check(i, y, graph, N, visited) :
                        answer = 1

            if answer == 1 :
                return True
            else :
                return False

N = int(input())

graph = {}

for i in range(1, N+1) :
    graph[i] = []

for i in range(N) :
    get = list(map(int, input().split()))
    
    for j in range(N) :
        if get[j] == 1 :
            graph[i+1].append(j+1)

answer = [[0 for i in range(N)] for i in range(N)]

for i in range(N) :
    for j in range(N) :
        if check(i+1, j+1, graph, N, []) :
            answer[i][j] = 1
            
for i in range(N) :
    form = ""
    for j in range(N) :
        form += str(answer[i][j])
        form += " "
    print(form)
