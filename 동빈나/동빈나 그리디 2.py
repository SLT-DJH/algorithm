N, M = map(int, input().split())

card = []
box = []

for _ in range(N) :
    line = list(map(int, input().split()))

    line.sort()

    box.append(line[0])


box.sort()

print(box[N-1])

