N, C = map(int, input().split())

box = []

for _ in range(N) :
    box.append(int(input()))

box.sort()

start = 1
end = box[-1] - box[0]
answer = 0

while start <= end :
    mid = (start + end) // 2

    count = 1

    temp = box[0]

    for i in range(1, N) :
        if mid <= box[i] - temp :
            count += 1
            temp = box[i]

    if count >= C :
        start = mid + 1
        answer = mid
    else :
        end = mid - 1

print(answer)
