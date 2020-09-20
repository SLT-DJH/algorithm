N = int(input())

box = []

for _ in range(N) :
    get = input()
    get = list(map(int, get.split()))

    box.append(get)

box = sorted(box, key = lambda time: time[0])
box = sorted(box, key = lambda time: time[1])

start = 0
count = 0

for time in box :
    if time[0] >= start :
        count += 1
        start = time[1]

print(count)
