matrix = input()
matrix = list(map(int, matrix.split()))

R = matrix[0]
C = matrix[1]

x = 0
y = 0

point = []

sheep = []
sharp = []
wolf = []
grass = []

for i in range(R) :
    check = input()
    for j in range(C) :
        if check[j] == 'o' :
            x = j+1
            y = i+1
            point.append(x)
            point.append(y)
            sheep.append(point)
            x = 0
            y = 0
            point = []
        elif check[j] == '#' :
            x = j+1
            y = i+1
            point.append(x)
            point.append(y)
            sharp.append(point)
            x = 0
            y = 0
            point = []
        elif check[j] == 'v' :
            x = j+1
            y = i+1
            point.append(x)
            point.append(y)
            wolf.append(point)
            x = 0
            y = 0
            point = []
        elif check[j] == '.' :
            x = j+1
            y = i+1
            point.append(x)
            point.append(y)
            grass.append(point)
            x = 0
            y = 0
            point = []
print(sheep)
print(sharp)
print(wolf)
print(grass)
