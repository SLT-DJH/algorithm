a = int(input())

answer = 0

box = []

for _ in range(a) :
    get = int(input())

    box.append(get)

box.sort()

for i in range(len(box)) :
    temp = (a-i) * box[i]

    if answer < temp :
        answer = temp

print(answer)
