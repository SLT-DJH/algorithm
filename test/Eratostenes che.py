a = int(input())

erabox  = []

answer = []

for i in range(a) :
    erabox.append(i+1)

erabox.remove(1)

while erabox != [] :
    x = erabox[0]

    answer.append(x)

    for i in range(big // x) :
        data = (i+1) * x

        if erabox.count(data) != 0 :
            erabox.remove(data)            
    

print(answer)
