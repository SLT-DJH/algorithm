import sys

input = sys.stdin.readline

def find(x) :
    if position[x] == x :
        return x
    else :
        p = find(position[x])

        position[x] = p

        return p

def union(x, y) :
    x, y = find(x), find(y)

    if x != y :
        position[y] = x

        number[x] += number[y]
    print(number[x])
        

T = int(input())

for _ in range(T) :
    N = int(input())

    position, number = {}, {}

    for i in range(N) :
        a, b = map(str, input().split())

        if a not in position :
            position[a] = a
            number[a] = 1

        if b not in position :
            position[b] = b
            number[b] = 1

        union(a, b)
