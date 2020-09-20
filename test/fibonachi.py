a = int(input())

n = 0
m = 1

box = 0

for i in range(a) :
    box = m
    m = m + n
    n = box
    

print(box)
