x = int(input())
y = int(input())

quadrant = 0

if x > 0 and y > 0 :
    quadrant = 1
elif x < 0 and y > 0 :
    quadrant = 2
elif x < 0 and y < 0 :
    quadrant = 3
else :
    quadrant = 4

print(quadrant)
