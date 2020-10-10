N = int(input())

box = []

for _ in range(N) :
    a, b = map(int, input().split())

    box.append([-a,b])

print(sorted(box))
