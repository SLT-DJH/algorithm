from collections import deque

def check(graph, colorbox) :
    previous = 0
    nownum = 1
   
    colorbox[1] = 1
    
    now = 2
    queue = deque([1])
    temp = []
    answer = 0
    
    while queue :
        v = queue.popleft()
        
        for i in graph[v] :
            if colorbox[i] == 0 :
                colorbox[i] = now
            elif colorbox[i] != now :
                answer = 1
                break
            temp.append(i)
            previous, nownum = nownum, i
            graph[previous].remove(nownum)
            graph[nownum].remove(previous)            
        
        if answer == 1 :
            break
        
        if queue == deque([]) :
            if temp != [] :
                queue.extend(temp)
                temp = []
                if now == 1 :
                    now = 2
                elif now == 2 :
                    now = 1
            else :
                break

    if answer == 1 :
        return False
    
    if answer == 0 :
        return True   

K = int(input())

for _ in range(K) :
    V, E = map(int, input().split())
    
    graph = {}
    colorbox = [0] * (V+1)
    
    for i in range(1, V+1) :
        graph[i] = []
    
    for i in range(E) :
        a, b = map(int, input().split())
        
        graph[a].append(b)
        graph[b].append(a)
    
    if check(graph, colorbox) :
        print("YES")
    else :
        print("NO")
