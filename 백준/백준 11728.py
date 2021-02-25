A , B = map(int, input().split())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

pA = 0
pB = 0

answer = []

while True :
    if pA < A and pB < B :
        if listA[pA] >= listB[pB] :
            answer.append(listB[pB])
            pB += 1
        elif listA[pA] < listB[pB] :
            answer.append(listA[pA])
            pA += 1
    elif pA == A and pB == B :
        break
    elif pA == A :
        answer.append(listB[pB])
        pB += 1
    elif pB == B :
        answer.append(listA[pA])
        pA += 1

for i in answer :
    print(i, end = " ")
        
