N = int(input())

box = []

for _ in range(N) :
    box.append(int(input()))

answer = 0

stack = [(0, box[0])]

position = 0

for i in range(1, N+1) :
    if i != N :
        height = box[i]
    else :
        height = 0
            
    position = i

    while stack and stack[-1][1] > height :
        position, temp = stack.pop()

        answer = max(answer, (temp * (i - position)))

    if i != N :
        stack.append((position, box[i]))

print(answer)

