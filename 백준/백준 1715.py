import heapq

N = int(input())

box = []

for _ in range(N) :
    heapq.heappush(box, int(input()))

if N == 1 :
    print(box[0])
else :

    count = 0

    while len(box) != 1 :
        a = heapq.heappop(box)

        b = heapq.heappop(box)

        count += a
        count += b

        heapq.heappush(box, a+b)

    print(count)
