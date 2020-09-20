N = int(input())

box = []

for _ in range(N) :
    line = input()
    line = list(map(int, line.split()))
    
    if box == [] :
        box = line
    else :
        tempbox = []

        for i in range(len(line)) :
            first = -1
            second = -1

            for j in range(len(box)) :
                if j != i :
                    if first == -1 :
                        first = box[j]
                    else :
                        second = box[j]

            if first < second :
                tempbox.append(first + line[i])
            else :
                tempbox.append(second + line[i])

        box = tempbox

print(min(box))
