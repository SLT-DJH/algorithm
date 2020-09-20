boxx = []
boxy = []

answer = []

for i in range(3) :
    a = input()

    a = list(map(int, a.split()))

    boxx.append(a[0])
    boxy.append(a[1])

for i in boxx :
    if boxx.count(i) == 1 :
        answer.append(i)
        
for i in boxy :
    if boxy.count(i) == 1 :
        answer.append(i)
        
print(answer[0], answer[1])
    
