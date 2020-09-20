n = int(input())

box = []

for _ in range(n) :
    line = input()
    line = list(map(int, line.split()))

    if box == [] :
        box = line
    else :
        tempbox = []
        
        for i in range(len(line)) :
            if i == 0 :
                tempbox.append(box[0] + line[i])
            elif i == len(line) - 1 :
                tempbox.append(box[len(box)-1] + line[i])
            else :
                first = box[i-1]
                second = box[i]

                if first < second :
                    tempbox.append(second + line[i])
                else :
                    tempbox.append(first + line[i])

        box = tempbox

print(max(box))
