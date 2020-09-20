a = input()

a = list(map(int, a.split()))

box = []

for i in range(a[0]) :
    box.append(i+1)

box.remove(1)

count = 0

answer = 0


while len(box) != 0 :
    P = box[0]
    big = box[len(box) - 1]
    for i in range(big // P) :
        data = (i+1) * P
        if box.count(data) == 0 :
            continue
        else :
            box.remove(data)
            count = count + 1
            if count == a[1] :
                answer = answer + data
            
print(answer)
