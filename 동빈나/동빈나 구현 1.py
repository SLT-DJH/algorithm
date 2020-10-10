N = input()

box = []

for i in N :
    box.append(i)

graph = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

x = graph[box[0]]
y = int(box[1])

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [-1, 1, -1, 1, -2, -2, 2, 2]

count = 0

for i in range(8) :
    cx = x + dx[i]
    cy = y + dy[i]

    if 1 <= cx < 9 and 1 <= cy < 9 :
        count += 1

print(count)
