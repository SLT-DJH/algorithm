import math

box = []


for i in range(5) :
    score = int(input())
    if score < 40 :
        score = 40

    box.append(score)

print(math.floor(sum(box) / 5))
