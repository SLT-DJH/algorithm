T = int(input())

for _ in range(T) :
    n = int(input())

    graph= {}
    wearlist = []
    for _ in range(n) :
        a, b = map(str, input().split())

        graph[a] = b
        wearlist.append(a)

    wearbox = list(graph.values())

    wearbox = set(wearbox)
    wearbox = list(wearbox)
    answer = []

    for i in range(len(wearbox)) :
        answer.append([])

    for i in wearlist :
        answer[wearbox.index(graph[i])].append(i)
        
    count = 1

    for i in answer :
        count = count * (len(i) + 1)

    print(count - 1)
