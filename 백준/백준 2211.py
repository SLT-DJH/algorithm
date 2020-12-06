import heapq

N, M = map(int, input().split())

answer = []

visited = [0 for i in range(N+1)]

visited[0] = 1

box = []

for _ in range(M) :
    A, B, C = map(int, input().split())

    heapq.heappush(box, [C, A, B])


while sum(visited) != N+1 :
    q = heapq.heappop(box)

    a = q[1]
    b = q[2]

    if visited[a] == 0 and visited[b] == 0 :
        visited[a] = 1
        visited[b] = 1
        answer.append([a, b])

    elif visited[a] == 0 :
        visited[a] = 1
        answer.append([a,b])
    elif visited[b] == 0 :
        visited[b] = 1
        answer.append([a,b])

print(len(answer))

for i in answer :
    print(i[0], i[1])
