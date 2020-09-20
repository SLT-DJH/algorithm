out = 0

score = 0

b1, b2, b3 = 0, 0, 0

while True :
    a = int(input())

    if a == 0 :
        out += 1
    elif a == 1 :

        score += b3

        b1, b2, b3 = 1, b1, b2
       
    elif a == 2 :

        score += b3
        score += b2

        b1, b2, b3 = 0, 1, b1

    elif a == 3 :

        score += b3
        score += b2
        score += b1

        b1, b2, b3 = 0, 0, 1

    else :

        score += b3
        score += b2
        score += b1
        score += 1

        b1, b2, b3 = 0, 0, 0

    if out == 3 :
        break

    print("score : ", score, " ", "b1 : ", b1, "b2 : ", b2, "b3 :  ", b3, "out : ", out)

print("inning over")
