N = int(input())

box = []

for _ in range(N) :
    a, b, c, d = input().split()
    ## name, korean, english, math

    box.append((str(a), int(b), int(c), int(d)))


box = sorted(box, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in box :
    print(i[0])
