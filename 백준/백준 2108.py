box = []

graph = {}

N = int(input())

center = N // 2

for _ in range(N) :
    get = int(input())

    if get not in graph :
        graph[get] = 1
    else :
        graph[get] += 1

    box.append(get)

box.sort()

bing = sorted(graph.items(), key = lambda x : (x[1], -x[0]))

# 산술평균
print(round(sum(box) / N))

# 중앙값
print(box[center])

# 최빈값
if N == 1 :
    print(bing[0][0])
else :
    if bing[-1][1] == bing[-2][1] :
        print(bing[-2][0])
    else :
        print(bing[-1][0])

# 범위
print(box[-1] - box[0])
