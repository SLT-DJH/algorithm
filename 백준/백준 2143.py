T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

Abox = {}
Bbox = {}

for i in range(n) :
    item = A[i]

    if item in Abox :
        Abox[item] += 1
    else :
        Abox[item] = 1

    for j in range(i+1, n) :
        item += A[j]

        if item in Abox :
            Abox[item] += 1
        else :
            Abox[item] = 1

for i in range(m) :
    item = B[i]

    if item in Bbox :
        Bbox[item] += 1
    else :
        Bbox[item] = 1

    for j in range(i+1, m) :
        item += B[j]

        if item in Bbox :
            Bbox[item] += 1
        else :
            Bbox[item] = 1

answer = 0

for i in Bbox.keys() :
    get = T - i

    if get in Abox :
        answer += Abox[get]

print(answer)



