a = input()

a = list(map(int, a.split()))

box = []

sample = []

totalbox = []

for _ in range(a[1]) :
    sample.append(0)
    
totalbox.append(sample)

for i in range(a[0]) :
    box.append(input())
    box[i] = list(map(int, box[i].split()))
    total = []
    totalsum = 0
    for number in range(a[1]) :
        totalsum = totalsum + box[i][number] + totalbox[i][number]
        total.append(totalsum)
        totalsum = totalsum - totalbox[i][number]
    totalbox.append(total)

b = int(input())

position = []

for k in range(b) :
    position.append(input())
    position[k] = list(map(int, position[k].split()))
    i = position[k][0]
    j = position[k][1]
    x = position[k][2]
    y = position[k][3]
    if j-1 == 0 :
        print(totalbox[x][y-1] - totalbox[i-1][y-1] - totalbox[0][j-1] + totalbox[0][j-1])
    else:
        print(totalbox[x][y-1] - totalbox[i-1][y-1] - totalbox[x][j-2] + totalbox[i-1][j-2])
