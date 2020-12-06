T = int(input())

for _ in range(T) :
    N, K = map(int, input().split())

    timelist = list(map(int, input().split()))
    
    timelist = [0] + timelist

    dp = [0 for i in range(N+1)]

    visitcount = [0 for i in range(N+1)]
    
    visitcount[0] += 1
    
    graph = [[] for i in range(N+1)]

    for i in range(K) :
        start, end = map(int, input().split())
        
        visitcount[end] += 1

        graph[start].append(end)

    destination = int(input())

    if visitcount[destination] == 0 :
        print(timelist[destination - 1])
    else :
        stack = []
        
        for i in range(N+1) :
            if visitcount[i] == 0 :
                stack.append(i)
                dp[i] = timelist[i]
  
        while stack :
              
            q = stack.pop()
                    
            temp = []
          
            if graph[q] != [] :
                for i in graph[q] :
                    dp[i] = max(dp[i], dp[q] + timelist[i])
              
                    visitcount[i] -= 1
              
                    if visitcount[i] == 0 :
                        temp.append(i)
            
                stack.extend(temp)
        
        print(dp[destination])
